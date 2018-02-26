import vcs
from . import EzTemplateSrc as EzTemplate
import random


class EzLinePlot(object):
    """
    ##
    """
    __default_linecolors = [[12.2, 46.7, 70.6], [100.0, 49.8, 5.5],
                            [17.25, 62.75, 17.25], [83.92, 15.29, 15.69],
                            [58.04, 40.39, 74.12], [54.9, 33.73, 29.41],
                            [89.01960784313725, 46.666666666666664, 76.07843137254902],
                            [49.80392156862745, 49.80392156862745, 49.80392156862745],
                            [73.72549019607844, 74.11764705882354,
                                13.333333333333334],
                            [9.019607843137255, 74.50980392156863, 81.17647058823529],
                            [68.23529411764706, 78.03921568627452, 90.98039215686275],
                            [100.0, 73.33333333333333, 47.05882352941176],
                            [59.6078431372549, 87.45098039215686, 54.11764705882353],
                            [100.0, 59.6078431372549, 58.82352941176471],
                            [77.25490196078432, 69.01960784313725, 83.52941176470588],
                            [76.86274509803923, 61.1764705882353, 58.03921568627452],
                            [96.86274509803921, 71.37254901960785, 82.35294117647058],
                            [78.03921568627452, 78.03921568627452, 78.03921568627452],
                            [85.88235294117646, 85.88235294117646,
                                55.294117647058826],
                            [61.96078431372549, 85.49019607843137, 89.80392156862746]]

    __range_increase = 0.05

    __default_grid_color = [(50, 50, 50, 50)]

    def __init__(self, rangeincrease=None, defaultgridcolor=None,
                 defaultlinecolors=None):
        """
        """
        if rangeincrease is not None:
            self.__range_increase = rangeincrease

        if defaultlinecolors is not None:
            self.__default_linecolors = defaultlinecolors

        if defaultgridcolor is not None:
            self.__default_grid_color = defaultgridcolor

    def list(self):
        print(self)
        return

    def __str__(self):
        st = '---------- EzPlot (attribute) listings ----------'
        st += ' '
        return st

    def __get_color_by_index(self, index):
        cs = len(self.__default_linecolors)
        return self.__default_linecolors[index if index < cs else int(
            float(index % cs))]

    def __check_values(self, data, canvas, template,
                       line, linetypes, linewidths, linecolors,
                       backgroundcolor, colormap, randomcolor,
                       title, titlesize, left_label, right_label, bottom_label, top_label,
                       verticallabelsize, horizontallabelsize,
                       marker, markercolors, markertypes, markersizes,
                       legendtexts, legendscratched, legendtextcolors, legendposition,
                       legendstacking, legenddrawbackground, legendbackgroundcolor,
                       legendsmallestfontsize, tick_sides, framewidth,
                       autoxaxis, autoyaxis, min_y, max_y, min_x, max_x, x_labels, y_labels,
                       enablegrid):

        dimensionality = 0
        if data is None or not isinstance(data, list):
            raise ValueError(
                'No data provided to be plotted or data is not in a list object.')
        else:
            dimensionality = len(data)

        if canvas is None or not isinstance(canvas, vcs.Canvas.Canvas):
            raise ValueError('No VCS canvas provided.')

        if isinstance(template, str):
            template = vcs.gettemplate(template)

        if backgroundcolor is not None and isinstance(
                backgroundcolor, list) is False:
            raise ValueError('backgroundcolor must be a valid VCS color.')

        if colormap is not None and isinstance(
                colormap, vcs.colormap.Cp) is False:
            raise ValueError(
                'colormap must be a valid VCS vcs.colormap.Cp object.')

        if randomcolor is not None and isinstance(randomcolor, bool) is False:
            raise ValueError('randomcolor must be a valid boolean value.')

        if legendsmallestfontsize is not None and isinstance(
                legendsmallestfontsize, float) is False:
            raise ValueError('legendsmallestfontsize must be a valid number.')

        if tick_sides is not None and isinstance(tick_sides, list) is False:
            raise ValueError(
                'tick_sides must be a valid list of "left" or "right" values.')

        if framewidth is not None and isinstance(framewidth, int) is False:
            raise ValueError('framewidth must be a valid integer value.')

        if autoxaxis is not None and isinstance(autoxaxis, bool) is False:
            raise ValueError('autoxaxis must be a valid boolean value.')

        if autoyaxis is not None and isinstance(autoyaxis, bool) is False:
            raise ValueError('autoyaxis must be a valid boolean value.')

        if min_y is not None and isinstance(min_y, float) is False:
            raise ValueError('min_y must be a valid float value.')

        if max_y is not None and isinstance(max_y, float) is False:
            raise ValueError('max_y must be a valid float value.')

        if min_x is not None and isinstance(min_x, float) is False:
            raise ValueError('min_x must be a valid float value.')

        if max_x is not None and isinstance(max_x, float) is False:
            raise ValueError('max_x must be a valid float value.')

        if x_labels != "*":
            if x_labels is not None and isinstance(x_labels, dict) is False:
                raise ValueError('x_labels must be a valid dictionary.')
        if y_labels != "*":
            if y_labels is not None and isinstance(y_labels, dict) is False:
                raise ValueError('y_labels must be a valid dictionary.')

        if title is not None:
            if isinstance(title, str) is False and isinstance(
                    title, vcs.textcombined.Tc) is False:
                raise ValueError(
                    'title must be an object name (str) or a VCS text.')

        if titlesize is not None:
            if isinstance(titlesize, int) is False:
                raise ValueError(
                    'titlesize must be an integer representing the font size.')

        if marker is not None:
            if isinstance(marker, str) is False and isinstance(
                    marker, vcs.marker.Tm) is False:
                raise ValueError(
                    'marker must be an object name (str) or a VCS marker.')

        if left_label is not None and isinstance(left_label, str) is False:
            raise ValueError(
                'left_label must be an object name (str) or None.')

        if right_label is not None and isinstance(right_label, str) is False:
            raise ValueError(
                'right_label must be an object name (str) or None.')

        if bottom_label is not None and isinstance(bottom_label, str) is False:
            raise ValueError(
                'bottom_label must be an object name (str) or None.')

        if top_label is not None and isinstance(top_label, str) is False:
            raise ValueError('top_label must be an object name (str) or None.')

        if legendstacking is not None and isinstance(
                legendstacking, str) is False:
            raise ValueError('legendstacking must be an object name (str).')
        else:
            if legendstacking != "horizontal" and legendstacking != "vertical":
                raise ValueError(
                    'legendstacking must be "horizontal" or "vertical".')

        if legenddrawbackground is not None and isinstance(
                legenddrawbackground, bool) is False:
            raise ValueError('legenddrawbackground must be a boolean or None.')

        if legendbackgroundcolor is not None and isinstance(
                legendbackgroundcolor, str) is False:
            raise ValueError(
                'legenddrawbackground must be a valid VCS color name (str).')

        if line is not None and isinstance(line, str) is False:
            raise ValueError('line must be an object name (str) or None.')

        if linetypes is not None:
            if len(linetypes) != dimensionality:
                raise ValueError(
                    'linetypes must have the same dimension as the data parameter.')

        if linewidths is not None:
            if len(linewidths) != dimensionality:
                raise ValueError(
                    'linewidths must have the same dimension as the data parameter.')

        if linecolors is not None:
            if len(linecolors) != dimensionality:
                raise ValueError(
                    'linecolors must have the same dimension as the data parameter.')

        if markercolors is not None:
            if len(markercolors) != dimensionality:
                raise ValueError(
                    'markercolors must have the same dimension as the data parameter.')

        if markertypes is not None:
            if len(markertypes) != dimensionality:
                raise ValueError(
                    'markertypes must have the same dimension as the data parameter.')

        if markersizes is not None:
            if len(markersizes) != dimensionality:
                raise ValueError(
                    'markersizes must have the same dimension as the data parameter.')

        if legendtexts is not None:
            if len(legendtexts) != dimensionality:
                raise ValueError(
                    'legendtexts must have the same dimension as the data parameter.')

        if legendtextcolors is not None:
            if len(legendtextcolors) != dimensionality:
                raise ValueError(
                    'legendtextcolors must have the same dimension as the data parameter.')

        if legendposition is not None:
            if isinstance(legendposition, list) is False and len(
                    legendposition) != 4:
                raise ValueError(
                    'legendposition must be a list of 4 float values.')

        if verticallabelsize is not None:
            if isinstance(verticallabelsize, int) is False:
                raise ValueError(
                    'verticallabelsize must be an integer with the font size.')

        if horizontallabelsize is not None:
            if isinstance(horizontallabelsize, int) is False:
                raise ValueError(
                    'horizontallabelsize must be an integer with the font size.')

    def __calculate_new_range_y(
            self, data, y_labels, tick_sides, min_vals, max_vals):
        # Beautiful plots are not packed. Lets increase the
        # data range in Y axis
        if y_labels != "*" and isinstance(y_labels, dict):
            for i, var in enumerate(data):
                tmp_y_min = min(y_labels.keys())
                tmp_y_max = max(y_labels.keys())
                min_y = min_vals[tick_sides[i]]
                max_y = max_vals[tick_sides[i]]
                if min_y is None or min_y > tmp_y_min:
                    min_vals[tick_sides[i]] = tmp_y_min - \
                        (tmp_y_max - tmp_y_min) * self.__range_increase
                if max_y is None or max_y < tmp_y_max:
                    max_vals[tick_sides[i]] = tmp_y_max + \
                        (tmp_y_max - tmp_y_min) * self.__range_increase
        else:
            for i, var in enumerate(data):
                tmp_y_min = min(var)
                tmp_y_max = max(var)
                min_y = min_vals[tick_sides[i]]
                max_y = max_vals[tick_sides[i]]
                if min_y is None or min_y > tmp_y_min:
                    min_vals[tick_sides[i]] = tmp_y_min - \
                        (tmp_y_max - tmp_y_min) * self.__range_increase
                if max_y is None or max_y < tmp_y_max:
                    max_vals[tick_sides[i]] = tmp_y_max + \
                        (tmp_y_max - tmp_y_min) * self.__range_increase
        return min_vals, max_vals

    def __calculate_new_range_x(
            self, data, x_labels, tick_sides2, min_vals2, max_vals2):
        # Beautiful plots are not packed. Lets increase the
        # data range in X axis
        if x_labels != "*" and isinstance(x_labels, dict):
            for i, var in enumerate(data):
                tmp_x_min = min(x_labels.keys())
                tmp_x_max = max(x_labels.keys())
                min_x = min_vals2[tick_sides2[i]]
                max_x = max_vals2[tick_sides2[i]]
                if min_x is None or min_x > tmp_x_min:
                    min_vals2[tick_sides2[i]] = tmp_x_min - \
                        (tmp_x_max - tmp_x_min) * self.__range_increase
                if max_x is None or max_x < tmp_x_max:
                    max_vals2[tick_sides2[i]] = tmp_x_max + \
                        (tmp_x_max - tmp_x_min) * self.__range_increase
        else:
            for i, var in enumerate(data):
                tmp_x_min = 0
                tmp_x_max = len(var)
                if hasattr(var, 'getTime'):
                    tmp_x_min = min(var.getTime())
                    tmp_x_max = max(var.getTime())
                min_x = min_vals2[tick_sides2[i]]
                max_x = max_vals2[tick_sides2[i]]
                if min_x is None or min_x > tmp_x_min:
                    min_vals2[tick_sides2[i]] = tmp_x_min - \
                        (tmp_x_max - tmp_x_min) * self.__range_increase
                if max_x is None or max_x < tmp_x_max:
                    max_vals2[tick_sides2[i]] = (
                        tmp_x_max - 1) + (tmp_x_max - tmp_x_min) * self.__range_increase
        return min_vals2, max_vals2

    def lineplot(self, data=None, canvas=None, template=None, line=None,
                 linetypes=None, linewidths=None, linecolors=None,
                 backgroundcolor=None, colormap=None, randomcolor=False,
                 title=None, titlesize=None, left_label=None, right_label=None, bottom_label=None, top_label=None,
                 verticallabelsize=None, horizontallabelsize=None,
                 marker=None, markercolors=None, markertypes=None, markersizes=None,
                 legendtexts=None, legendscratched=None, legendtextcolors=None, legendposition=None,
                 legendstacking="horizontal", legenddrawbackground=False, legendbackgroundcolor=None,
                 legendsmallestfontsize=None, tick_sides=None, framewidth=None,
                 autoxaxis=True, autoyaxis=True, min_y=None, max_y=None, min_x=None, max_x=None,
                 x_labels="*", y_labels="*",
                 enablegrid=False):
        """
        This file is ready to be imported by your scripts, and you can just call this function.

        Sample usage is below.

        data: List of variables to plot
        canvas: VCS canvas
        template: The template to use as the base for the plot.
        line: A line object or name of a line object used to describe the lines plotted. Set to None to hide.
        linetypes: List of VCS valid line types. Ex. solid, dash, etc. Set to None to hide.
        linewidths: List of line widths. Set to None to hide.
        linecolors: List of line colors. Set to None to hide.
        backgroundcolor: Canvas background color. Set to None to hide.
        colormap: A valid VCS colormap. Set to None to hide.
        randomcolor: Set the line colors in a random way.
        title: A VCS text type or a string text for the plot title. Set to None to hide.
        titlesize: If title is only a str, titlesize is used to define the font size for the title text.
        left_label: Text to put on the left Y axis.
        right_label: Text to put on the right Y axis.
        bottom_label: Text to put on the bottom.
        top_label: Text to put on the top.
        marker: A marker object or name of a marker object used to describe the markers plotted. Set to None to hide.
        markercolors: A list of valid VCS colors. Set to None to hide.
        markertypes: A list of valid VCS marker types. Ex: dot, None, etc. Set to None to hide.
        markersizes: A list of valid marker sizes. Ex: [4, 3, 1]. Set to None to hide.
        legendtexts: List of strings with for the legend texts. Set to None to hide.
        legendscratched:
        legendtextcolors: List of valid VCS colors for the legend texts. Ex. ["black", "yellow"].
        legendposition: List of 4 values"[x1, x2, y1, y2]. Set to None to hide.
        legendstacking: Set to "horizontal" or "vertical"
        legenddrawbackground: Boolean enabling/disabling background rendering. Set to None to hide.
        legendbackgroundcolor: A valid VCS color for the legend box background. Set to None to hide.
        legendsmallestfontsize: Minimal value for the legend font size.
        tick_sides: A list of "left" or "right" values indicating which side of the chart you want the variable axes
                    to be displayed.
        framewidth: The width of the frames lines.
        autoxaxis: Boolean enabling/disabling auto range for the X axis. Enabled by default.
        autoyaxis: Boolean enabling/disabling auto range for the Y axis. Enabled by default.
        min_y: If you want to adjust the y axis bounds, you can set a minimum value.
               Will be derived from data if not specified.
        max_y: If you want to adjust the y axis bounds, you can set a maximum value.
               Will be derived from data if not specified.
        min_x: If you want to adjust the x axis bounds, you can set a minimum value.
               Will be derived from data if not specified.
        max_x: If you want to adjust the x axis bounds, you can set a maximum value.
               Will be derived from data if not specified.
        x_labels: Dictionary for setting axis tick labels
        y_labels: Dictionary for setting axis tick labels
        horizontallabelsize: Font size for the x labels.
        verticallabelsize:  Font size for the y labels.
        enablegrid: Boolean enabling/disabling the grid rendering.
        """

        self.__check_values(data, canvas, template,
                            line, linetypes, linewidths, linecolors,
                            backgroundcolor, colormap, randomcolor,
                            title, titlesize, left_label, right_label, bottom_label, top_label,
                            verticallabelsize, horizontallabelsize,
                            marker, markercolors, markertypes, markersizes,
                            legendtexts, legendscratched, legendtextcolors, legendposition,
                            legendstacking, legenddrawbackground, legendbackgroundcolor,
                            legendsmallestfontsize, tick_sides, framewidth,
                            autoxaxis, autoyaxis, min_y, max_y, min_x, max_x, x_labels, y_labels,
                            enablegrid)

        if template is None:
            # Creates a default template for 1D plots
            template = vcs.createtemplate()
            template.move(.02, "x")
            template.yname.x = .01
            template.data.y1 = .1
            template.box1.y1 = .1
            ticlen = template.xtic1.y2 - template.xtic1.y1
            template.xtic1.y1 = template.data.y1
            template.xtic1.y2 = template.xtic1.y1 + ticlen
            template.xtic2.priority = 0
            template.xlabel1.y = template.xtic1.y2 - .01
            template.legend.x1 = template.data.x2 + (1 - template.data.x2) / 3.
            template.legend.x2 = .95
            template.legend.y1 = template.data.y1
            template.legend.y2 = template.data.y2
            template.yname.y = (template.data.y1 + template.data.y2) / 2.
            template.xname.y = template.xlabel1.y - .05

            # Standard practice for beautiful plots:
            template.blank(
                ["dataname", "legend", "mean", "min", "max", "source"])

            # legend position
            if legendposition is None:
                template.legend.x1 = .15
                template.legend.x2 = .25
                template.legend.y1 = .68
                template.legend.y2 = .78
            else:
                template.legend.x1 = legendposition[0]
                template.legend.x2 = legendposition[1]
                template.legend.y1 = legendposition[2]
                template.legend.y2 = legendposition[3]

            # Frame lines
            lineT = vcs.createline()
            if framewidth is None:
                lineT.width = 3
            else:
                lineT = framewidth
            template.box1.line = lineT
            template.xtic1.line = lineT
            # template.xtic2.line = lineT
            template.ytic1.line = lineT
            # template.ytic2.line = lineT

        # The labels don't make any sense with multiple values; hide them.
        template.min.priority = 0
        template.max.priority = 0
        template.mean.priority = 0
        template.dataname.priority = 0

        # Creates the base template
        templates = EzTemplate.oneD(len(data), template=template)
        templates.x = canvas
        # Creates the legend's template
        legendTemplate = vcs.createtemplate(source=template.name)
        legendTemplate.legend.priority = 1

        # Frame lines
        lineT = vcs.createline()
        if framewidth is None:
            lineT.width = 3
        else:
            lineT = framewidth
        legendTemplate.box1.line = lineT

        # Colormap
        if colormap is not None:
            templates.x.setcolormap(colormap)

        # Plot line colors
        lcolors = []
        if randomcolor is True:
            for c in range(len(data)):
                lcolors.append(colormap.getcolorcell(random.randint(0, 254)))
        elif linecolors is None:
            for c in range(len(data)):
                lcolors.append(self.__get_color_by_index(c))
        else:
            lcolors = linecolors

        # Plot line types
        ltypes = None
        if linetypes is None:
            if linecolors is not None:
                ltypes = []
                for i in range(len(data)):
                    ltypes.append('solid')
            else:
                ltypes = ['solid']
        else:
            ltypes = linetypes

        # Plot line widths
        lwidths = None
        if linewidths is None:
            lwidths = []
            for i in range(len(data)):
                lwidths.append(4)
        else:
            lwidths = linewidths

        # Plot marker colors
        mcolors = None
        if markercolors is None:
            mcolors = []
            for i in range(len(data)):
                mcolors.append(lcolors[i])
        else:
            mcolors = markercolors

        # Plot marker types
        mtypes = None
        if markertypes is None:
            mtypes = []
            for i in range(len(data)):
                mtypes.append(None)
        else:
            mtypes = markertypes

        # Plot marker sizes
        msizes = None
        if markersizes is None:
            msizes = []
            for i in range(len(data)):
                msizes.append(0)
        else:
            msizes = markersizes

        # Plot legend texts
        ltexts = None
        if legendtexts is None:
            ltexts = []
            for i in range(len(data)):
                ltexts.append('Plot line ' + str(i))
        else:
            ltexts = legendtexts

        # Plot legend text colors
        legcolors = None
        if legendtextcolors is None:
            legcolors = []
            for i in range(len(lcolors)):
                legcolors.append(lcolors[i])
        else:
            legcolors = legendtextcolors

        # Set the default font for the legend's texts
        if templates.x.getfontname(1) is not "DejaVuSans":
            try:
                templates.x.switchfonts("default", "DejaVuSans")
            except vcs.error.vcsError:
                print
                "\nError loading DejaVuSans font."

        # If not defined, lets show the ticks in the left side of the plot
        if tick_sides is None:
            tick_sides = ["left"] * len(data)

        clean_ticks = []
        for t in tick_sides:
            if t.lower() not in ('left', 'right'):
                raise ValueError(
                    "tick_sides must be a list of 'left' or 'right' values; found '%s'." %
                    t)
            clean_ticks.append(t.lower())

        tick_sides = clean_ticks
        if len(tick_sides) < len(data):
            tick_sides += tick_sides[-1:] * len(data)

        # Store min/max Y's per side for appropriate scaling
        min_vals = {"left": min_y, "right": min_y}
        max_vals = {"left": max_y, "right": max_y}

        # Beautiful plots are not packed. Lets increase the
        # data range in Y axis
        if autoyaxis is True:
            min_vals, max_vals = self.__calculate_new_range_y(data, y_labels,
                                                              tick_sides, min_vals, max_vals)

        # If not defined, lets show ticks in bottom side of the plot
        tick_sides2 = ["bottom"] * len(data)
        clean_ticks2 = []
        for t in tick_sides2:
            if t.lower() not in ('bottom', 'top'):
                raise ValueError(
                    "tick_sides must be a list of 'bottom' or 'top' values; found '%s'." %
                    t)
            clean_ticks2.append(t.lower())

        tick_sides2 = clean_ticks2
        if len(tick_sides2) < len(data):
            tick_sides2 += tick_sides2[-1:] * len(data)

        # Store min/max X's per side for appropriate scaling
        min_vals2 = {"bottom": min_x, "top": min_x}
        max_vals2 = {"bottom": max_x, "top": max_x}

        # Beautiful plots are not packed. Lets increase the
        # data range in X axis
        if autoxaxis is True:
            min_vals2, max_vals2 = self.__calculate_new_range_x(data, x_labels,
                                                                tick_sides2, min_vals2, max_vals2)

        if isinstance(line, str):
            line = vcs.getline(line)

        if marker is not None and isinstance(marker, str):
            marker = vcs.getmarker(marker)

        if line is not None:
            widths = line.width
            styles = line.type
            colors = line.color
        else:
            widths = lwidths
            styles = ltypes
            colors = lcolors

        if marker is not None:
            markers = marker.type
            marker_colors = marker.color
            marker_sizes = marker.size

        # background color
        if backgroundcolor is not None:
            templates.x.backgroundcolor = backgroundcolor

        # Now we create the graphical method and update its
        # parameters based on user data
        for n in range(len(data)):
            gm = templates.x.create1d()

            # Lines
            gm.linetype = styles[n]
            gm.linewidth = widths[n]
            gm.linecolor = colors[n]

            if marker is not None:
                gm.marker = markers[n]
                gm.markersize = marker_sizes[n]
                gm.markercolor = marker_colors[n]
            else:
                gm.marker = None

            if autoyaxis is True:
                # Updates the data range in Y axis
                gm.datawc_y1 = min_vals[tick_sides[n]]
                gm.datawc_y2 = max_vals[tick_sides[n]]

            if autoxaxis is True:
                # Updates the data range in X axis
                gm.datawc_x1 = min_vals2[tick_sides2[n]]
                gm.datawc_x2 = max_vals2[tick_sides2[n]]

            templateT = templates.get(n)

            gm.xticlabels1 = x_labels

            if tick_sides[n] == "left":
                if tick_sides.index("left") == n:
                    templateT.ylabel1.priority = 1
                    if left_label is not None:
                        templateT.yname.priority = 0
                        left_text = vcs.createtext(Tt_source=templateT.yname.texttable,
                                                   To_source=templateT.yname.textorientation)
                        left_text.x = templateT.yname.x
                        left_text.y = templateT.yname.y
                        hgt = verticallabelsize if verticallabelsize is not None else left_text.height
                        left_text.height = hgt
                        left_text.string = [left_label]
                        templates.x.plot(left_text)
                else:
                    templateT.ylabel1.priority = 0
                    templateT.yname.priority = 0
                templateT.ylabel2.priority = 0
                gm.yticlabels1 = y_labels
                if not enablegrid:
                    gm.yticlabels2 = ""
            else:
                templateT.ylabel1.priority = 0
                if tick_sides.index("right") == n:
                    templateT.ylabel2.priority = 1
                    if right_label is not None:
                        right_text = vcs.createtext(Tt_source=templateT.yname.texttable,
                                                    To_source=templateT.yname.textorientation)
                        right_text.x = templateT.data.x2 + \
                            (templateT.data.x1 - templateT.yname.x)
                        right_text.y = templateT.yname.y
                        right_text.height = verticallabelsize if verticallabelsize is not None else right_text.height
                        right_text.string = [right_label]
                        templates.x.plot(right_text)
                else:
                    templateT.ylabel2.priority = 0
                if not enablegrid:
                    gm.yticlabels1 = ""
                gm.yticlabels2 = y_labels
            if n != 0:
                templateT.xlabel1.priority = 0
                templateT.xname.priority = 0

            if tick_sides2[n] == "bottom":
                # if tick_sides2.index("bottom") == n:
                if tick_sides2[n] == "bottom":
                    templateT.xlabel1.priority = 1
                    if bottom_label is not None:
                        templateT.xname.priority = 0
                        bottom_text = vcs.createtext(Tt_source=templateT.xname.texttable,
                                                     To_source=templateT.xname.textorientation)
                        bottom_text.x = templateT.xname.x
                        bottom_text.y = templateT.xname.y
                        hgt = horizontallabelsize if horizontallabelsize is not None else bottom_text.height
                        bottom_text.height = hgt
                        bottom_text.string = [bottom_label]
                        templates.x.plot(bottom_text)
                else:
                    templateT.xlabel1.priority = 0
                    templateT.xname.priority = 0
                templateT.xlabel2.priority = 0
                gm.xticlabels1 = x_labels
                if not enablegrid:
                    gm.xticlabels2 = ""
            else:
                templateT.xlabel1.priority = 0
                if tick_sides2.index("top") == n:
                    templateT.xlabel2.priority = 1
                    if top_label is not None:
                        top_label = vcs.createtext(Tt_source=templateT.xname.texttable,
                                                   To_source=templateT.xname.textorientation)
                        top_label.x = templateT.data.x2 + \
                            (templateT.data.x1 - templateT.yname.x)
                        top_label.y = templateT.yname.y2
                        top_label.height = horizontallabelsize if horizontallabelsize is not None else top_label.height
                        top_label.string = [top_label]
                        templates.x.plot(top_label)
                else:
                    templateT.xlabel2.priority = 0
                if not enablegrid:
                    gm.xticlabels1 = ""
                gm.xticlabels2 = x_labels
            if n != 0:
                templateT.ylabel1.priority = 0
                templateT.yname.priority = 0

            # Grids:
            if enablegrid is True:
                templateT.xtic2.priority = 1
                templateT.ytic2.priority = 1

                if tick_sides[n] == "left":
                    templateT.ytic2.x1 = templateT.data.x1
                    templateT.ytic2.x2 = templateT.data.x2
                    templateT.ytic1.x1 = templateT.data.x1
                else:
                    templateT.ytic1.x2 = templateT.data.x2
                if x_labels != "*" and isinstance(x_labels, dict):
                    gm.xticlabels2 = x_labels
                    templateT.xtic2.y1 = templateT.data.y1
                    templateT.xtic2.y2 = templateT.data.y2
                else:
                    if tick_sides2[n] == "bottom":
                        templateT.xtic2.y1 = templateT.data.y1
                        templateT.xtic2.y2 = templateT.data.y2
                    else:
                        templateT.xtic2.y1 = templateT.data.y2
                        templateT.xtic2.y2 = templateT.data.y1

                lineG = templates.x.createline()
                lineG.color = self.__default_grid_color
                templateT.ytic2.line = lineG
                templateT.xtic2.line = lineG

            display = templates.x.plot(data[n], gm, templateT, bg=True)

        # Build Legend
        legendTemplate.drawLinesAndMarkersLegend(canvas=templates.x, linecolors=lcolors,
                                                 linetypes=ltypes, linewidths=lwidths, markercolors=mcolors,
                                                 markertypes=mtypes, markersizes=msizes, strings=ltexts,
                                                 scratched=legendscratched, stringscolors=legcolors,
                                                 stacking=legendstacking, bg=legenddrawbackground, render=True,
                                                 smallestfontsize=legendsmallestfontsize,
                                                 backgroundcolor=legendbackgroundcolor)
        # Title:
        if title is not None:
            titleObj = None
            if isinstance(title, str) or isinstance(title, list):
                titleObj = vcs.createtext()
                titleObj.halign = "center"
                titleObj.valign = "top"
                titleObj.height = titlesize if titlesize is not None else 30
                titleObj.string = title
                titleObj.x = .5
                titleObj.y = .95
                titleObj.font = "DejaVuSans"
            elif isinstance(title, vcs.textcombined.Tc):
                titleObj = title

            if titleObj is not None:
                display = templates.x.plot(titleObj)

        return display
