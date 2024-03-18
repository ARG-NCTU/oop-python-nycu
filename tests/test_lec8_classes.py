import add_path
import mit_ocw_exercises.lec8_classes as lc

def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.str == "<3, 4>" #3 updated str method
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5

def test_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)

def test_3_Fraction():
    p = lc.Fraction(7, 8)
    assert p.num == 7
    assert p.denom == 8
    assert p.__str__() == '7/8'
    assert p.__add__(lc.Fraction(1, 2)).__str__() == '15/16'
    assert p.__sub__(lc.Fraction(1, 2)).__str__() == '3/8'
    assert p.__float__() == 0.875
    assert p.inverse().__str__() == '8/7'
