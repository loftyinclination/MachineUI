import math
import random

class Node(object):

    def __init__(self, parent, x_pos, y_pos):
        self.parent = parent
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.children = []

    def __repr__(self):
        return f"Node({self.parent}, {self.x_pos}, {self.y_pos})"

    def add_child(self, new_child):
        self.children.append(new_child)

    @property
    def children(self):
        return self.children

    def get_direction(self):
        if self.parent is None:
            return None
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

    def split(self, children, angle, angle_step, length, length_var):
        """produce {children} new nodes, with {self} as parent
           angle: +ve max value of angle from current direction.
           angle_step: angle can have values of n * angle_step
           returns new children as a list"""
        steps = int(math.pi / angle_step)
        angles = [n * angle_step for n in range(-steps, steps) if abs(n * angle_step) <= angle]
        # print(angles)
        new_children = []

        for _ in range(children):
            new_child = Node(self, None, None)

            new_direction = random.choice(angles)
            new_length = random.gauss(length, length_var)
            angles.remove(new_direction)

            new_child.set_position_polar(new_length, new_direction)
            self.add_child(new_child)
            new_children.append(new_child)

        return new_children
