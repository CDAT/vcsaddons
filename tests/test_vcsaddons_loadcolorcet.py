import vcs
import unittest
import vcsaddons

class TestColorcetImport(unittest.TestCase):
    def testLoad(self):
        cmaps = vcs.listelements("colormap")
        self.assertFalse("cet_rainbow" in cmaps)
        norig = len(cmaps)
        vcsaddons.loadcolorcetcolormaps("rainbow")
        cmaps = vcs.listelements("colormap")
        self.assertEqual(len(cmaps),norig+1)
        self.assertTrue("cet_rainbow" in cmaps)

