import basetest
import vcsaddons
import sys
import os
import cdms2
import cdat_info
import vcsaddons.EzPlot
import cdutil
import vcs

class EzPlotTest(basetest.BaseTest):
    def testLinePlot(self):
        variables = [[1, 2, 3, 4, 3, 2, 1]]

        plotfunction = vcsaddons.EzPlot.EzLinePlot(defaultgridcolor=[(50, 50, 50, 50)])

        canvas = self.x

        # Customize the lines used to draw the plots
        line_type  = ["solid"]
        line_widths = [5]

        # Customize the markers drawn
        marker_type = [None]

        # Customize Legend Text
        legend_texts = ["Test Line"]
        legend_text_colors = ['black']

        marker = vcs.createmarker()
        marker.size = 3
        marker.color = ["black", "black"]
        marker.type = ["triangle_up", "triangle_down"]


        plotfunction.lineplot(data=variables, canvas=canvas, title="Simple EzLinePlot", titlesize=25,
                                  autoxaxis=True, autoyaxis=True,
                                  marker=marker, bottom_label="Non-dimensional values", horizontallabelsize=20,
                                  legendtextcolors=legend_text_colors, legendtexts=legend_texts,
                                  enablegrid=True, legendbackgroundcolor="white")

        self.checkImage("test_vcsaddons_EzPlot_00.png")


