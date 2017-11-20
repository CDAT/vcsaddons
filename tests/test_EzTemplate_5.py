import basetest


class VCSAddonTest(basetest.BaseTest):
    def test5(self):
        self.M.margins.top = .25
        self.M.margins.bottom = .25
        self.M.margins.left = .25
        self.M.margins.right = .25

        self.M.legend.direction = 'vertical'
        # The legend uses the right margin for display are
        # We need to "shrink it"
        self.M.legend.thickness = .05
        for i in range(12):
            t = self.M.get()

        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_5.png')
