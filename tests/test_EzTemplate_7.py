import basetest


class VCSAddonTest(basetest.BaseTest):
    def test7(self):
        # 12 plots plotted in reverse order
        icol = 3
        irow = 4
        for i in range(12):
            if i % 3 == 0:
                irow -= 1
            icol -= 1
            t = self.M.get(column=icol, row=irow)
            if icol == 0:
                icol = 3
        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_0.png')
