#################
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

# Test code for Coordinate
def test_Coordinate():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert c1.distance(c2) == 5.0  # (3^2 + 4^2) ** 0.5 = 5
    assert str(c1) == "<3,4>"
    print("Coordinate class tests passed.")

test_Coordinate()


#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
    """ A number represented as a fraction """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Returns a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

# Test code for Fraction
def test_Fraction():
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b
    assert str(c) == "16/16"
    assert float(c) == 1.0
    assert float(b.inverse()) == 4/3

    try:
        c = Fraction(3.14, 2.7)
        print("Should not reach here")
    except AssertionError:
        print("Fraction class tests passed.")

test_Fraction()


##############
## EXAMPLE: a set of integers as class
##############
class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals = []

    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """ Assumes e is an integer
        Returns True if e is in self, and False otherwise """
        return e in self.vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

# Test code for intSet
def test_intSet():
    s = intSet()
    assert str(s) == "{}"  # 初始集合應該是空的

    s.insert(3)
    s.insert(4)
    s.insert(3)  # 重複插入應該無效
    assert str(s) == "{3,4}"

    assert s.member(3) is True
    assert s.member(5) is False

    s.insert(6)
    assert str(s) == "{3,4,6}"

    s.remove(3)
    assert str(s) == "{4,6}"

    try:
        s.remove(3)  # 應該拋出 ValueError
    except ValueError as e:
        assert str(e) == "3 not found"

    print("intSet class tests passed.")

test_intSet()
print("\n==== Custom Tests ====")

# Coordinate 類別測試
def test_coordinate_custom():
    p1 = Coordinate(-1, -1)
    p2 = Coordinate(2, 3)
    assert str(p1) == "<-1,-1>"
    assert str(p2) == "<2,3>"
    assert round(p1.distance(p2), 5) == round(((3**2 + 4**2)**0.5), 5)  # 距離應該是 5.0

test_coordinate_custom()
print("Coordinate custom test passed.")

# Fraction 類別測試
def test_fraction_custom():
    f1 = Fraction(2, 5)
    f2 = Fraction(1, 10)
    sum_f = f1 + f2  # 應該是 5/10 = 1/2
    diff_f = f1 - f2  # 應該是 3/10
    assert str(sum_f) == "25/50"
    assert str(diff_f) == "15/50"
    assert round(float(sum_f), 5) == 0.5
    assert round(float(diff_f), 5) == 0.3
    assert str(f1.inverse()) == "5/2"

test_fraction_custom()
print("Fraction custom test passed.")

# intSet 類別測試
def test_intset_custom():
    s = intSet()
    s.insert(10)
    s.insert(-5)
    s.insert(0)
    assert str(s) == "{-5,0,10}"
    assert s.member(-5)
    s.remove(-5)
    assert str(s) == "{0,10}"
    try:
        s.remove(-5)
    except ValueError as e:
        assert str(e) == "-5 not found"

test_intset_custom()
print("intSet custom test passed.")
