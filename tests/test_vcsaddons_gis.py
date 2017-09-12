import vcsaddons._gis
import unittest

class VCSAddons(unittest.TestCase):
    def testgis(self):
        sources = ['tests/data/fe_2007_06_county.dbf','tests/data/co1990p020.dbf']
        keys= [['NAME', 'CNTYIDFP', 'FUNCSTAT', 'LSAD', 'CLASSFP', 'COUNTYFP', 'UR', 'MTFCC', 'NAMELSAD', 'STATEFP', 'COUNTYNS'],
                ['PERIMETER', 'STATE_FIPS', 'AREA', 'CO1990P020', 'COUNTY', 'STATE', 'FIPS', 'SQUARE_MIL']]
        tested_keys = ["NAME","COUNTY"]
        tested_len = [58,6136]
        for i,s in enumerate(sources):
            D = vcsaddons._gis.readdbffile(s)
            self.assertEqual(sorted(D.keys()),sorted(keys[i]))
            self.assertEqual(len(D[tested_keys[i]]),tested_len[i])

