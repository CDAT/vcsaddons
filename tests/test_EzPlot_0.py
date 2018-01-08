import basetest
import vcsaddons
import sys
import os
import cdms2
import cdat_info
import vcsaddons.EzPlot
import cdutil

class EzPlotTest(basetest.BaseTest):
    def testLinePlot(self):
        variables = [[1, 2, 3, 4, 3, 2, 1]]

        plotfunction = vcsaddons.EzPlot.EzLinePlot(defaultgridcolor=[(50, 50, 50, 50)])

        canvas = self.x
        
        line_type  = ["solid"]
        line_widths = [8]

        marker_type = [None]

        legend_texts = ["Test Line"]
        legend_text_colors = ['black']

        marker = vcs.createmarker()
        marker.size = 6
        marker.color = ["black", "black"]
        marker.type = ["triangle_up", "triangle_down"]

        plotfunction.lineplot(data=variables, canvas=canvas, title="Simple EzLinePlot",
                              autoxaxis=True, autoyaxis=True,
                              marker=marker, bottom_label="Non-dimensional values",
                              legendtextcolors=legend_text_colors, legendtexts=legend_texts,
                              enablegrid=True, legendbackgroundcolor="white")

        self.checkImage("test_vcsaddons_EzPlot_00.png")


