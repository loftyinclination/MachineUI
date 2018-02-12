import math
import random
import numbers

class Node(object):

    def __init__(self, parent, x_pos, y_pos):
        self.parent = parent
        self.x_pos = float(x_pos)
        self.y_pos = float(y_pos)
        self.children = []
        self.PRECISION = 12

    def __repr__(self):
        return f"Node({self.parent}, {self.x_pos}, {self.y_pos})"

    def __str__(self):
        if self.parent is None:
            return f"Node(None, {self.x_pos:.4}, {self.y_pos:.4})"
        else:
            return f"Node(Node({self.parent.x_pos:.4}, {self.parent.y_pos:.4}), {self.x_pos:.4}, {self.y_pos:.4})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.parent == other.parent and round(self.x_pos - other.x_pos, self.PRECISION) == 0 and round(self.y_pos - other.y_pos, self.PRECISION) == 0

    def __ne__(self, other):
        return not isinstance(other, self__class__) and self.parent != other.parent and round(self.x_pos - other.x_pos, self.PRECISION) != 0 and round(self.y_pos - other.y_pos, self.PRECISION) != 0

    def __hash__(self):
        return hash((round(self.x_pos, self.PRECISION), round(self.y_pos, self.PRECISION), hash(self.parent)))

    def __add__(self, other):
        if type(other) == tuple:
            return Node(self.parent, self.x_pos + other[0], self.y_pos + other[1])
        elif isinstance(other, self.__class__):
            return Node(self.parent, self.x_pos + other.x_pos, self.y_pos + other.y_pos)
        elif isinstance(other, numbers.Number):
            return abs(self) + other
        else:
            raise TypeError
    
    def __radd__(self, other):
        if isinstance(other, numbers.Number):
            return abs(self) + other
        else:
            raise TypeError

    def __sub__(self, other):
        if type(other) == tuple:
            return Node(self.parent, self.x_pos - other[0], self.y_pos - other[1])
        elif type(other) == Node:
            return Node(self.parent, self.x_pos - other.x_pos, self.y_pos - other.y_pos)
        else:
            raise TypeError

    def __mul__(self, coef):
        if isinstance(coef, numbers.Number):
            return Node(self.parent, self.x_pos * coef, self.y_pos * coef)
        else:
            raise TypeError

    def __abs__(self):
        if self.parent is None:
            return 0
        else:
            return math.sqrt((self.x_pos - self.parent.x_pos) ** 2 + (self.y_pos - self.parent.y_pos) ** 2)

    def pos(self):
        return (self.x_pos, self.y_pos)

    def add_child(self, new_child):
        self.children.append(new_child)

    def get_direction(self):
        if self.parent is None:
            return None
        elif (self.parent.x_pos == self.x_pos):
            if (self.parent.y_pos > self.y_pos):
                return math.pi * 0.5
            else:
                return math.pi * 1.5    
        else:
            theta = math.atan((self.parent.y_pos - self.y_pos) / (self.parent.x_pos - self.x_pos))
            # print(f"theta {theta},
            #       p.x {self.parent.x_pos}, x {self.x_pos},
            #       p.y {self.parent.y_pos}, y {self.y_pos}")
            if (self.parent.x_pos > self.x_pos) and (self.parent.y_pos < self.y_pos):
                return math.pi + theta
            elif (self.parent.x_pos > self.x_pos) and (self.parent.y_pos > self.y_pos):
                return math.pi + theta
            elif (self.parent.x_pos < self.x_pos) and (self.parent.y_pos > self.y_pos):
                return math.pi * 2 + theta
            return theta

    def set_position_polar(self, norm, theta):
        parent_theta = self.parent.get_direction()
        if parent_theta is None:
            parent_theta = math.pi / 4
        self.x_pos = self.parent.x_pos + (norm * math.cos(theta + parent_theta))
        self.y_pos = self.parent.y_pos + (norm * math.sin(theta + parent_theta))

    def split(self, children, angle, angle_step, length, length_var, straight=False):
        """produce {children} new nodes, with {self} as parent
           angle: +ve max value of angle from current direction.
           angle_step: angle can have values of n * angle_step
           returns new children as a list"""
        steps = int(math.pi / angle_step)

        # angle_mag = [n / steps for n in range(-steps, steps) if straight or (n != 0 or n != steps)]
        # angles = [n * math.pi for n in angle_mag if abs(n * math.pi) <= angle]
        angles = [n * math.pi / steps for n in range(-steps, steps) if (straight or (n != 0 and n != steps)) and (abs(n * math.pi / steps) <= angle)]
        # print(angles)

        new_children = []

        for _ in range(children):
            new_child = Node(self, 0, 0)

            new_direction = random.choice(angles)
            new_length = random.gauss(length, length_var)
            angles.remove(new_direction)

            new_child.set_position_polar(new_length, new_direction)
            self.add_child(new_child)
            new_children.append(new_child)

        return new_children
