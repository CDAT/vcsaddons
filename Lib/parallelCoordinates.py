import vcs
import numpy
import vcsaddons


class Gpc(vcsaddons.core.VCSaddon):
    def __init__(self,name,source="default",x=None,template=None):
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
    def list(self):
        print 'graphics method = ',self.g_name
        print 'name = ',self.name
        print 'datawc_x1 = ',self.datawc_x1
        print 'datawc_x2 = ',self.datawc_x2
        print 'datawc_y1 = ',self.datawc_y1
        print 'datawc_y2 = ',self.datawc_y2
        print 'xmtics1 = ',self.xmtics1
        print 'xmtics2 = ',self.xmtics2
        print 'ymtics = ',self.ymtics
        print 'xticlabels1 = ',self.xticlabels1
        print 'xticlabels2 = ',self.xticlabels2
        print 'yticlabels = ',self.yticlabels
        print 'xaxisconvert = ',self.xaxisconvert
        print 'yaxisconvert = ',self.yaxisconvert

    def drawYAxes(self,mins,maxs,labels,template,X,bg):
        N = len(labels)
        l = X.createline(source=template.box1.line)
        l.viewport = [template.data.x1, template.data.x2,
                template.data.y1, template.data.y2]
        ys = [[0,1]]*N
        xs = [[x/(N-1.),x/(N-1.)] for x in range(N)]

        l.x=xs+[[0,1,1,0,0]]
        l.y=ys+[[0,0,1,1,0]]
        l.priority = template.box1.priority
        X.plot(l,bg=bg)

        l1 = X.createline(source = template.ytic1.line)
        l2 = X.createline(source = template.ytic2.line)
        le1 = X.createline(source = template.ytic1.line)
        le2 = X.createline(source = template.ytic2.line)
        txt = X.createtext(To_source = template.ylabel1.textorientation,
                Tt_source =  template.ylabel1.texttable)
        txt.priority = template.ylabel1.priority
        l1.priority = template.ytic1.priority
        l2.priority = template.ytic2.priority
        le1.priority = template.ytic1.priority
        le2.priority = template.ytic2.priority
        if 0<txt.priority>=template.data.priority:
            txt.priority+=1
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
        for i,lbl in enumerate(labels):
            x = float(i)/(N-1)
            for y in lbl:
                st.append(lbl[y])
                Y= (y - mins[i])/(maxs[i]-mins[i])
                ys.append([Y,Y])
                yt.append(Y)
                d1 = abs(template.ytic1.x2-template.ytic1.x1)
                mn = min(template.data.x1,template.data.x2)
                dt = mn - template.ylabel1.x
                xs1.append([x-d1,x])
                xt.append(x-dt)
                if i==0:
                    xe1.append([template.data.x1-d1,template.data.x1])
                    ye1.append([Y,Y])
                elif i==N-1:
                    xe2.append([template.data.x2+d2,template.data.x2])
                    ye2.append([Y,Y])
                d2 = abs(template.ytic2.x2-template.ytic2.x1)
                xs2.append([x+d2,x])
        l1.viewport = l.viewport
        l2.viewport = l.viewport
        le1.viewport = [0,1,template.data.y1, template.data.y2]
        le2.viewport = [0,1,template.data.y1, template.data.y2]
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
        X.plot(l1,bg=bg)
        X.plot(l2,bg=bg)
        X.plot(le1,bg=bg)
        X.plot(le2,bg=bg)
        X.plot(txt,bg=bg)


    def plot(self,array, template=None, bg=False, x=None):
        """Parallel Coordinates plot array must be of shape:
        (...,Dim1,Nlines)
        """
        if not array.ndim > 1:
            raise Exception("Array must be at least 2D")
        nlines = array.shape[-1]
        length = array.shape[-2]

        # Pad attributes related to Y axis
        for att in ["datawc_y1","datawc_y2",
                "yticlabels"]:
            # prepare local lists
            exec("%s = list(self.%s)" % (att,att))
            exec("while len(%s) < length: %s+=[%s[-1]]" % (att,att,att))

        data = array.asma()
        maxs = numpy.ma.max(data,axis=-1)
        mins = numpy.ma.min(data,axis=-1)

        if template is not None:
            t = vcs.createtemplate(source=template)
        else:
            t = vcs.createtemplate(source=self.template)

        for i in range(length):
            levels = vcs.mkscale(mins[i],maxs[i])
            # Do we need to create our range
            if numpy.allclose(datawc_y1[i],1.e20):
                datawc_y1[i]=levels[0]
                datawc_y2[i]=levels[-1]
            maxs[i] = datawc_y2[i]
            mins[i] = datawc_y1[i]

            # Do we have tics?
            if yticlabels[i] == "*":
                yticlabels[i]=vcs.mklabels(levels)
        if x is None:
            x = self.x
        self.drawYAxes(mins,maxs,yticlabels,t,x,bg) 
        ax = array.getAxis(-2)
        deflbls = {}
        for i in range(length):
            deflbls[float(i)/(length-1)] = str(ax[i])
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

        for l,lbls in enumerate([lbls1,lbls1m,lbls2,lbls2m]):
            ln = x.createline(source=t.xtic1.line)
            xs = []
            ys = []
            if l % 2 == 0:
                if l == 0:
                    txt = x.createtext(To_source = t.xlabel1.textorientation,
                            Tt_source = t.xlabel1.texttable)
                else:
                    txt = x.createtext(To_source = t.xlabel2.textorientation,
                            Tt_source = t.xlabel2.texttable)
                txs = []
                tys = []
                ts = []
            for loc in lbls:
                xs.append([loc,loc])
                if l==0:
                    ys.append([t.xtic1.y1,t.xtic1.y2])
                    txs.append(loc)
                    tys.append(t.xlabel1.y)
                    ts.append(lbls[loc])
                    ln.priority = t.xtic1.priority
                    txt.priority = t.xlabel1.priority
                elif l == 1:
                    ys.append([t.xmintic1.y1,t.xmintic1.y2])
                    ln.priority = t.xmintic1.priority
                elif l == 2:
                    ys.append([t.xtic2.y1,t.xtic2.y2])
                    txs.append(loc)
                    tys.append(t.xlabel2.y)
                    ts.append(lbls[loc])
                    ln.priority = t.xtic2.priority
                    txt.priority = t.xlabel2.priority
                elif l == 3:
                    ys.append([t.xmintic2.y1,t.xmintic2.y2])
                    ln.priority = t.xmintic2.priority
            ln.x = xs
            ln.y = ys
            ln.viewport = [t.data.x1,t.data.x2,0,1]
            x.plot(ln,bg=bg)
            if l % 2 == 0:  # text on
                txt.viewport = ln.viewport
                txt.x = txs
                txt.y = tys
                txt.string = ts
                x.plot(txt,bg=bg)

        # Normalizes
        deltas = maxs-mins
        data = (data-mins[:,numpy.newaxis])/deltas[:,numpy.newaxis]

        # Pad attributes related to number of lines
        lineAtts = ["linetypes","linewidths",
                "markertypes","markersizes"]
        if self.markercolors is not None:
            lineAtts.append("markercolors")
        if self.linecolors is not None:
            lineAtts.append("linecolors")
        for att in lineAtts:
            # prepare local lists
            exec("%s = list(self.%s)" % (att,att))
            exec("while len(%s) < nlines: %s+=[%s[-1]]" % (att,att,att))

        if self.linecolors is None:
            linecolors = vcs.getcolors(range(nlines+1))
        if self.markercolors is None:
            markercolors = vcs.getcolors(range(nlines+1))

        leg_prio = t.legend.priority
        t.blank()
        t.data.priority = 1
        # Now draws the legend
        # Now figures out the widest string and tallest
        text = vcs.createtext(To_source = template.legend.textorientation,
                Tt_source = template.legend.texttable)
        text.x = .5
        text.y = .5
        ax = array.getAxis(-1)
        maxx = 0
        maxy = 0
        dx = abs(t.legend.x2 - t.legend.x1)
        dy = abs(t.legend.y2 - t.legend.y1)
        while maxx*maxy < nlines:
            width = 0
            height = 0
            for i in range(nlines):
                text.string = str(ax[i])
                ext = x.gettextextent(text)[0]
                width = max(width,ext[1]-ext[0])
                height = max(height,ext[3]-ext[2])
            leg_lines = width/3.
            leg_spc = leg_lines/3.
            width += leg_lines+leg_spc
            maxx = int(dx/width)
            maxy = int(dy/height)
            if maxx*maxy < nlines:
                text.height -= 1
            if text.height==0:
                text.height=1
                break

        nH = maxx
        nV = numpy.ceil(nlines/float(nH))
        spcX = (dx - width*nH)/(nH+1)
        spcY = (dy - height*nV)/(nV+1)
        txs = []
        tys = []
        ts = []
        x1 = min(template.legend.x1,template.legend.x2)
        y1 = max(template.legend.y1,template.legend.y2)
        # Box around legend area
        ln = x.createline(source = template.legend.line)
        ln.x = [template.legend.x1,template.legend.x2,template.legend.x2,template.legend.x1,template.legend.x1]
        ln.y = [template.legend.y1,template.legend.y1,template.legend.y2,template.legend.y2,template.legend.y1]
        x.plot(ln,bg=bg)
        for i in range(nlines):
            l = vcs.create1d()
            l.colormap = self.colormap
            l.linecolor = linecolors[i]
            l.linewidth = linewidths[i]
            l.linetype = linetypes[i]
            l.marker = markertypes[i]
            l.markercolor = markercolors[i]
            l.markersize = markersizes[i]
            l.datawc_y1 = 0.
            l.datawc_y2 = 1.
            x.plot(data[:,i],t,l,bg=bg)
            col = int(i % nH)
            row = int(i/nH)
            ln = x.createline()
            ln.color = linecolors[i]
            ln.type = linetypes[i]
            ln.width = linewidths[i]
            ln.priority = template.legend.priority
            mrk = x.createmarker()
            mrk.color = markercolors[i]
            mrk.type = markertypes[i]
            mrk.size = markersizes[i]
            mrk.priority = template.legend.priority
            xs = x1+spcX+col*(width+spcX)
            ln.x = [xs,xs+leg_lines]
            mrk.x = [xs+leg_lines/2.]
            txs.append(xs+leg_lines+leg_spc)
            ts.append(str(ax[i]))
            ys = y1 - row*(height+spcY) - spcY
            ln.y = [ys,ys]
            mrk.y = [ys]
            tys.append(ys)
            x.plot(ln,bg=bg)
            x.plot(mrk,bg=bg)
        text.halign = "left"
        text.string = ts
        text.x = txs
        text.y = tys
        text.viewport = [0,1,0,1]
        text.priority = leg_prio
        x.plot(text,bg=bg)
