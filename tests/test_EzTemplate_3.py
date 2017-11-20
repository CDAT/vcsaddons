import basetest


class VCSAddonTest(basetest.BaseTest):
    def test3(self):
        self.M.legend.stretch = 2.5  # 250% of width (for middle one)
        for i in range(12):
            t = self.M.get(legend='local')
            if i % 3 != 1:
                t.legend.priority = 0  # Turn off legend

        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_3.png')
