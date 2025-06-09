import pytest

class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Retunrs a string representation of self """
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
    
def test_fraction():
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b  # c is a Fraction object
    assert str(c) == "1/1", f"Expected '1/1', got '{c}'"
    assert float(c) == 1.0, f"Expected 1.0, got {float(c)}"
    assert Fraction.__float__(c) == 1.0, f"Expected 1.0, got {Fraction.__float__(c)}"
    assert float(b.inverse()) == 4/3, f"Expected 4/3, got {float(b.inverse())}"