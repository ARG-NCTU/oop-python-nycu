
#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
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

def test_Fraction():
    b = Fraction(3, 4)
    a = Fraction(1, 2)
    c = a + b
    assert str(c) == "10/8"
    assert float(c) == 1.25
    d = b - a
    assert str(d) == "2/8"
    assert float(d) == 0.25
    e = b.inverse()
    assert str(e) == "4/3"
    assert float(e) == 1.3333333333333333
a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))

# try:
#     c = Fraction(3.14,2.7)
#     print(error)
# except AssertionError:
#     print (passed)
##c = Fraction(3.14, 2.7) # assertion error
##print a*b # error, did not define how to multiply two Fraction objects

