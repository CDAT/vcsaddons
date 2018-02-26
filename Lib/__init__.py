from .core import gms
from . import histograms
from . import polar
from . import EzTemplateSrc as EzTemplate  # noqa
from . import yxvsxfill
from . import parallelCoordinates


def createyxvsxfill(name=None, source='default', x=None, template=None):
    return yxvsxfill.Gyf(name, source=source, x=x, template=template)


def createhistogram(name=None, source='default', x=None, template=None):
    return histograms.Ghg(name, source=source, x=x, template=template)

# Deprecated
# def createusercontinents(name=None,source="default",x=None,template=None):
#     return continents.Guc(name,source=source,x=x,template=template)


def createpolar(name=None, source="default", x=None, template=None):
    if "Gpo" not in gms:
        polar.init_polar()
    return polar.Gpo(name, source=source, x=x, template=template)


def createparallelcoordinates(
        name=None, source="default", x=None, template=None):
    return parallelCoordinates.Gpc(name, source=source, x=x, template=template)


def getpolar(name=None):
    if "Gpo" not in gms:
        polar.init_polar()
    if name in gms["Gpo"]:
        return gms["Gpo"][name]
    raise KeyError("No Polar GM exists with name '%s'" % name)
