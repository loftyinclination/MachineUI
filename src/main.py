import argparse
import random
import math
from classes import Node

def main(cla):
    tree = [Node(None, 0, 0)]

    tree += tree[0].split(random.randrange(1, 4, 1), math.pi / 4, math.pi / 4, cla.length, cla.l_var, straight=True)
    visited = [tree[0]]

    while (_area(tree) < cla.area):
        weights = [cla.branching,
                   cla.terminating, 
                   (1 - (cla.branching + cla.terminating))             / (cla.ratio + 1),
                   (1 - (cla.branching + cla.terminating)) * cla.ratio / (cla.ratio + 1)]
        
        for x in [x for x in tree if x not in visited]:
            default = [1, math.pi, math.pi / 4, cla.length, cla.l_var]
            default = random.choices([lambda x: [3, x[1], x[2], x[3], x[4]], 
                                      lambda x: [0, x[1], x[2], x[3], x[4]], 
                                      lambda x: [1, x[1], x[2], 0.1,  0],
                                      lambda x: x], weights=weights)[0](default)
            # print(default)
            tree += x.split(default[0], default[1], default[2], default[3], default[4])
            visited.append(x)

        print(tree)
        exit()

def _area(tree):
    x_values = [i.x_pos for i in tree]
    y_values = [i.y_pos for i in tree]
    return [max(x_values) - min(x_values), max(y_values) - min(y_values)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Machine UI Generator')
    parser.add_argument('-a', '--area', nargs=2, type=float, default=[10, 10])
    parser.add_argument('-S', '--seed', default=random.randrange(2**16))
    parser.add_argument('-b', '--branching', default=0.1)
    parser.add_argument('-t', '--terminating', default=0.3)
    parser.add_argument('-r', '--ratio', default=7, help="ratio of long to short segments")
    parser.add_argument('-l', '--length', default=1)
    parser.add_argument('-v', '--length-var', default=0.6, dest="l_var")
    cla = parser.parse_args()

    print(f"seed {cla.seed}; length {cla.length}, length variance {cla.l_var}")
    random.seed(cla.seed)

    main(cla)
