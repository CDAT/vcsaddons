import basetest
import MV2
import cdms2
from vcsaddons import EzTemplate


class VCSAddonTest(basetest.BaseTest):
    def test11(self):
        bg = True
        n = 4

        self.M = EzTemplate.Multi(
            rows=1,
            columns=1,
            legend_direction='vertical',
            right_margin=.2,
            left_margin=.15,
            top_margin=.15,
            bottom_margin=.15)
        t = self.M.get()
        leg = t.legend
        tt = self.x.gettexttable(leg.texttable)
        to = self.x.gettextorientation(leg.textorientation)

        OD = EzTemplate.oneD(n=n, template=t)

        x = MV2.arange(0, 360)
        x = x / 180. * MV2.pi
        ax = cdms2.createAxis(x)
        self.x.portrait()

        for i in range(n):
            y = MV2.sin((i + 1) * x)
            y.setAxis(0, ax)
            yx = self.x.createyxvsx()
            yx.linecolor = 241 + i
            yx.datawc_y1 = -1.
            yx.datawc_y2 = 1.
            y.id = str(i)
            t = OD.get()
            self.x.plot(y, t, yx, bg=bg)
        self.checkImage('test_EzTemplate_11.png')
