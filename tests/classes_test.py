import sys
sys.path.append("..")
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
        centre = Node(None, 0, 0)
        children = sorted(centre.split(3, math.pi / 4, math.pi / 4, 1, 0, straight=True), key=lambda node: node.get_direction())
        expected = [Node(centre, 1.0, 0.0), Node(centre, 1 / math.sqrt(2), 1 / math.sqrt(2)), Node(centre, 0.0, 1.0)]
        # print(f"{children}\n{expected}")
        for d in range(len(children)):
            self.assertAlmostEqual(children[d].x_pos, expected[d].x_pos)
            self.assertAlmostEqual(children[d].y_pos, expected[d].y_pos)

    def test_split_parent_full(self):
        centre = Node(Node(None, 0, 0), 1, 0)
        children = sorted(centre.split(6, math.pi, math.pi / 4, 1, 0, straight=False), key=lambda node: node.get_direction())
        x1 = 1 - math.sqrt(2)
        x2 = 1 + math.sqrt(2)
        y  =     math.sqrt(2)
        expected = [
            Node(centre, x1,  y),
            Node(centre, 1,   1),
            Node(centre, x2,  y),
            Node(centre, x2, -y),
            Node(centre, 1,  -1),
            Node(centre, x2, -y)
        ]

if __name__ == '__main__':
    unittest.main()
