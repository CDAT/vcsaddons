import basetest

class VCSAddonTest(basetest.BaseTest):
    def test00(self):
        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_0.png')

