#!/usr/bin/env python
from setuptools import setup, Extension
from subprocess import Popen, PIPE

src = ['Src/shpopen.c','Src/readshape.c','Src/dbfopen.c']

p = Popen(
    ("git",
     "describe",
     "--tags"),
    stdin=PIPE,
    stdout=PIPE,
    stderr=PIPE)
try:
    descr = p.stdout.readlines()[0].strip().decode("utf-8")
    Version = "-".join(descr.split("-")[:-2])
    if Version == "":
        Version = descr
except:
    descr = Version

setup (name = "vcsaddons",
       version=descr,
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
