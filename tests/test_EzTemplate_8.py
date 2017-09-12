import basetest

class VCSAddonTest(basetest.BaseTest):
    def test8(self):
        ## 12 plots plotted with different spacing param
        self.M.spacing.horizontal=.25
        self.M.spacing.vertical=.1
        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_8.png')
