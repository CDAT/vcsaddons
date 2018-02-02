
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
        r_simple = 5. * numpy.sin(theta)
        # Another simple one
        r_simple_2 = 4. - 4. * numpy.cos(theta)
        polar = vcsaddons.createpolar()
        polar.x = self.x
        r2 = numpy.array([mag, r_simple, r_simple_2])
        polar.markercolors = ["red", "green", "blue"]
        polar.markertypes = ["square", "dot", "diamond"]
        polar.markersizes = [1., 5., 1.]
        polar.plot(r2, theta)
        self.checkImage('test_vcsaddons_polar_groups.png')
