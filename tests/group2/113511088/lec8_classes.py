# -*- coding: utf-8 -*-
"""
lec8_classes_113511088.py
Classes: Coordinate, Fraction, intSet
"""

class Coordinate(object):
    """A coordinate made up of an x and y value"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def distance(self, other):
        """Returns the euclidean distance between two points"""
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


class Fraction(object):
    """A number represented as a fraction"""
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int, "ints not used"
        assert denom != 0, "denom cannot be 0"
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        top = self.num * other.denom - self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __float__(self):
        return self.num / self.denom

    def inverse(self):
        """Returns a new fraction representing 1/self"""
        assert self.num != 0, "cannot invert a zero fraction"
        return Fraction(self.denom, self.num)


class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Removes e from self; raises ValueError if e not in self"""
        try:
            self.vals.remove(e)
        except Exception:
            raise ValueError(str(e) + " not found")

    def __str__(self):
        self.vals.sort()
        return "{" + ",".join([str(e) for e in self.vals]) + "}"


if __name__ == "__main__":
    # Demo (optional)
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    print(c1, "distance to", c2, "=", c1.distance(c2))

    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b
    print("a+b =", c, "float =", float(c))
    print("inverse(b) =", b.inverse(), "float =", float(b.inverse()))

    s = intSet()
    s.insert(3); s.insert(4); s.insert(3)
    print("set:", s)
