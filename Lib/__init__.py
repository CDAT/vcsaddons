gms = {}
import histograms
import polar
import EzTemplate
import yxvsxfill
import continents
import vcs
import parallelCoordinates


def createyxvsxfill(name=None,source='default',x=None,template=None):
    return yxvsxfill.Gyf(name,source=source,x=x,template=template)


def createhistogram(name=None,source='default',x=None,template=None):
    return histograms.Ghg(name,source=source,x=x,template=template)


def createusercontinents(name=None,source="default",x=None,template=None):
    return continents.Guc(name,source=source,x=x,template=template)


def createpolar(name=None, source="default", x=None, template=None):
    if "polar_oned" not in gms:
        polar.init_polar()
    return polar.Gpo(name, source=source, x=x, template=template)

def createparallelcoordinates(name=None, source="default", x=None, template=None):
    return parallelCoordinates.Gpc(name, source=source, x=x, template=template)

def getpolar(name=None):
    if "polar_oned" not in gms:
        init_polar()
    if name in gms["polar_oned"]:
        return gms["polar_oned"][name]
    raise KeyError("No Polar GM exists with name '%s'" % name)


