import cdms2,cdat_info
import basetest
import os
import vcsaddons

class VCSAddonTest(basetest.BaseTest):
    def testUserContinent(self):
        f=cdms2.open(os.path.join(cdat_info.get_sampledata_path(),'clt.nc'))
        c=vcsaddons.createusercontinents(x=self.x)
        lon1=-10
        lon2=25
        lat1=35
        lat2=60
        c.types = ['shapefile','shapefile']
        c.sources = ['WDBII_shp/c/WDBII_border_c_L3.shp','WDBII_shp/c/WDBII_border_c_L3.shp']
        c.colors = [241,244,]
        c.widths=[2,2]
        c.lines=['solid','dot']
        s=f("clt",latitude=(lat1,lat2),longitude=(lon1,lon2),time=slice(0,1))
        t=self.x.createtemplate()
        iso=self.x.createisofill()
        lons = range(-180,181,5)
        L={}
        for l in lons:
            if l<0:
                L[int(l)]="%iW" % int(l)
            elif l>0:
                L[int(l)]="%iE" % int(l)
            else:
                L[0]="0"
        L2={}
        for l in lons:
            if l<0:
                L2[int(l)]="%iS" % int(l)
            elif l>0:
                L2[int(l)]="%iN" % int(l)
            else:
                L2[0]="Eq"

        iso.xticlabels1=L
        iso.xticlabels2=L
        iso.yticlabels1=L2
        iso.yticlabels2=L2
        c.xticlabels1=L
        c.xticlabels2=L
        c.yticlabels1=L2
        c.yticlabels2=L2
        self.x.plot(s,t,iso,continents=0,ratio='autot')
        self.x.plot(s,c,t,ratio='autot')
        self.checkImage("test_user_continents_00.png")

