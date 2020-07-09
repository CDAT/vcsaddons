from __future__ import print_function
import unittest
import cdat_info
import os
import vcs
import sys
from vcsaddons import EzTemplate


class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.geometry = {"width": 1200, "height": 1090}
        if 'geometry' in kwargs:
            self.geometry = kwargs['geometry']
            del kwargs['geometry']
        self.bg = int(os.environ.get("VCS_BACKGROUND", 1))
        if 'bg' in kwargs:
            self.bg = kwargs['bg']
            del kwargs['bg']
        super(BaseTest, self).__init__(*args, **kwargs)

    def setUp(self):
        # This is for circleci that crashes for any mac bg=True
        self.x = vcs.init(geometry=self.geometry, bg=self.bg)
        self.x.setantialiasing(0)
        self.x.drawlogooff()
        if self.geometry is not None:
            self.x.setbgoutputdimensions(self.geometry['width'],
                                         self.geometry['height'],
                                         units="pixels")
        # if not self.bg:
        #    self.x.open()
        self.orig_cwd = os.getcwd()
        self.pngsdir = "tests_png"
        if not os.path.exists(self.pngsdir):
            os.makedirs(self.pngsdir, exist_ok=True)
        self.basedir = os.path.join("tests", "baselines")
        self.basedatadir = os.path.join("tests", "data")
        self.M = EzTemplate.Multi(rows=4, columns=3, x=self.x)

    def tearDown(self):
        os.chdir(self.orig_cwd)
        self.x.clear()
        del(self.x)
        # if png dir is empty (no failures) remove it
        # if glob.glob(os.path.join(self.pngsdir,"*")) == []:
        #    shutil.rmtree(self.pngsdir)

    def checkImage(self, fnm, src=None, threshold=cdat_info.defaultThreshold,
                   pngReady=False, pngPathSet=False):
        ret = cdat_info.checkImage(fnm, self.x, self.basedir, self.pngsdir, src,
                                    threshold, pngReady, pngPathSet)
        self.assertEqual(ret, 0)
        return ret

    def check_values_setting(self, gm, attributes,
                             good_values=[], bad_values=[]):
        if isinstance(attributes, str):
            attributes = [attributes, ]
        for att in attributes:
            for val in good_values:
                setattr(gm, att, val)
            for val in bad_values:
                try:
                    setattr(gm, att, val)
                    success = True
                except BaseException:
                    success = False
                else:
                    if success:
                        if hasattr(gm, "g_name"):
                            nm = gm.g_name
                        elif hasattr(gm, "s_name"):
                            nm = gm.s_name
                        else:
                            nm = gm.p_name
                        raise Exception(
                            "Should not be able to set %s attribute '%s' to %s" %
                            (nm, att, repr(val)))


def run():
    unittest.main()
