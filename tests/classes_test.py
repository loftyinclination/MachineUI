import sys
sys.path.append('C:\\Users\\Alastair\\OneDrive\\Documents\\Creative\\Python\\Gen2')
import unittest
import math
from src.classes import Node

class classes_Test(unittest.TestCase):

    def test_direction(self):
        steps = 30
        angles = [i * (2 * math.pi / steps) for i in range(steps)]
        for d in angles:
            self.assertAlmostEqual(Node(Node(None, 0, 0), math.cos(d), math.sin(d)).get_direction(), d)

    def test_split_parentless(self):
        center = Node(None, 0, 0)
        children = sorted(center.split(3, math.pi / 4, math.pi / 4, 1, 0, straight=True), key=lambda node: node.get_direction())
        expected = [Node(center, 1.0, 0.0), Node(center, 1 / math.sqrt(2), 1 / math.sqrt(2)), Node(center, 0.0, 1.0)]
        # print(f"{children}\n{expected}")
        for d in range(len(children)):
            self.assertAlmostEqual(children[d].x_pos, expected[d].x_pos)
            self.assertAlmostEqual(children[d].y_pos, expected[d].y_pos)

if __name__ == '__main__':
    unittest.main()
