# Adapted for numpy/ma/cdms2 by convertcdms.py
import thermo,vcs,cdms2
import os,sys
import basetest

class ThermoTest(basetest.BaseGraphicsTest):
    def testBasic(self):

        f=cdms2.open(vcs.sample_data+'/dar.meteo.mod.cam3.era.v31.h0.l3.nrstpt.cp.2000070100.2000080100.tau.12.36.nc')

        s=f('ta',time=slice(0,1),squeeze=1)

        th = thermo.Gth(x=self.x,name='my')

        try:
            th.plot_TP(s)
            failed = False
        except:
            failed = True
            pass

        if not failed:
            print(failed)
            raise "Error should have raised an exception on all missing data!"

        th.clear()

        s=f('ta',time=slice(1,2),squeeze=1)
        th.type='stuve'
        th.plot_TP(s)
        th.clear()

        th.type='emagram'
        th.plot_TP(s)
        th.clear()

        th.type='tephigram'
        th.plot_TP(s)
        th.clear()

        th.type='skewT'
        th.plot_TP(s)
        th.clear()

