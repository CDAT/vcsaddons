import basetest


class VCSAddonTest(basetest.BaseTest):
    def test2(self):
        self.M.legend.direction = 'vertical'
        for i in range(12):
            t = self.M.get(legend='local')
        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_2.png')
