import vcs
import numpy
import vcsaddons


def circle_points(center, radius, points=75, ratio=1):
    """
    Generates the coordinates of a circle in x list and y list.
    """
    x = []
    y = []
    if ratio > 1:
        ymul = ratio
        xmul = 1
    else:
        xmul = ratio
        ymul = 1
    for i in range(points):
        x.append(
            center[0] +
            xmul *
            radius *
            numpy.cos(
                float(i) /
                points *
                numpy.pi *
                2))
        y.append(
            center[1] +
            ymul *
            radius *
            numpy.sin(
                float(i) /
                points *
                numpy.pi *
                2))
    x.append(x[0])
    y.append(y[0])
    return x, y


def convert_arrays(var, theta):
    """
    Normalizes valid input options to two lists of lists of values and a list of names.

    Handles:
    list/tuple of list/tuples/arrays
    (X,N,2) array
    (N,2) array
    list/tuple, list/tuple
    """
    magnitudes = []
    thetas = []
    names = []
    if theta is None:
        # var must be list/tuple of arrays or an array
        if isinstance(var, (list, tuple)):
            for arr in var:
                if isinstance(arr, numpy.ndarray):
                    if len(arr.shape) == 2 and arr.shape[1] == 2:
                        magnitudes.append(arr[..., 0].tolist())
                        thetas.append(arr[..., 1].tolist())
                        try:
                            names.append(arr.id)
                        except AttributeError:
                            names.append(None)
                    else:
                        raise ValueError("Array is wrong shape; expected 2d array of 2-long elements,"
                                         " got %dd array of %d-long elements." % (len(arr.shape), arr.shape[-1]))
                else:
                    if len(arr) == 2:
                        # Might be just a pair
                        if not isinstance(arr[0], (list, tuple)):
                            magnitudes.append([arr[0]])
                            thetas.append([arr[1]])
                            names.append(None)
                            continue
                    mag_group = []
                    theta_group = []
                    for val in arr:
                        if len(val) != 2:
                            raise ValueError("List is wrong shape; expected list/tuple of 2 element list/tuples,"
                                             " got %s of %d elements." % (type(val).__name__, len(val)))
                        mag_group.append(val[0])
                        theta_group.append(val[1])
                        names.append(None)
                    magnitudes.append(mag_group)
                    thetas.append(theta_group)
        else:
            if len(var.shape) == 3:
                for i in range(var.shape[0]):
                    magnitudes.append(var[i, ..., 0].tolist())
                    thetas.append(var[i, ..., 1].tolist())
                    try:
                        names.append(var[i].id)
                    except AttributeError:
                        names.append(None)
            else:
                magnitudes = [var[..., 0].tolist()]
                thetas = [var[..., 1].tolist()]
                try:
                    names.append(var.id)
                except AttributeError:
                    names.append(None)
    else:
        magnitudes = []
        if isinstance(var, (list, tuple)):
            if isinstance(var[0], (list, tuple, numpy.ndarray)):
                for v in var:
                    magnitudes.append(list(v))
                    try:
                        names.append(v.id)
                    except AttributeError:
                        names.append(None)
            else:
                magnitudes = [var]
                names.append(None)
        elif isinstance(var, numpy.ndarray):
            if len(var.shape) == 1:
                magnitudes = [list(var)]
                try:
                    names.append(var.id)
                except AttributeError:
                    names.append(None)
            elif len(var.shape) == 2:
                for i in range(var.shape[0]):
                    magnitudes.append(list(var[i]))
                    try:
                        names.append(var[i].id)
                    except AttributeError:
                        names.append(None)
            else:
                raise ValueError("Array is wrong shape; expected 1d array or 2d array,"
                                 " got %dd array." % len(var.shape))

        thetas = []
        if isinstance(theta, (list, tuple)):
            if isinstance(theta[0], (list, tuple, numpy.ndarray)):
                thetas = [list(v) for v in theta]
            else:
                thetas = [theta]
        elif isinstance(theta, numpy.ndarray):
            if len(theta.shape) == 1:
                thetas = [list(theta)]
            elif len(theta.shape) == 2:
                thetas = [list(theta[i]) for i in range(theta.shape[0])]
            else:
                raise ValueError("Array is wrong shape; expected 1d array or 2d array,"
                                 " got %dd array." % len(var.shape))
        if not names:
            names = [None] * len(var)
    return magnitudes, thetas, names


