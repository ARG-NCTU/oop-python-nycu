# === Coordinate 類別 ===
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x},{self.y}>"

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


# === Fraction 類別 ===
class Fraction(object):
    def __init__(self, num, denom):
        assert isinstance(num, int) and isinstance(denom, int), "ints not used"
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


# === intSet 類別 ===
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
            raise ValueError(f"{e} not found")

    def __str__(self):
        self.vals.sort()
        return '{' + ','.join(str(e) for e in self.vals) + '}'
    
# === Tests ===
def test_coordinate():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert str(c1) == "<3,4>"
    assert c1.distance(c2) == 5.0
    assert c2.distance(c1) == 5.0

def test_fraction():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    assert str(f1) == "1/2"
    assert str(f2) == "1/3"
    assert str(f1 + f2) == "5/6"
    assert str(f1 - f2) == "1/6"
    assert float(f1) == 0.5
    assert float(f2) == 0.3333333333333333
    assert str(f1.inverse()) == "2/1"
def test_intSet():
    s = intSet()
    s.insert(3)
    s.insert(1)
    s.insert(2)
    assert str(s) == "{1,2,3}"
    assert s.member(2) is True
    assert s.member(4) is False
    s.remove(2)
    assert str(s) == "{1,3}"
    try:
        s.remove(4)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "4 not found"
def test_all():
    test_coordinate()
    test_fraction()
    test_intSet()