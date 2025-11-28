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

def Coordinate_test():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert c1.distance(c2) == 5.0  # (3^2 + 4^2) ** 0.5 = 5
    assert str(c1) == "<3,4>"

# Coodinate test()
# c = Coordinate(3,4)
# origin = Coordinate(0,0)
# print(c.x, origin.x)
# print(c.distance(origin))
# print(Coordinate.distance(c, origin))
# print(origin.distance(c))
# print(c)


def test_Coordinate_comprehensive():
    # 1. 基礎初始化與屬性測試
    c1 = Coordinate(3, 4)
    assert c1.x == 3
    assert c1.y == 4
    
    # 2. 字串表現形式 (__str__) 測試
    assert str(c1) == "<3,4>"
    assert str(Coordinate(0, 0)) == "<0,0>"
    assert str(Coordinate(-1, -2)) == "<-1,-2>"

    # 3. 距離計算測試 (Distance) - 快樂路徑
    origin = Coordinate(0, 0)
    assert c1.distance(origin) == 5.0
    
    # 4. 距離計算測試 - 對稱性 (A 到 B 等於 B 到 A)
    c2 = Coordinate(6, 8) # 與 (3,4) 距離應為 5
    assert c1.distance(c2) == 5.0
    assert c2.distance(c1) == 5.0

    # 5. 負數座標測試
    neg = Coordinate(-3, -4)
    assert neg.distance(origin) == 5.0
    
    # 6. 自我距離測試 (應為 0)
    assert c1.distance(c1) == 0.0

    # 7. 浮點數坐標測試 (使用近似值比較，避免浮點數精度問題)
    # 雖然你的範例直接用 ==，但在處理非整數結果時，建議考慮這類邊界
    c_float = Coordinate(1.5, 2.5)
    assert c_float.x == 1.5