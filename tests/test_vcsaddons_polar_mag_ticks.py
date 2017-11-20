import basetest
import vcsaddons
import numpy


class VCSAddonTestPolar(basetest.BaseTest):
    def testMagnitudeTooHigh(self):
        nPoints = 75
        theta0 = .001
        e = numpy.exp(1.)
        pi = numpy.pi
        thetaN = 2. * pi
        delta = (thetaN - theta0) / (nPoints - 1)
        theta = numpy.arange(theta0, thetaN, delta)
        mag = theta
        polar = vcsaddons.createpolar()
        polar.x = self.x
        polar.markersizes = [8.]
        polar.markercolors = ["red"]
        polar.markertypes = ["square"]
        polar.linepriority = 1
        polar.linetypes = ["dot"]
        polar.linecolors = ["blue"]
        polar.linewidths = [2.]
        ticks = {}
        for a in range(45, 361, 45):
            ticks[float(a) / 180. * numpy.pi] = r"$%i^o$" % a
        polar.xticlabels1 = ticks
        polar.datawc_y1 = 0
        polar.datawc_y2 = 7
        polar.yticlabels1 = {1.: "one", 3.: "three", 5: "five"}
        polar.magnitude_tick_angle = pi / 4.
        to = self.x.createtextorientation()
        to.angle = -45
        tmpl = self.x.createtemplate()
        tmpl.ylabel1.textorientation = to
        polar.plot(mag, theta, template=tmpl)
        self.checkImage('test_vcsaddons_polar_mag_ticks.png')
