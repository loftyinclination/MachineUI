import sys
sys.path.append('C:\\Users\\Alastair\\OneDrive\\Documents\\Creative\\Python\\Gen2')
import unittest
import math
from src.classes import Node

class classes_Test(unittest.TestCase):

    def test_direction(self):
        steps = 30
        angles = [i * (2 * math.pi / steps) for i in range(steps)]
        calculated = [Node(Node(None, 0, 0), math.cos(d), math.sin(d)) for d in angles]
        self.assertAlmostEqual(angles, calculated)

if __name__ == '__main__':
    unittest.main()
