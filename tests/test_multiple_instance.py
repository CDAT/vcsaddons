import cdms2,cdat_info
import basetest
import os
import EzTemplate
import vcs

class VCSAddonTest(basetest.BaseTest):
    def testMultiple(self):
        f=cdms2.open(os.path.join(cdat_info.get_sampledata_path(),'clt.nc'))
        s=f('clt',slice(0,1))
        f.close()

        M=EzTemplate.Multi(rows=2,columns=2)
        for i in range(4):
            self.x.plot(s,M.get())

        y=vcs.init(bg=True,geometry={"width": 1200, "height": 1090})
        M2=EzTemplate.Multi(rows=1,columns=2)
        for i in range(2):
            y.plot(s,M2.get())
        y.png("tests_png/test_vcsaddons_multiple_y.png")
        self.checkImage("test_vcsaddons_multiple_x.png")
        self.checkImage("test_vcsaddons_multiple_y.png",pngReady=True)

