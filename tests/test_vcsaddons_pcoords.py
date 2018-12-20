import basetest
import vcsaddons
import numpy
import vcs
import cdms2

class VCSAddonTestParallelCoordinates(basetest.BaseTest):
    def setUp(self):
        super(VCSAddonTestParallelCoordinates, self).setUp()
        self.gm = vcsaddons.createparallelcoordinates(x=self.x)
        f = cdms2.open("tests/data/pcoords.nc")
        self.data = f("pcoords")
        ax = cdms2.createAxis(['NAM_DJF', 'NAM_JJA', 'NAM_MAM', 'NAM_SON', 'NAO_DJF', 'NAO_JJA',
                               'NAO_MAM', 'NAO_SON', 'PDO_monthly', 'PNA_DJF', 'PNA_JJA',
                               'PNA_MAM', 'PNA_SON', 'SAM_DJF', 'SAM_JJA', 'SAM_MAM', 'SAM_SON'])
        self.data.setAxis(0, ax)
        ax = cdms2.createAxis(['ACCESS1-0', 'ACCESS1-3', 'BCC-CSM1-1', 'BCC-CSM1-1-M', 'BNU-ESM',
                               'CanESM2', 'CCSM4', 'CESM1-BGC', 'CESM1-CAM5', 'CESM1-FASTCHEM',
                               'CESM1-WACCM', 'CMCC-CESM', 'CMCC-CM', 'CMCC-CMS', 'CNRM-CM5',
                               'CNRM-CM5-2', 'CSIRO-Mk3-6-0', 'EC-EARTH', 'FGOALS-g2', 'FIO-ESM',
                               'GFDL-CM2p1', 'GFDL-CM3', 'GFDL-ESM2G', 'GFDL-ESM2M', 'GISS-E2-H',
                               'GISS-E2-H-CC', 'GISS-E2-R', 'GISS-E2-R-CC', 'HadCM3',
                               'HadGEM2-AO', 'HadGEM2-CC', 'HadGEM2-ES', 'INMCM4', 'IPSL-CM5A-LR',
                               'IPSL-CM5A-MR', 'IPSL-CM5B-LR', 'MIROC-ESM', 'MIROC-ESM-CHEM',
                               'MIROC5', 'MPI-ESM-LR', 'MPI-ESM-MR', 'MPI-ESM-P', 'NorESM1-M',
                               'NorESM1-ME'])
        self.data.setAxis(1, ax)
        # Preprare the canvas areas
        t = vcs.createtemplate()
        # Create a text orientation object for xlabels
        to=vcs.createtextorientation()
        to.angle=-75
        to.halign="right"
        # Tell template to use this orientation for x labels
        t.xlabel1.textorientation = to.name

        # Define area where plot will be drawn in x direction
        t.reset('x',0.05,0.9,t.data.x1,t.data.x2)
        ln = vcs.createline()

        # Turn off box around legend
        ln.color = [[0,0,0,0]]
        t.legend.line = ln
        # turn off box around data area
        t.box1.priority = 0

        # Define box where legend will be drawn
        t.legend.x1 = .91
        t.legend.x2 = .99
        # use x/y of data drawn for legend height
        #t.legend.y1 = t.data.y1
        #t.legend.y2 = t.data.y2
        t.legend.y1 = 0.1
        t.legend.y2 = 0.9

        t.data.x2 = 0.9
        self.t = t

    def testSetDatawcYs(self):
        self.gm.datawc_y1 = [.7]
        self.gm.datawc_y2 = [2.6]
        self.gm.plot(self.data, self.t)
        self.checkImage('test_vcsaddons_pcoords_DataWcYs.png')

    def testSetDatawcYlabels(self):
        self.gm.datawc_y1 = [.7]
        self.gm.datawc_y2 = [2.6]
        self.gm.yticlabels = [{.5: ".5", 1: "1", 2: "2"}, {
            2.2: "2.2", 2: "TWO", 2.4: ""}, {5: "5"}, ]
        self.gm.plot(self.data, self.t)
        self.checkImage('test_vcsaddons_pcoords_DataWcYlabels.png')

