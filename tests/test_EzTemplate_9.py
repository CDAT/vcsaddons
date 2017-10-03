import basetest

class VCSAddonTest(basetest.BaseTest):
    def test9(self):
        # Test a good one
        tok = self.M.get(row=3,column=2)

        # Test out of range column
        with self.assertRaises(ValueError) as context:
            self.M.get(row=1,column=12)
        self.assertTrue('You requested template for column 12 but you defined 3 columns only' in context.exception)

        # Test out of range row
        with self.assertRaises(ValueError) as context:
            self.M.get(row=14,column=1)
        self.assertTrue('You requested template for row 14 but you defined 4 rows only' in context.exception)
