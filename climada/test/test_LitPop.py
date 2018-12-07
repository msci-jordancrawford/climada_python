"""
This file is part of CLIMADA.

Copyright (C) 2017 CLIMADA contributors listed in AUTHORS.

CLIMADA is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free
Software Foundation, version 3.

CLIMADA is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with CLIMADA. If not, see <https://www.gnu.org/licenses/>.

Tests on LitPop exposures.
"""

import unittest

from climada.entity.exposures.litpop import LitPop

# ---------------------
class TestDefault(unittest.TestCase):
    """Test data availability checks (blackmarble nightlight and gpw population):"""

    def test_switzerland_pass(self):
        """Create LitPop entity for Switzerland:"""
        country_name = ['CHE']
        resolution = 300
        ent = LitPop()
        with self.assertLogs('climada.entity.exposures.litpop', level='INFO') as cm:
            ent.set_country(country_name, res_arcsec = resolution)
        print(cm)
        self.assertIn('Generating LitPop data at a resolution of 300 arcsec', cm.output[0])
        self.assertTrue(ent.region_id.min() == 756)
        self.assertTrue(ent.region_id.max() == 756)
        self.assertTrue(ent.value.sum() == 3343726398022.6597)
        
class TestDataCheck(unittest.TestCase):
    """Default test LitPop for Switzerland:"""

    def blackmarble_data(self):
        """Test data availability checks (blackmarble nightlight):"""
        ent = LitPop()

# Execute Tests
TESTS = unittest.TestLoader().loadTestsFromTestCase(TestDefault)
unittest.TextTestRunner(verbosity=2).run(TESTS)
