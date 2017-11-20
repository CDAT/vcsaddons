import basetest
import vcsaddons
import numpy


class VCSAddonTestPolar(basetest.BaseTest):
    def testMagnitudeTooHigh(self):
        p = vcsaddons.createpolar()
        mag = numpy.arange(2.5, 8, 1)
        print(mag)
        n = len(mag)
        angle = numpy.arange(n) / float(n) * 2. * numpy.pi
        p.x = self.x
        p.magnitude_ticks = [2, 3, 4, 5, 6]
        p.plot(mag, angle)
        self.checkImage('test_vcsaddons_polar_magnitude_too_high.png')
