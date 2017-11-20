import basetest


class VCSAddonTest(basetest.BaseTest):
    def test9(self):
        # Test a good one
        tok = self.M.get(row=3, column=2)

        # Test out of range column
        if hasattr(self,"assertRaisesRegex"):
            with self.assertRaisesRegex(ValueError, "You requested template for column 12 but you defined 3 columns only") as context:
                self.M.get(row=1, column=12)
        else:
            with self.assertRaises(ValueError) as cm:
                self.M.get(row=1, column=12)
                self.assertTrue("You requested template for column 12 but you defined 3 columns" in cm)

        # Test out of range row
        if hasattr(self,"assertRaisesRegex"):
            with self.assertRaisesRegex(ValueError, "You requested template for row 14 but you defined 4 rows only") as context:
                self.M.get(row=14, column=1)
        else:
            with self.assertRaises(ValueError) as context:
                self.M.get(row=14, column=1)
                self.assertTrue("You requested template for row 14 but you defined 4 rows only" in cm)
