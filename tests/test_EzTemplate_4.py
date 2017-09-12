import basetest
## 12 plot playing with margins and legend thickness

class VCSAddonTest(basetest.BaseTest):
    def test4(self):
        self.M.margins.top=.25
        self.M.margins.bottom=.25
        self.M.margins.left=.25
        self.M.margins.right=.25
        ## The legend uses the bottom margin for display are
        ## We need to "shrink it"
        self.M.legend.thickness=.1
        for i in range(12):
            t=self.M.get()
        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_4.png')
