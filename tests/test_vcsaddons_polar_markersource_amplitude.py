import basetest
import vcsaddons
import numpy

class VCSAddonTestPolar(basetest.BaseTest):
    def testMagnitudeTooHigh(self):
	nPoints = 75
	theta0 = .001
	e = numpy.exp(1.)
	pi = numpy.pi
	thetaN =  2.*pi
	delta = (thetaN-theta0)/(nPoints-1)
	theta = numpy.arange(theta0,thetaN,delta)
	mag = theta
	polar = vcsaddons.createpolar()
	polar.x=self.x
        polar.markercolors = [16, 66, 116, 143, 162, 181, 200, 219]
        polar.markercolorsource = "magnitude"
        tmpl = self.x.createtemplate()
        tmpl.legend.x1=.9
        tmpl.legend.x2=.99
        tmpl.legend.y1 = .2
        tmpl.legend.y2=.8
	polar.plot(mag,theta,template=tmpl)
	self.checkImage('test_vcsaddons_polar_markers_source_ampl.png')


