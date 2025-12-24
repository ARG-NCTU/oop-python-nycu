

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
    
    
def test_Fraction_comprehensive():
    # 1. 基礎初始化與字串測試
    f1 = Fraction(1, 2)
    assert str(f1) == "1/2"
    assert float(f1) == 0.5

    # 2. 加法測試 (__add__)
    # 邏輯: (1*4 + 2*3) / (2*4) = 10 / 8
    # 


    f2 = Fraction(3, 4)
    f3 = f1 + f2 
    assert str(f3) == "10/8" 
    assert float(f3) == 1.25

    # 3. 減法測試 (__sub__)
    # 邏輯: (3*2 - 4*1) / (4*2) = 2 / 8
    f4 = f2 - f1
    assert str(f4) == "2/8"
    assert float(f4) == 0.25

    # 4. 倒數測試 (inverse)
    inv = f2.inverse()
    assert str(inv) == "4/3"
    assert float(inv) == 3/4  # 0.75

    # 5. 負數與零的測試
    neg = Fraction(-1, 2)
    assert str(neg) == "-1/2"
    
    # 負數加法: (-1*2 + 2*1) / (2*2) = 0 / 4
    zero_res = neg + f1 
    assert str(zero_res) == "0/4"
    assert float(zero_res) == 0.0