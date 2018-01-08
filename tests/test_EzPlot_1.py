import basetest
import vcsaddons
import sys
import os
import cdms2
import cdat_info
import vcsaddons.EzPlot
import cdutil
import math

class EzPlotTest(basetest.BaseTest):
    def testLinePlot(self):
        
        variables  = []
        line_type  = []
        line_widths = []
        legend_texts = []
        legend_text_colors = []
        marker_type = []
        
        for v in range(0, 10):
            var = []
            for i in range(0, 100):
                if v%2 == 0:
                    var.append(math.sin(2*math.pi*float(i-v)/100.0))
                else:
                    var.append(math.cos(2*math.pi*float(i-v)/100.0))
            line_type += ["solid"]
            line_widths += [6]
            if i%2 == 0:
                legend_texts += ["Sin"]
            else:    
                legend_texts += ["Cos"]
            legend_text_colors += ['black']
            marker_type += [None]
            variables.append(var)
    
        plotfunction = vcsaddons.EzPlot.EzLinePlot()

        canvas = self.x
        
        plotfunction.lineplot(data=variables, canvas=canvas, title="Simple 2 EzLinePlot",
                              linetypes=line_type, linewidths=line_widths,   
                              legendposition=[0.15, 0.25, 0.70, 0.80], legendtextcolors=legend_text_colors, legendtexts=legend_texts,
                              legendbackgroundcolor="yellow",
                              enablegrid=True)

        self.checkImage("test_vcsaddons_EzPlot_01.png")


