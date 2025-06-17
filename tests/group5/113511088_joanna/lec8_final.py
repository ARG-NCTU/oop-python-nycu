class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x},{self.y}>"

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom

    def __str__(self):
        return f"{self.num}/{self.denom}"

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
        return Fraction(self.denom, self.num)


class intSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
