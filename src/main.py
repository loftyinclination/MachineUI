import argparse
from src.classes import Node

def main(area):
    tree = [Node(None, 0, 0)]
    tree[0]        

def _area(tree):
    x_values = [i.x_pos for i in tree]
    y_values = [i.y_pos for i in tree]
    return [max(x_values) - min(x_values), max(y_values) - min(y_values)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Machine UI Generator')
    parser.add_argument('-a', '--area', nargs=2, type=float)
    parser.add_argument('-S', '--seed')
    parser.add_argument('-b', '--branching', default=0.3)
    parser.add_argument('-r', '--ratio', default=7)
    cla = parser.parse_args()

    print(cla.area)
    main(area)
