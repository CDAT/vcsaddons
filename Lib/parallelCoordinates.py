import vcs
import numpy
import vcsaddons


class Gpc(vcsaddons.core.VCSaddon):

    def __init__(self, name, source="default", x=None, template=None):
        self.g_name = 'Gpc'
        self.g_type = 'parallelcoordinates'
        super(Gpc, self).__init__(name, source, x, template)
        if source == "default":
            self.datawc_y1 = [1.e20]
            self.datawc_y2 = [1.e20]
            self.markercolors = None
            self.markertypes = ["dot"]
            self.markersizes = [2.]
            self.linecolors = None
            self.linetypes = ["solid"]
            self.linewidths = [1]
            self.yticlabels = ["*"]
            # self.ymtics = [""]
            del(self.yticlabels1)
            del(self.ymtics1)
            del(self.yticlabels2)
            del(self.ymtics2)
        else:
            if isinstance(source, (str, unicode)):
                gm = vcsaddons.gms[self.g_type][source]
            else:
                gm = source
            self.datawc_y1 = gm.datawc_y1
            self.datawc_y2 = gm.datawc_y2
            self.markercolors = gm.markercolors
            self.markertypes = gm.markertypes
            self.markersizes = gm.markersizes
            self.linecolors = gm.linecolors
            self.linetypes = gm.linetypes
            self.linewidths = gm.linewidths
            self.yticlabels = gm.yticlabels

    def list(self):
        print 'graphics method = ', self.g_name
        print 'name = ', self.name
        print 'datawc_x1 = ', self.datawc_x1
        print 'datawc_x2 = ', self.datawc_x2
        print 'datawc_y1 = ', self.datawc_y1
        print 'datawc_y2 = ', self.datawc_y2
        print 'xmtics1 = ', self.xmtics1
        print 'xmtics2 = ', self.xmtics2
        print 'ymtics = ', self.ymtics
        print 'xticlabels1 = ', self.xticlabels1
        print 'xticlabels2 = ', self.xticlabels2
        print 'yticlabels = ', self.yticlabels
        print 'xaxisconvert = ', self.xaxisconvert
        print 'yaxisconvert = ', self.yaxisconvert

    def drawYAxes(self, mins, maxs, labels, template, X, bg):
        N = len(labels)
        l = X.createline(source=template.xtic1.line)
        l.viewport = [template.data.x1, template.data.x2,
                      template.data.y1, template.data.y2]
        ys = [[0, 1]] * N
        xs = [[x / (N - 1.), x / (N - 1.)] for x in range(N)]

        l.x = xs
        l.y = ys
        l.priority = template.xtic1.priority
        X.plot(l, bg=bg, render=False)

        l = X.createline(source=template.box1.line)
        l.viewport = [template.data.x1, template.data.x2,
                      template.data.y1, template.data.y2]
        l.x = [[0, 1, 1, 0, 0]]
        l.y = [[0, 0, 1, 1, 0]]
        l.priority = template.box1.priority
        X.plot(l, bg=bg, render=False)

        l1 = X.createline(source=template.ytic1.line)
        l2 = X.createline(source=template.ytic2.line)
        le1 = X.createline(source=template.ytic1.line)
        le2 = X.createline(source=template.ytic2.line)
        txt = X.createtext(To_source=template.ylabel1.textorientation,
                           Tt_source=template.ylabel1.texttable)
        txt.priority = template.ylabel1.priority
        l1.priority = template.ytic1.priority
        l2.priority = template.ytic2.priority
        le1.priority = template.ytic1.priority
        le2.priority = template.ytic2.priority
        if 0 < txt.priority >= template.data.priority:
            txt.priority += 1
        xs1 = []
        xs2 = []
        xe1 = []
        xe2 = []
        ye1 = []
        ye2 = []
        ys = []
        xt = []
        yt = []
        st = []
        for i, lbl in enumerate(labels):
            x = float(i) / (N - 1)
            for y in lbl:
                st.append(lbl[y])
                Y = (y - mins[i]) / (maxs[i] - mins[i])
                ys.append([Y, Y])
                yt.append(Y)
                d1 = abs(template.ytic1.x2 - template.ytic1.x1)
                mn = min(template.data.x1, template.data.x2)
                dt = mn - template.ylabel1.x
                xs1.append([x - d1, x])
                xt.append(x - dt)
                if i == 0:
                    xe1.append([template.data.x1 - d1, template.data.x1])
                    ye1.append([Y, Y])
                elif i == N - 1:
                    xe2.append([template.data.x2 + d1, template.data.x2])
                    ye2.append([Y, Y])
                d2 = abs(template.ytic2.x2 - template.ytic2.x1)
                xs2.append([x + d2, x])
        l1.viewport = l.viewport
        l2.viewport = l.viewport
        le1.viewport = [0, 1, template.data.y1, template.data.y2]
        le2.viewport = [0, 1, template.data.y1, template.data.y2]
        txt.viewport = l.viewport
        l1.x = xs1
        l1.y = ys
        l2.x = xs2
        l2.y = ys
        le1.x = xe1
        le1.y = ye1
        le2.x = xe2
        le2.y = ye2
        txt.x = xt
        txt.y = yt
        txt.string = st
        X.plot(l1, bg=bg, render=False)
        X.plot(l2, bg=bg, render=False)
        X.plot(le1, bg=bg, render=False)
        X.plot(le2, bg=bg, render=False)
        X.plot(txt, bg=bg, render=False)

    def plot(self, array, template=None, bg=False, render=True, x=None):
        """Parallel Coordinates plot array must be of shape:
        (...,Dim1,Nlines)
        """
        if not array.ndim > 1:
            raise Exception("Array must be at least 2D")
        nlines = array.shape[-1]
        length = array.shape[-2]

        # Pad attributes related to Y axis
        for att in ["datawc_y1", "datawc_y2",
                    "yticlabels"]:
            # prepare local lists
            exec("%s = list(self.%s)" % (att, att))
            exec("while len(%s) < length: %s+=[%s[-1]]" % (att, att, att))

        data = array.asma()
        maxs = numpy.ma.max(data, axis=-1)
        mins = numpy.ma.min(data, axis=-1)

        if template is not None:
            t = vcs.createtemplate(source=template)
        else:
            t = vcs.createtemplate(source=self.template)

        for i in range(length):
            levels = vcs.mkscale(mins[i], maxs[i])
            # Do we need to create our range
            if numpy.allclose(datawc_y1[i], 1.e20):  # noqa
                datawc_y1[i] = levels[0]  # noqa
                datawc_y2[i] = levels[-1]  # noqa
            maxs[i] = datawc_y2[i]  # noqa
            mins[i] = datawc_y1[i]  # noqa

            # Do we have tics?
            if yticlabels[i] == "*":  # noqa
                yticlabels[i] = vcs.mklabels(levels)  # noqa
        if x is None:
            x = self.x
        self.drawYAxes(mins, maxs, yticlabels, t, x, bg)  # noqa
        ax = array.getAxis(-2)
        deflbls = {}
        for i in range(length):
            deflbls[float(i) / (length - 1)] = str(ax[i])
            if hasattr(ax, "units") and isinstance(ax.units, (list, tuple)):
                deflbls[float(i) / (length - 1)] += " (%s)" % ax.units[i]
        if self.xticlabels1 == "*":
            lbls1 = deflbls
        else:
            lbls1 = self.xticlabels1
        if self.xmtics1 == "":
            lbls1m = deflbls
        else:
            lbls1m = self.xmtics1
        if self.xticlabels2 == "*":
            lbls2 = deflbls
        else:
            lbls2 = self.xticlabels2
        if self.xmtics2 == "":
            lbls2m = deflbls
        else:
            lbls2m = self.xmtics2

        for l, lbls in enumerate([lbls1, lbls1m, lbls2, lbls2m]):
            ln = x.createline(source=t.xtic1.line)
            xs = []
            ys = []
            if l % 2 == 0:
                if l == 0:
                    txt = x.createtext(To_source=t.xlabel1.textorientation,
                                       Tt_source=t.xlabel1.texttable)
                else:
                    txt = x.createtext(To_source=t.xlabel2.textorientation,
                                       Tt_source=t.xlabel2.texttable)
                txs = []
                tys = []
                ts = []
            for loc in lbls:
                xs.append([loc, loc])
                if l == 0:
                    ys.append([t.xtic1.y1, t.xtic1.y2])
                    txs.append(loc)
                    tys.append(t.xlabel1.y)
                    ts.append(lbls[loc])
                    ln.priority = t.xtic1.priority
                    txt.priority = t.xlabel1.priority
                elif l == 1:
                    ys.append([t.xmintic1.y1, t.xmintic1.y2])
                    ln.priority = t.xmintic1.priority
                elif l == 2:
                    ys.append([t.xtic2.y1, t.xtic2.y2])
                    txs.append(loc)
                    tys.append(t.xlabel2.y)
                    ts.append(lbls[loc])
                    ln.priority = t.xtic2.priority
                    txt.priority = t.xlabel2.priority
                elif l == 3:
                    ys.append([t.xmintic2.y1, t.xmintic2.y2])
                    ln.priority = t.xmintic2.priority
            ln.x = xs
            ln.y = ys
            ln.viewport = [t.data.x1, t.data.x2, 0, 1]
            x.plot(ln, bg=bg, render=False)
            if l % 2 == 0:  # text on
                txt.viewport = ln.viewport
                txt.x = txs
                txt.y = tys
                txt.string = ts
                x.plot(txt, bg=bg, render=False)

        # Normalizes
        deltas = maxs - mins
        data = (data - mins[:, numpy.newaxis]) / deltas[:, numpy.newaxis]

        # Pad attributes related to number of lines
        lineAtts = ["linetypes", "linewidths",
                    "markertypes", "markersizes"]
        if self.markercolors is not None:
            lineAtts.append("markercolors")
        if self.linecolors is not None:
            lineAtts.append("linecolors")
        for att in lineAtts:
            # prepare local lists
            exec("%s = list(self.%s)" % (att, att))
            exec("while len(%s) < nlines: %s+=[%s[-1]]" % (att, att, att))

        if self.linecolors is None:
            linecolors = vcs.getcolors(range(nlines + 1))
        if self.markercolors is None:
            markercolors = vcs.getcolors(range(nlines + 1))

        # Mark fully missing models
        scratched = []
        for i in range(nlines):
            if data[:, i].count() > 0:
                scratched.append(False)
            else:
                scratched.append(True)
        # Now draws the legend
        t.drawLinesAndMarkersLegend(x,
                                    linecolors, linetypes, linewidths,  # noqa
                                    markercolors, markertypes, markersizes,  # noqa
                                    [str(v) for v in array.getAxis(-1)],
                                    bg=bg, render=False, scratched=scratched)

        lst = ["max", "min", "mean"]
        t.blank(lst)
        t.drawAttributes(x, array, self, bg=bg)
        t.blank()
        t.data.priority = 1

        for i in range(nlines):
            if data[:, i].count() > 0:
                l = vcs.create1d()
                l.colormap = self.colormap
                l.linecolor = linecolors[i]
                l.linewidth = linewidths[i]  # noqa
                l.linetype = linetypes[i]  # noqa
                l.marker = markertypes[i]  # noqa
                l.markercolor = markercolors[i]
                l.markersize = markersizes[i]  # noqa
                l.datawc_y1 = 0.
                l.datawc_y2 = 1.
                if i < nlines - 1:
                    x.plot(data[:, i], t, l, bg=bg, render=False)
                else:
                    x.plot(data[:, i], t, l, bg=bg, render=render)
