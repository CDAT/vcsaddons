import vcs
import numpy

def drawLinesAndMarkersLegend(canvas, templateLegend,
        linecolors,linetypes,linewidths,
        markercolors,markertypes,markersizes,
        strings,bg,render=True):
        """Draws a legend with line/marker/text inside a template legend box
    Auto adjust text size to make it fit inside the box
    Auto arrange the elements to fill the box nicely
    :: Example ::

    import vcsaddons
    import vcs
    x = vcs.init()
    t = vcs.createtemplate()
    vcsaddons.utils.drawLinesAndMarkersLegend(x,t.legend,
          ["red","blue","green"], ["solid","dash","dot"],[1,4,8],
          ["blue","green","red"], ["cross","square","dot"],[3,4,5],
          ["sample A","type B","thing C"],True)
    x.png("sample")

    :param canvas: a VCS canvas object onto which to draw the legend
    :type canvas: vcs.Canvas.Canvas

    :param templateLegend: a template legend object (template.legend), used to determine the coordinates of the box and the box line type
    :type legendTemplate: vcs.Plegend.Pls

    :param linecolors: list containing the colors of each line to draw
    :type linecolors: list of either colorInt, (r,g,b,opacity), or string color names
    
    :param linetypes: list containing the type of each line to draw
    :type linetypes: list on int of line stype strings

    :param linewidths: list containing each line width
    :type linewidths: list of float

    :param markercolors: list of the markers colors to draw
    :type markercolors: list of either colorInt, (r,g,b,opacity), or string color names

    :param markertypes: list of the marker types to draw
    :type markertypes: list of int or  string of marker names

    :param markersizes: list of the size of each marker to draw
    :type markersizes: list of float

    :param strings: list of the string to draw next to each line/marker
    :type strings: list of string

    :param bg: do we draw in background or foreground
    :type bg: bool

    :param render: do we render or not (so it less flashy)
    :type render: bool
"""
        nlines = len(linecolors)
        # Now figures out the widest string and tallest
        text = vcs.createtext(To_source = templateLegend.textorientation,
                Tt_source = templateLegend.texttable)
        text.x = .5
        text.y = .5
        maxx = 0  # Max number of elts on X direction
        maxy = 0  # Max number of elts on Y direction
        dx = abs(templateLegend.x2 - templateLegend.x1)
        dy = abs(templateLegend.y2 - templateLegend.y1)

        # Loop until we can fit all elts into the box
        while maxx*maxy < nlines:
            maxwidth = 0
            maxheight = 0
            for i in range(nlines):
                text.string = strings[i]
                ext = canvas.gettextextent(text)[0]
                maxwidth = max(maxwidth,ext[1]-ext[0])
                maxheight = max(maxheight,ext[3]-ext[2])
            leg_lines = maxwidth/3.
            leg_spc = leg_lines/3.
            maxwidth += leg_lines+leg_spc
            maxx = int(dx/maxwidth)
            maxy = int(dy/maxheight)
            if maxx*maxy < nlines:
                # Does not fit less shrink the text a bit
                text.height -= 1
            if text.height==0:
                # Oh well it cannot fit...
                # We settle for the smallest size
                text.height=1
                break

        nH = min(maxx,len(strings)) # How many elts on horizontal direction
        nV = numpy.ceil(nlines/float(nH))  # How many elts vertically
        spcX = (dx - maxwidth*nH)/(nH+1)
        spcY = (dy - maxheight*nV)/(nV+1)
        txs = []
        tys = []
        ts = []
        x1 = min(templateLegend.x1,templateLegend.x2)
        y1 = max(templateLegend.y1,templateLegend.y2)
        # Box around legend area
        ln = canvas.createline(source = templateLegend.line)
        ln.x = [templateLegend.x1,templateLegend.x2,templateLegend.x2,templateLegend.x1,templateLegend.x1]
        ln.y = [templateLegend.y1,templateLegend.y1,templateLegend.y2,templateLegend.y2,templateLegend.y1]
        canvas.plot(ln,bg=bg,render=render)

        # Create the objects
        for i in range(len(strings)):
            col = int(i % nH)
            row = int(i/nH)
            # TODO check if previous line was identical
            # so that we create less objet/renderers
            ln = canvas.createline()
            ln.color = [linecolors[i],]
            ln.type = linetypes[i]
            ln.width = linewidths[i]
            ln.priority = templateLegend.priority
            # TODO check if previous marker was identical
            # so that we create less objet/renderers
            mrk = canvas.createmarker()
            mrk.color = [markercolors[i]]
            mrk.type = markertypes[i]
            mrk.size = markersizes[i]
            mrk.priority = templateLegend.priority
            xs = x1+spcX+col*(maxwidth+spcX)
            ln.x = [xs,xs+leg_lines]
            mrk.x = [xs+leg_lines/2.]
            txs.append(xs+leg_lines+leg_spc)
            ts.append(strings[i])
            ys = y1 - row*(maxheight+spcY) - spcY - maxheight/2.
            ln.y = [ys,ys]
            mrk.y = [ys]
            tys.append(ys)
            canvas.plot(ln,bg=bg,render=render)
            canvas.plot(mrk,bg=bg,render=render)
        text.halign = "left"
        text.string = ts
        text.x = txs
        text.y = tys
        #text.viewport = [0,1,0,1]
        text.priority = templateLegend.priority
        canvas.plot(text,bg=bg,render=render)
