import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def multiply(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def divide(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def set_magnitude(self, magnitude):
        return self.normalize().multiply(Point(magnitude, magnitude))

    def normalize(self):
        if not self.is_zero():
            m = self.get_magnitude()
            self.x /= m
            self.y /= m
        return self

    def is_zero(self):
        return self.x == 0 and self.y == 0

    def get_magnitude(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def distance2(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return dx**2 + dy**2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y