class Gpo(vcsaddons.core.VCSaddon):
    __slots__ = ("markersizes","markercolors","markertypes", "markercolorsource","markerpriority", "clockwise","theta_offset","theta_tick_count", "magnitude_ticks","magnitude_mintics","magnitude_tick_angle","negative_magnitude","group_names","connect_groups","linecolors","linetypes","linewidths","linepriority","to_cleanup")
    def __init__(self, name=None, source="default", x=None, template=None):
        self.g_name = "Gpo"
        self.g_type = "polar_oned"
        super(Gpo, self).__init__(name, source, x, template)
        self.x = None
        if source == "default":
            self.markersizes = [3]
            self.markercolors = ["black"]
            self.markertypes = ["dot"]
            self.markercolorsource = "group"
            self.markerpriority = 2
            self.clockwise = False
            self.theta_offset = 0
            self.theta_tick_count = 6
            self.magnitude_ticks = "*"
            self.magnitude_mintics = None
            self.magnitude_tick_angle = 0
            self.negative_magnitude = False
            self.group_names = []
            self.connect_groups = False
            self.linecolors = ["black"]
            self.linetypes = ["solid"]
            self.linewidths = [1]
            self.linepriority = 0
            # Nice default labels
            self.xticlabels1 = {
                0: "0 (2pi)",
                numpy.pi / 4: "pi/4",
                numpy.pi / 2: "pi/2",
                numpy.pi * 3 / 4.: "3pi/4",
                numpy.pi: "pi",
                numpy.pi * 5 / 4.: "5pi/4",
                numpy.pi * 3 / 2.: "3pi/2",
                numpy.pi * 7 / 4.: "7pi/4",
            }
        else:
            if isinstance(source, (str, unicode)):
                gm = vcsaddons.gms[self.g_name][source]
            else:
                gm = source
            self.markersizes = gm.markersizes
            self.markercolors = gm.markercolors
            self.markertypes = gm.markertypes
            self.markercolorsource = gm.markercolorsource
            self.markerpriority = gm.markerpriority
            self.clockwise = gm.clockwise
            self.linecolors = gm.linecolors
            self.linewidths = gm.linewidths
            self.linepriority = gm.linepriority
            self.linetypes = gm.linetypes
            self.connect_groups = gm.connect_groups
            self.theta_offset = gm.theta_offset
            self.magnitude_ticks = gm.magnitude_ticks
            self.magnitude_mintics = gm.magnitude_mintics
            self.magnitude_tick_angle = gm.magnitude_tick_angle
            self.negative_magnitude = gm.negative_magnitude
            self.theta_tick_count = gm.theta_tick_count
            self.group_names = gm.group_names
        self.to_cleanup = []

    def list(self):
        print 'graphics method = ',self.g_name
        print 'name = ',self.name
        print 'datawc_x1 = ',self.datawc_x1
        print 'datawc_x2 = ',self.datawc_x2
        print 'datawc_y1 = ',self.datawc_y1
        print 'datawc_y2 = ',self.datawc_y2
        print 'markersizes = ',self.markersizes
        print 'markercolors = ',self.markercolors
        print 'markertypes = ',self.markertypes
        print 'markercolorsource = ',self.markercolorsource
        print 'markerpriority = ',self.markerpriority
        print 'clockwise = ',self.clockwise
        print 'theta_offset = ',self.theta_offset
        print 'theta_tick_count = ',self.theta_tick_count
        print 'magnitude_ticks = ',self.magnitude_ticks
        print 'magnitude_mintics = ',self.magnitude_mintics
        print 'magnitude_tick_angle = ',self.magnitude_tick_angle
        print 'negative_magnitude = ',self.negative_magnitude
        print 'group_names = ',self.group_names
        print 'connect_groups = ',self.connect_groups
        print 'linecolors = ',self.linecolors
        print 'linetypes = ',self.linetypes
        print 'linewidths = ',self.linewidths
        print 'linepriority = ',self.linepriority
        print 'xticlabels1 = ',self.xticlabels1
        print 'yticlabels1 = ',self.yticlabels1
        print 'colormap = ',self.colormap

    def create_text(self, tt, to):
        tc = vcs.createtext(Tt_source=tt, To_source=to)
        self.to_cleanup.append(tc.Tt)
        self.to_cleanup.append(tc.To)
        return tc

    def text_orientation_for_angle(self, theta, source="default"):
        """
        Generates a text orientation that will align text to look good depending on quadrant.
        """
        # Normalize to [0, 2*pi)
        while 0 > theta:
            theta += 2 * numpy.pi
        while 2 * numpy.pi <= theta:
            theta -= 2 * numpy.pi

        if 0 < theta < numpy.pi:
            valign = "bottom"
        elif 0 == theta or numpy.pi == theta:
            valign = "half"
        else:
            valign = "top"

        if numpy.pi / 2 > theta or numpy.pi * 3 / 2 < theta:
            halign = "left"
        elif numpy.allclose(numpy.pi / 2, theta) or numpy.allclose(numpy.pi * 3 / 2, theta):
            halign = "center"
        else:
            halign = "right"

        # Build new text table
        to = vcs.createtextorientation(source=source)
        to.valign = valign
        to.halign = halign
        self.to_cleanup.append(to)
        return to

    def magnitude_from_value(self, value, scale):
        below = None
        for ind, v in enumerate(scale):
            if v > value:
                break
            below = v
        else:
            return numpy.nan
        if below is None:
            return numpy.nan

        pct_between_levs = (value - below) / float(v - below)
        lower_lev_pos = (ind - 1) / float(len(scale) - 1)
        higher_lev_pos = ind / float(len(scale) - 1)
        return pct_between_levs * \
            (higher_lev_pos - lower_lev_pos) + lower_lev_pos

    def theta_from_value(self, value):
        if numpy.allclose((self.datawc_x1, self.datawc_x2), 1e20):
            # No scale specified, just use the value as theta
            if self.clockwise:
                return -(value + self.theta_offset)
            else:
                return value + self.theta_offset

        minval = self.datawc_x1
        maxval = self.datawc_x2
        offset = self.theta_offset / float(maxval - minval)

        pct_val = (value - minval) / float(maxval - minval) + offset
        rad_val = numpy.pi * 2 * pct_val
        if self.clockwise:
            # Reflect the value
            rad_val *= -1
        return rad_val

    def plot(self, var, theta=None, template=None, bg=0, x=None):
        """
        Plots a polar plot of your data.

        If var is an ndarray with the second dimension being 2, it will use the first value
        as magnitude and the second as theta.

        Otherwise, if theta is provided, it uses var as magnitude and the theta given.
        """
        if x is None:
            if self.x is None:
                self.x = vcs.init()
            x = self.x
        if template is None:
            template = self.template

        if self.markercolorsource.lower() not in ("group", "magnitude", "theta"):
            raise ValueError(
                "polar.markercolorsource must be one of: 'group', 'magnitude', 'theta'")

        magnitudes, thetas, names = convert_arrays(var, theta)
        if not self.negative_magnitude: # negative amplitude means 180 degree shift
            neg = numpy.ma.less(magnitudes,0.0)
            magnitudes = numpy.ma.abs(magnitudes)
            thetas = numpy.ma.where(neg,theta+numpy.pi,theta)
        if self.group_names:
            names = self.group_names
            while len(names) < len(magnitudes):
                names.append(None)

        flat_magnitude = numpy.ravel(magnitudes)
        flat_theta = numpy.ma.ravel(thetas)

        canvas = x
        # Determine aspect ratio for plotting the circle
        canvas_info = canvas.canvasinfo()
        # Calculate aspect ratio of window
        window_aspect = canvas_info["width"] / float(canvas_info["height"])
        if window_aspect > 1:
            ymul = window_aspect
            xmul = 1
        else:
            ymul = 1
            xmul = window_aspect
        # Use window_aspect to adjust size of template.data
        x0, x1 = template.data.x1, template.data.x2
        y0, y1 = template.data.y1, template.data.y2

        xdiff = abs(x1 - x0)
        ydiff = abs(y1 - y0)

        center = x0 + xdiff / 2., y0 + ydiff / 2.
        diameter = min(xdiff, ydiff)
        radius = diameter / 2.
        plot_kwargs = {"render": False, "bg": bg, "donotstoredisplay": True}
        # Outer line
        if template.box1.priority > 0:
            outer = vcs.createline(source=template.box1.line)
            x, y = circle_points(center, radius, ratio=window_aspect)
            outer.x = x
            outer.y = y
            canvas.plot(outer, **plot_kwargs)
            del vcs.elements["line"][outer.name]

        if numpy.allclose((self.datawc_y1, self.datawc_y2), 1e20):
            if self.magnitude_ticks == "*":
                m_scale = vcs.mkscale(*vcs.minmax(flat_magnitude))
            else:
                if isinstance(self.magnitude_ticks, (str, unicode)):
                    ticks = vcs.elements["list"][self.magnitude_ticks]
                else:
                    ticks = self.magnitude_ticks
                m_scale = ticks
        else:
            m_scale = vcs.mkscale(self.datawc_y1, self.datawc_y2)

        if template.ytic1.priority > 0:
            m_ticks = vcs.createline(source=template.ytic1.line)
            m_ticks.x = []
            m_ticks.y = []

            if template.ylabel1.priority > 0:
                to = self.text_orientation_for_angle(self.magnitude_tick_angle + self.theta_offset,
                                                     source=template.ylabel1.textorientation)
                m_labels = self.create_text(template.ylabel1.texttable, to)
                m_labels.x = []
                m_labels.y = []
                m_labels.string = []
                if self.yticlabels1 == "*":
                    mag_labels = vcs.mklabels(m_scale)
                else:
                    mag_labels = self.yticlabels1
            else:
                m_labels = None

            for lev in m_scale:
                lev_radius = radius * self.magnitude_from_value(lev, m_scale)
                x, y = circle_points(center, lev_radius, ratio=window_aspect)
                if m_labels is not None:
                    if lev in mag_labels:
                        m_labels.string.append(mag_labels[lev])
                        m_labels.x.append(
                            xmul *
                            lev_radius *
                            numpy.cos(
                                self.magnitude_tick_angle + self.theta_offset) +
                            center[0])
                        m_labels.y.append(
                            ymul *
                            lev_radius *
                            numpy.sin(
                                self.magnitude_tick_angle + self.theta_offset) +
                            center[1])
                m_ticks.x.append(x)
                m_ticks.y.append(y)
            canvas.plot(m_ticks, **plot_kwargs)
            del vcs.elements["line"][m_ticks.name]
            if m_labels is not None:
                canvas.plot(m_labels, **plot_kwargs)
                del vcs.elements["textcombined"][m_labels.name]

        if template.ymintic1.priority > 0 and self.magnitude_mintics is not None:
            mag_mintics = vcs.createline(source=template.ymintic1.line)
            mag_mintics.x = []
            mag_mintics.y = []

            mintics = self.magnitude_mintics
            if isinstance(mintics, (str, unicode)):
                mintics = vcs.elements["list"][mintics]

            for mag in mintics:
                mintic_radius = radius * \
                    self.magnitude_from_value(mag, m_scale)
                x, y = circle_points(
                    center, mintic_radius, ratio=window_aspect)
                mag_mintics.x.append(x)
                mag_mintics.y.append(y)
            canvas.plot(mag_mintics, **plot_kwargs)
            del vcs.elements["line"][mag_mintics.name]

        if self.xticlabels1 == "*":
            if numpy.allclose((self.datawc_x1, self.datawc_x2), 1e20):
                tick_thetas = list(numpy.arange(0, numpy.pi * 2, numpy.pi / 4))
                tick_labels = {t: str(t) for t in tick_thetas}
            else:
                d_theta = (self.datawc_x2 - self.datawc_x1) / \
                    float(self.theta_tick_count)
                tick_thetas = numpy.arange(
                    self.datawc_x1, self.datawc_x2 + .0001, d_theta)
                tick_labels = vcs.mklabels(tick_thetas)
        else:
            tick_thetas = self.xticlabels1.keys()
            tick_labels = self.xticlabels1

        if template.xtic1.priority > 0:
            t_ticks = vcs.createline(source=template.xtic1.line)
            t_ticks.x = []
            t_ticks.y = []

            if template.xlabel1.priority > 0:
                t_labels = []
                theta_labels = tick_labels
            else:
                t_labels = None

            for t in tick_thetas:
                angle = self.theta_from_value(t)
                x0 = center[0] + (xmul * radius * numpy.cos(angle))
                x1 = center[0]
                y0 = center[1] + (ymul * radius * numpy.sin(angle))
                y1 = center[1]
                if t_labels is not None:
                    label = self.create_text(template.xlabel1.texttable,
                            self.text_orientation_for_angle(angle,
                                source=template.xlabel1.textorientation))
                    label.string = [theta_labels[t]]
                    label.x = [x0]
                    label.y = [y0]
                    t_labels.append(label)
                t_ticks.x.append([x0, x1])
                t_ticks.y.append([y0, y1])
            canvas.plot(t_ticks, **plot_kwargs)
            del vcs.elements["line"][t_ticks.name]
            if t_labels is not None:
                for l in t_labels:
                    canvas.plot(l, **plot_kwargs)
                    del vcs.elements["textcombined"][l.name]

        values = vcs.createmarker()
        values.type = self.markertypes
        values.size = self.markersizes
        values.color = self.markercolors
        values.colormap = self.colormap
        values.priority = self.markerpriority
        values.x = []
        values.y = []

        if template.legend.priority > 0:
            # Only labels that are set will show up in the legend
            label_count = len(names) - len([i for i in names if i is None])
            labels = self.create_text(
                template.legend.texttable,
                template.legend.textorientation)
            labels.x = []
            labels.y = []
            labels.string = []

        if self.linepriority>0:
            line = vcs.createline()
            line.x = []
            line.y = []
            line.type = self.linetypes
            line.color = self.linecolors if self.linecolors is not None else self.markercolors
            line.width = self.linewidths
            line.priority = self.linepriority

            # This is up here because when it's part of the main loop, we can
            # lose "order" of points when we flatten them.
            for mag, theta in zip(magnitudes, thetas):
                x = []
                y = []

                for m, t in zip(mag, theta):
                    t = self.theta_from_value(t)
                    r = self.magnitude_from_value(m, m_scale) * radius
                    if r == numpy.nan:
                        continue
                    x.append(xmul * numpy.cos(t) * r + center[0])
                    y.append(ymul * numpy.sin(t) * r + center[1])

                if self.connect_groups:
                    line.x.extend(x)
                    line.y.extend(y)
                else:
                    line.x.append(x)
                    line.y.append(y)

        if self.markercolorsource.lower() in ('magnitude', "theta"):
            # Regroup the values using the appropriate metric

            mag_flat = numpy.array(magnitudes).flatten()
            theta_flat = numpy.array(thetas).flatten()

            if self.markercolorsource.lower() == "magnitude":
                scale = m_scale
                vals = mag_flat
            else:
                scale = theta_ticks
                vals = theta_flat

            indices = [numpy.where(numpy.logical_and(vals >= scale[i], vals <= scale[i + 1]))
                       for i in range(len(scale) - 1)]
            magnitudes = [mag_flat[inds] for inds in indices]
            thetas = [theta_flat[inds] for inds in indices]
            names = vcs.mklabels(scale, output="list")
            names = [names[i] + " - " + names[i + 1]
                     for i in range(len(names) - 1)]
            label_count = len(names)

        for mag, theta, name in zip(magnitudes, thetas, names):
            x = []
            y = []
            for m, t in zip(mag, theta):
                t = self.theta_from_value(t)
                r = self.magnitude_from_value(m, m_scale) * radius
                x.append(xmul * numpy.cos(t) * r + center[0])
                y.append(ymul * numpy.sin(t) * r + center[1])

            if template.legend.priority > 0 and name is not None:
                y_offset = len(labels.x) / float(label_count) * \
                    (template.legend.y2 - template.legend.y1)
                lx, ly = template.legend.x1, template.legend.y1 + y_offset
                x.append(lx)
                y.append(ly)
                labels.x.append(lx + .01)
                labels.y.append(ly)
                labels.string.append(str(name))
            values.x.append(x)
            values.y.append(y)

        if template.legend.priority > 0:
            canvas.plot(labels, **plot_kwargs)
            del vcs.elements["textcombined"][labels.name]
        if self.linepriority>0:
            canvas.plot(line, **plot_kwargs)
            del vcs.elements["line"][line.name]

        for el in self.to_cleanup:
            if vcs.istexttable(el):
                if el.name in vcs.elements["texttable"]:
                    del vcs.elements["texttable"][el.name]
            else:
                if el.name in vcs.elements["textorientation"]:
                    del vcs.elements["textorientation"][el.name]
        self.to_cleanup = []

        # Prune unneeded levels from values
        to_prune = []
        for ind, (x, y) in enumerate(zip(values.x, values.y)):
            if x and y:
                continue
            else:
                to_prune.append(ind)

        for prune_ind in to_prune[::-1]:
            del values.x[prune_ind]
            del values.y[prune_ind]
            if len(values.color) > prune_ind and len(values.color) > 1:
                del values.color[prune_ind]
            if len(values.size) > prune_ind and len(values.size) > 1:
                del values.size[prune_ind]
            if len(values.type) > prune_ind and len(values.type) > 1:
                del values.type[prune_ind]

        canvas.plot(values, bg=bg, donotstoredisplay=True)
        del vcs.elements["marker"][values.name]
        return canvas


