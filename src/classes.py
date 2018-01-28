import math

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

    def get_children(self):
        return self.children

    def get_direction(self):
        if self.parent is None:
            return None
        else:
            theta = math.atan((self.parent.y_pos - self.y_pos) / (self.parent.x_pos - self.x_pos))
            # print(f"theta {theta}, p.x {self.parent.x_pos}, x {self.x_pos}, p.y {self.parent.y_pos}, y {self.y_pos}")
            if (self.parent.x_pos > self.x_pos) and (self.parent.y_pos < self.y_pos):
                return math.pi + theta
            elif (self.parent.x_pos > self.x_pos) and (self.parent.y_pos > self.y_pos):
                return math.pi + theta
            elif (self.parent.x_pos < self.x_pos) and (self.parent.y_pos > self.y_pos):
                return math.pi * 2 + theta
            return theta
