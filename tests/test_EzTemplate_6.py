import basetest

class VCSAddonTest(basetest.BaseTest):
    def test6(self):
## 12 plot one legend every other plot various orientation for legend
        for i in range(12):
            if i%2==1:
                if i%4 == 3:
                    self.M.legend.direction='vertical'
                t=self.M.get(legend='local')
                self.M.legend.direction='horizontal'
            else:
                t=self.M.get()
        self.M.preview(bg=True)
        self.checkImage('test_EzTemplate_6.png')
