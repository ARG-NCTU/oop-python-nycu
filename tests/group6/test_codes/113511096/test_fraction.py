import math

class Fraction(object):
    """ A number represented as a fraction """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        assert denom != 0, "Denominator cannot be zero"
        self.num = num
        self.denom = denom

    def __str__(self):
        """ Returns a string representation of self """
        return str(self.num) + "/" + str(self.denom)

    def reduce(self):
        """ Reduces the fraction using the greatest common divisor """
        common = math.gcd(self.num, self.denom)
        self.num //= common
        self.denom //= common
        return self

    def __add__(self, other):
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott).reduce()

    def __sub__(self, other):
        top = self.num * other.denom - self.denom * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott).reduce()

    def __mul__(self, other):
        """ Multiplies two fractions """
        return Fraction(self.num * other.num, self.denom * other.denom).reduce()

    def __truediv__(self, other):
        """ Divides self by other fraction """
        return Fraction(self.num * other.denom, self.denom * other.num).reduce()

    def __float__(self):
        return self.num / self.denom

    def inverse(self):
        return Fraction(self.denom, self.num)

# --- Pytest Functions ---

def test_Fraction_math():
    a = Fraction(1, 2)
    b = Fraction(3, 4)
    
    # Test Addition (1/2 + 3/4 = 10/8 -> 5/4)
    c = a + b
    assert str(c) == "5/4"
    
    # Test Multiplication (1/2 * 3/4 = 3/8)
    d = a * b
    assert str(d) == "3/8"
    
    # Test Division (1/2 / 3/4 = 4/6 -> 2/3)
    e = a / b
    assert str(e) == "2/3"

def test_Fraction_reduction():
    f = Fraction(10, 8)
    f.reduce()
    assert str(f) == "5/4"

def test_Fraction_errors():
    import pytest
    with pytest.raises(AssertionError):
        Fraction(3.14, 2.7)