#!/usr/bin/env python
from distutils.core import setup, Extension

src = ['Src/shpopen.c','Src/readshape.c','Src/dbfopen.c']

setup (name = "vcsaddons",
       version='8.0',
       description = "addons for VCS",
       url = "http://cdat.sf.net",
       packages = ['vcsaddons','EzTemplate','EzPlot'],
       package_dir = {'vcsaddons': 'Lib', 'EzTemplate':'EzTemplate/Lib', 'EzPlot':'EzPlot/Lib'},
       ext_modules = [
    Extension('vcsaddons._gis',
              src,['Include']
              ),
    ],
       data_files = [("share/vcsaddons",('share/test_data_files.txt',))]
       )
