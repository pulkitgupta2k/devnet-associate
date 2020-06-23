import unittest
from cuboid_volume import *

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),1)

    def test_input_values(self):
        self.assertRaises(TypeError, cuboid_volume, True)

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2, exit=False)