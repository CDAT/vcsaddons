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
        polar.markersizes = [8.]
        polar.markercolors = ["red"]
        polar.markertypes = ["square"]
        polar.linepriority=1
        polar.linetypes=["dot"]
        polar.linecolors = ["blue"]
        polar.linewidths = [2.]
        polar.datawc_y1 = 0
        polar.datawc_y2= 7
        tmpl = self.x.createtemplate()
        dot = self.x.createline()
        dot.type="dot"
        dot.color = ["grey"]
        tmpl.ymintic1.line = dot
        tmpl.ymintic1.priority = 1
        polar.magnitude_mintics = [.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
        polar.magnitude_ticks = [1,1.1,2,7]
        polar.datawc_y1 = 1.e20
        polar.datawc_y2 = 1.e20
	polar.plot(mag,theta,template=tmpl)
	self.checkImage('test_vcsaddons_polar_no_linear_mag.png')

