import basetest


class VCSAddonTest(basetest.BaseTest):
    def test1(self):
        for i in range(12):
            t = self.M.get()
        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_0.png')
