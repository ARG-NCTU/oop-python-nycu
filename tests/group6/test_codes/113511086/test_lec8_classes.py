import math

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return math.sqrt(x_diff_sq + y_diff_sq)

    def __str__(self):
        return f"<{self.x},{self.y}>"


class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __float__(self):
        return self.num / self.den

    def inverse(self):
        return Fraction(self.den, self.num)


class intSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)
            self.vals.sort()

    def member(self, e):
        return e in self.vals

    def __str__(self):
        result = '{'
        for i in range(len(self.vals)):
            result += str(self.vals[i])
            if i != len(self.vals) - 1:
                result += ','
        result += '}'
        return result