def init_polar():
    # Create nice polar template
    try:
        t = vcs.createtemplate("polar_oned")
        t.data.x1 = .2
        t.data.x2 = .8
        t.data.y1 = .2
        t.data.y2 = .8

        t.legend.x1 = .85
        t.legend.x2 = 1
        t.legend.y1 = .15
        t.legend.y2 = .85

        dash = vcs.createline()
        dash.type = "dash"
        dot = vcs.createline()
        dot.type = "dot"
        t.xtic1.line = dash
        t.ytic1.line = dot

        left_aligned = vcs.createtextorientation()
        left_aligned.halign = "left"
        left_aligned.valign = "half"
        t.legend.textorientation = left_aligned
    except vcs.vcsError:
        # Template already exists
        pass
    # Create some nice default polar GMs
    degree_polar = Gpo("degrees", template="polar_oned")
    degree_polar.datawc_x1 = 0
    degree_polar.datawc_x2 = 360
    degree_polar.xticlabels1 = {
        i: str(i) for i in range(0, 360, 45)
    }

    clock_24 = Gpo("diurnal", template="polar_oned")
    clock_24.datawc_x1 = 0
    clock_24.datawc_x2 = 24
    clock_24.clockwise = True
    # 6 AM on the right
    clock_24.theta_offset = -6
    clock_24.xticlabels1 = {
        i: str(i) for i in range(0, 24, 3)
    }

    clock_24_meridiem = Gpo(
        "diurnal_12_hour",
        source="diurnal",
        template="polar_oned")
    clock_24_meridiem.xticlabels1 = {
        0: "12 AM",
        3: "3 AM",
        6: "6 AM",
        9: "9 AM",
        12: "12 PM",
        15: "3 PM",
        18: "6 PM",
        21: "9 PM"
    }

    clock_12 = Gpo("semidiurnal", source="diurnal", template="polar_oned")
    clock_12.datawc_x2 = 12
    clock_12.xticlabels1 = {
        i: str(i) for i in range(3, 13, 3)
    }
    # 3 on the right
    clock_12.theta_offset = -3

    annual_cycle = Gpo("annual_cycle", template="polar_oned")
    annual_cycle.datawc_x1 = 1
    annual_cycle.datawc_x2 = 13
    annual_cycle.clockwise = True
    annual_cycle.xticlabels1 = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    # Put December on the top
    annual_cycle.theta_offset = -2

    seasonal = Gpo("seasonal", template="polar_oned")
    seasonal.datawc_x1 = 0
    seasonal.datawc_x2 = 4
    seasonal.xticlabels1 = {0: "DJF", 1: "MAM", 2: "JJA", 3: "SON"}
    seasonal.clockwise = True
    # DJF on top
    seasonal.theta_offset = -1
