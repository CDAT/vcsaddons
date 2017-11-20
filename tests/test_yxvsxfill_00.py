import cdms2
import cdat_info
import basetest
import os
import MV2
import cdutil
import vcsaddons


class VCSAddonTest(basetest.BaseTest):
    def testYxfilled(self):
        f = cdms2.open(os.path.join(cdat_info.get_sampledata_path(), 'clt.nc'))

        cdms2.setAutoBounds("on")
        s = f("clt")

        d1 = MV2.max(s, axis=0)
        d2 = MV2.min(s, axis=0)

        s1 = cdutil.averager(d1, axis='x')
        s2 = cdutil.averager(d2, axis='x')

        yf = vcsaddons.createyxvsxfill()
        yf.linewidth = 5
        yf.linecolor = "red"
        yf.fillareacolor = "blue"

        self.x.plot(s1, s2, yf)

        self.checkImage("test_yxvsxfill.png")
