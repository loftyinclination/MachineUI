import argparse
import random
import math
from classes import Node

def main(area, length, length_var):
    tree = [Node(None, 0, 0)]

    num_children_l_1 = random.randrange(1, 3, 1)
    print(num_children_l_1)
    tree += tree[0].split(num_children_l_1, math.pi / 4, math.pi / 4, length, length_var)
    print(tree)

def _area(tree):
    x_values = [i.x_pos for i in tree]
    y_values = [i.y_pos for i in tree]
    return [max(x_values) - min(x_values), max(y_values) - min(y_values)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Machine UI Generator')
    parser.add_argument('-a', '--area', nargs=2, type=float, default=[10, 10])
    parser.add_argument('-S', '--seed', default=random.randrange(2**16))
    parser.add_argument('-b', '--branching', default=0.3)
    parser.add_argument('-r', '--ratio', default=7)
    parser.add_argument('-l', '--length', default=1)
    parser.add_argument('-v', '--lengthvar', default=0.6)
    cla = parser.parse_args()

    print(f"seed {cla.seed}; length {cla.length}, length variance {cla.lengthvar}")
    random.seed(cla.seed)

    main(cla.area, cla.length, cla.lengthvar)
