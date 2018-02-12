import sys
sys.path.append("..")
import unittest
import math
from src.classes import Node

class classes_Test(unittest.TestCase):

    def test_equality(self):
        centre = Node(None, 0, 0)
        c1 = Node(centre, math.cos(math.pi / 2), math.sin(math.pi / 2))
        n1 = Node(centre, 0, 1)
        self.assertEqual(c1, n1)

        c2 = Node(centre, math.cos(0), math.sin(0))
        n2 = Node(centre, 1, 0)
        self.assertEqual(c2, n2)

    def test_addition(self):
        centre = Node(None, 0, 0)
        self.assertEqual(Node(None, 1, 1), centre + Node(None, 1, 1))

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
    
    def test_split_short_args(self):
        # args = lambda x: [1, x[1], x[2], 0.1,  0]
        # default = [1, math.pi / 4, math.pi / 4, cla.length_long, cla.variance_long]
        centre = Node(Node(None, 0, 0), 1, 1)
        for i in range(3, 9):
            self.assertRaises(IndexError, centre.split, i, math.pi / 4, math.pi / 4, 0.1, 0, straight=False)
        
        self.assertSetEqual(set(centre.split(2, math.pi / 4, math.pi / 4, 0.1, 0, straight=False)), set([Node(centre, 1.1, 1), Node(centre, 1, 1.1)]))

if __name__ == '__main__':
    unittest.main()
