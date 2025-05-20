import add_path
import lec8 as lc
import pytest


def test_coordinate_basic():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0, 0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
    

def test_coordinate_advanced():
    c1 = lc.Coordinate(5, 12)
    c2 = lc.Coordinate(9, 40)
    origin = lc.Coordinate(0, 0)
    assert c1.distance(origin) == 13
    assert c2.distance(origin) == 41

def test_intset_basic():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)

def test_intset_varied():
    s = lc.intSet()
    s.insert(8)
    s.insert(7)
    assert s.member(8)
    assert s.member(7)
    s.remove(8)
    assert not s.member(8)
    assert s.member(7)

def test_fraction_operations():
    p = lc.Fraction(2, 5)
    q = lc.Fraction(1, 5)
    assert p.num == 2 and p.denom == 5
    assert str(p + q) == "15/25"
    assert str(p - q) == "5/25"
    assert float(p) == 0.4
    assert str(p.inverse()) == "5/2"

def test_fraction_misc():
    a = lc.Fraction(1, 2)
    b = lc.Fraction(1, 4)
    result = a + b
    assert result.num == 6
    assert result.denom == 8
    assert float(a) == 0.5
    assert str(a) == "1/2"


if __name__ == "__main__":
    test_coordinate_basic()
    test_intset_basic()
    test_fraction_operations()
    print("Basic tests passed.")
