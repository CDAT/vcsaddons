from setuptools import setup, Extension
from subprocess import Popen, PIPE

src = ['Src/shpopen.c','Src/readshape.c','Src/dbfopen.c']

try:
    import cdat_info

    Version = cdat_info.Version
except Exception:
    Version = "???"
print("VERSION:", Version)

setup (name = "vcsaddons",
       version=Version,
       description = "addons for VCS",
       url = "http://cdat.llnl.gov",
       packages = ['vcsaddons','EzTemplate','EzPlot'],
       package_dir = {'vcsaddons': 'Lib', 'EzTemplate':'EzTemplate/Lib', 'EzPlot':'EzPlot/Lib'},
       ext_modules = [
    Extension('vcsaddons._gis',
              src,['Include']
              ),
    ]
       )
