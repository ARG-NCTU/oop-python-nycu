#################
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):   ## Python 會把 self 當作是一個物件的參考，指向這個物件
                                ## self 之後的參數都是構件這個物件時所需要的參數
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):      ##when print the object, it will what this function return
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):      ##note that other objects can also be parameter in an object
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
##不管在物件內或物件外呼叫其中包含self參數的函數時，都不需要在參數的地方打上該物件的名子
test = Coordinate(6, 8)
print(test)
print(Coordinate(1,2)) 
oot = Coordinate(0, 0)
print(test.distance(oot))

def Coordinate_test():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert c1.distance(c2) == 5.0  # (3^2 + 4^2) ** 0.5 = 5
    assert str(c1) == "<3,4>"   ##goto to __str__ function


Coordinate_test()
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x, origin.x)
print(c.distance(origin))
print(Coordinate.distance(c, origin))##這裡的c是Coordinate的物件，origin也是Coordinate的物件
print(origin.distance(c))
print(c)


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
        return Fraction(top, bott)  ##return the value in the form of Fraction
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __mul__(self, other):
        """ Returns a float value of the fraction """
        num = self.num * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
d = a - b
e = a * b
print(c)
print(d)
print(e)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))

# try:\
##     c = Fraction(3.14,2.7)
#     print(error)
# except AssertionError:
#     print (passed)
##c = Fraction(3.14, 2.7) # assertion error
##print a*b # error, did not define how to multiply two Fraction objects


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
        if e not in self.vals:
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
            ##[str(e) for e in self.vals]
            ##這是一個 list comprehension（串列推導式）：
            ##把 self.vals 裡的每個元素 e 轉成字串 → str(e)
            ##結果會變成一個字串組成的 list
            ##例如：如果 self.vals = [1, 2, 3]，那這部分就會得到 ['1', '2', '3']

            ##','.join(...)
            ##這是 字串方法 join()，會把 list 中的字串用 , 串起來。
            ##','.join(['1', '2', '3']) → '1,2,3'



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

