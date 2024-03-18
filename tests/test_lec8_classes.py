import add_path
import mit_ocw_exercises.lec8_classes as lc
import pytest

def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
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
    p = lc.Fraction(2, 5)
    assert p.num == 2
    assert p.denom == 5
    q = lc.Fraction(1, 5)
    assert q.num == 1
    assert q.denom == 5
    a1 = p + q
    assert str(a1) == "15/25"
    a2 = p - q
    assert str(a2) == "5/25"
    assert lc.Fraction.__float__(p) == 0.4
    assert str(p.inverse()) == "5/2"

if __name__ == "__main__":
    test_coordinate()
    print("test_coordinate passed")
    test_intset()
    print("test_intset passed")
    test_3_Fraction()
    print("test_3_Fraction passed")
    print("All tests passed")
