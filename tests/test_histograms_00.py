import basetest
import vcsaddons
import sys
import os
import cdms2
import cdat_info

cdms2.setAutoBounds("on")

class Histo(basetest.BaseTest):
    def testHistogram(self):
        h = vcsaddons.createhistogram()

        f=cdms2.open(os.path.join(cdat_info.get_sampledata_path(),'clt.nc'))
        s=f("clt")

        h.datawc_x1=-.5
        h.datawc_x2=119.5
        h.datawc_y1=0.
        h.datawc_y2=105

        self.x.plot(s[:,6,8],h)
        self.checkImage("test_vcsaddons_histogram_00.png")
