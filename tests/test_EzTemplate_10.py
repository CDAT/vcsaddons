import basetest


class VCSAddonTest(basetest.BaseTest):
    def test10(self):
        self.M.legend.direction = 'vertical'
        for i in range(12):
            t = self.M.get(legend='local')
            if i % 3 != 2:
                t.legend.priority = 0  # Turn off legend
        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_10.png')
