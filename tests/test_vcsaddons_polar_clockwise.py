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
        polar.clockwise = True
        polar.plot(mag, theta)
        self.checkImage('test_vcsaddons_polar_clockwise.png')
