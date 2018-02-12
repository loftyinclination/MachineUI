import sys
sys.path.append("..")
import argparse
import random
import math
from src.classes import Node
from PIL import Image, ImageDraw, ImageColor
from pathlib import Path

DEFAULT_MAX_AREA = [10, 10]
DEFAULT_MAX_LENGTH = 25

def main(cla):
    tree = [Node(None, 0.0, 0.0)]

    tree += tree[0].split(random.randrange(1, 4, 1), math.pi / 4, math.pi / 4, cla.length_long, cla.variance_long, straight=True)
    visited = {tree[0]: 0}

    choices = [
        lambda x: [3, math.pi, x[2], x[3], x[4]], 
        lambda x: [0, x[1], x[2], x[3], x[4]], 
        lambda x: [1, x[1], x[2], 0.1,  0],
        lambda x: x
    ]

    weights = _weights(cla.branching, 0, cla.ratio)

    default = [1, math.pi / 4, math.pi / 4, cla.length_long, cla.variance_long]

    while (_area(tree) < cla.area and sum(tree) < cla.length and set(tree) != set(visited)):
        if len(tree) >= 5:
            weights = _weights(cla.branching, cla.terminating, cla.ratio)
        
        for x in [x for x in tree if (x not in visited)]:
            choice = random.choices(range(len(choices)), weights=weights)[0] #index
            args = choices[choice](default)
            if cla.debug:
                print(f"currently splitting: x: {x.x_pos}, y: {x.y_pos}")
            tree += x.split(args[0], args[1], args[2], args[3], args[4], debug=cla.debug)
            visited[x] = choice

    print(f"terminated. reason: area: {_area(tree) < cla.area}, length: {sum(tree) < cla.length}, visited: {set(tree) != set(visited)}\n")
    
    draw(cla, visited)
    if cla.debug:
        for i in tree:
            print(str(i))

def _area(tree):
    x_values = [i.x_pos for i in tree]
    y_values = [i.y_pos for i in tree]
    return [max(x_values) - min(x_values), max(y_values) - min(y_values)]

def _weights(branching, terminating, ratio):
    return [
        branching,
        terminating, 
        (1 - (branching + terminating))         / (ratio + 1) if ratio != 0 else 0,
        (1 - (branching + terminating)) * ratio / (ratio + 1) if ratio != 0 else 1 - (branching + terminating)
    ]

def draw(cla, tree, scale=100, _width=2):
    area = tuple(int(x * scale) + 10 for x in _area(tree))
    im = Image.new('RGB', area) #convert type of area to tuple here - fewer checks
    draw = ImageDraw.Draw(im)
    smallest = Node(None, min([i.x_pos for i in tree]), min([i.y_pos for i in tree]))
    # print(f"bottom left is {smallest}")

    for x in tree:
        # print(f"drawing line from ({x.x_pos:.3}, {x.y_pos:.3}) to ({x.parent.x_pos:.3}, {x.parent.y_pos:.3})")

        if x.parent is not None:
            x = (x - smallest) * scale + (5, 5)
            x.parent = (x.parent - smallest) * scale + (5, 5)
            draw.line([x.pos(), x.parent.pos()], fill=0xffffff, width=_width)

    for x in tree:
        colour = [0x0000ff, 0x00ff00, 0xff0000, 0xff9000][tree[x]]
        x = (x - smallest) * scale + (5, 5)
        draw.ellipse([(x.x_pos - 0.5 * _width, x.y_pos - 0.5 * _width), (x.x_pos + 0.5 * _width, x.y_pos + 0.5 * _width)], fill=colour)

    print(f"splits {len([x for x in tree if tree[x] == 0])}, long {len([x for x in tree if tree[x] == 3])}, short {len([x for x in tree if tree[x] == 2])}, total {len(tree)}")

    del(draw)
    im = im.transpose(Image.FLIP_TOP_BOTTOM)
    
    filename = ""
    if cla.length != DEFAULT_MAX_LENGTH:
        filename = f"_{cla.length}"
    im.save(Path(f"img\\{cla.seed}{filename}.png", format="PNG"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Machine UI Generator')
    parser.add_argument('-a', '--area',        type=float, default=DEFAULT_MAX_AREA, nargs=2, help="max area encompassed")
    parser.add_argument('-L', '--length',      type=float, default=DEFAULT_MAX_LENGTH, help="max length of tree brances")
    parser.add_argument('-S', '--seed',        type=int,   default=random.randrange(2 ** 18))
    parser.add_argument('-D', '--debug',       action="store_true")

    choices = parser.add_argument_group('node choice probability')
    choices.add_argument('-b', '--branching',   type=float, default=0.1)
    choices.add_argument('-t', '--terminating', type=float, default=0.3)

    length = parser.add_argument_group('length settings', description='settings for the two different types of length_longs')
    length.add_argument('-r', '--ratio', type=float, default=4, help="ratio of long to short length_longs")
    length.add_argument('-ls', '--length-short',   type=float, default=0.1, dest="length_short")
    length.add_argument('-ll', '--length-long',    type=float, default=1.0, dest="length_long")
    length.add_argument('-vs', '--variance-short', type=float, default=0, dest="variance_short")
    length.add_argument('-vl', '--variance-long',  type=float, default=0, dest="variance_long")
    
    cla = parser.parse_args()

    print(f"seed {cla.seed}; length {cla.length_long}, length variance {cla.variance_long}")
    random.seed(cla.seed)

    main(cla)
