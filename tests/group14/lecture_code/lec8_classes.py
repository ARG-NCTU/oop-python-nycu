"""
lec8_classes.py

此檔提供數個教學用類別及簡單範例：
- `Coordinate`：二維座標類別，示範建構子、字串表示與計算歐氏距離。
- `Fraction`：分數類別，示範 operator overloading（加、減、轉為浮點數、求倒數）。
- `intSet`：簡單整數集合類別，示範集合插入、成員查詢、刪除與字串化表示。

檔中包含少量示範與斷言（教學用），不會對外暴露其他副作用函式。
"""

#################
# 範例：簡單的 Coordinate 類別（中文說明）
#################
class Coordinate(object):
    """二維座標：包含 x, y 屬性。

    方法說明：
    - __init__(x, y): 建構子，設定 x 與 y。
    - __str__(): 回傳 '<x,y>' 的字串表示，方便列印與除錯。
    - distance(other): 回傳與另一座標的歐氏距離。
    """
    def __init__(self, x, y):
        """設定 x 與 y 的初始值。"""
        self.x = x
        self.y = y
    def __str__(self):
        """回傳字串表示（例如 '<3,4>'）。"""
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """計算並回傳 self 與 other 之間的歐氏距離。"""
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

def Coordinate_test():
    # 測試 Coordinate 的基本行為與方法
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    # 3-4-5 右三角形，距離應為 5
    assert c1.distance(c2) == 5.0  # (3^2 + 4^2) ** 0.5 = 5
    assert str(c1) == "<3,4>"

# 範例用法（可取消註解以手動測試）
# Coodinate test()
# c = Coordinate(3,4)
# origin = Coordinate(0,0)
# print(c.x, origin.x)
# print(c.distance(origin))
# print(Coordinate.distance(c, origin))
# print(origin.distance(c))
# print(c)


#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
    """分數類別（num/denom）。

    示範：
    - 透過 operator overloading 支援 `+` 與 `-`，並能轉為浮點數 (`float()`)。
    - `inverse()` 回傳分子與分母互換的新分數。
    - 目前未實作約分（reduce）或乘除法，作為練習題。
    """
    def __init__(self, num, denom):
        """num 和 denom 應為整數（assert 檢查）。"""
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    def __str__(self):
        """回傳分數的字串表示，例如 '1/4'。"""
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other):
        """回傳兩分數相加後的新 Fraction 物件。"""
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __sub__(self, other):
        """回傳兩分數相減後的新 Fraction 物件。"""
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    def __float__(self):
        """將分數轉為浮點數值。"""
        return self.num/self.denom
    def inverse(self):
        """回傳 1/self 的分數表示（分子/分母互換）。"""
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))

# 範例：測試輸入型別檢查（未通過的情況會觸發 AssertionError）
# try:
#     c = Fraction(3.14,2.7)
#     print(error)
# except AssertionError:
#     print (passed)
##c = Fraction(3.14, 2.7) # assertion error
##print a*b # error, did not define how to multiply two Fraction objects


##############
## EXAMPLE: a set of integers as class
##############
class intSet(object):
    """簡單的整數集合類別（教學用）。

    實作細節：集合以 list `self.vals` 儲存，確保每個整數只出現一次。
    方法：
    - insert(e): 插入元素（若尚未存在）。
    - member(e): 回傳是否為成員。
    - remove(e): 移除元素，若不存在則拋出 ValueError。
    - __str__(): 將集合排序並回傳 '{a,b,c}' 的字串表示。
    注意：這只是示範，效能不如使用內建 `set`。
    """
    def __init__(self):
        """建立空集合。"""
        self.vals = []

    def insert(self, e):
        """假設 e 為整數，若尚未存在則加入集合。"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """檢查 e 是否為集合成員。"""
        return e in self.vals

    def remove(self, e):
        """移除元素 e；若不存在則拋出 ValueError。"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """回傳排序後的集合字串表示，例如 '{3,4,6}'。"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

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

"""
s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.insert(6)
print(s)
#s.remove(3)  # leads to an error
print(s)
s.remove(3)
"""
