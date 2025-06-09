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

def test_init_and_str():
    f = lc.Fraction(3, 5)
    assert f.num == 3
    assert f.denom == 5
    assert str(f) == "3/5"

def test_addition():
    a = lc.Fraction(1, 4)
    b = lc.Fraction(3, 4)
    result = a + b
    assert result.num == 16
    assert result.denom == 16
    assert str(result) == "16/16"

def test_subtraction():
    a = lc.Fraction(3, 4)
    b = lc.Fraction(1, 4)
    result = a - b
    assert result.num == 8
    assert result.denom == 16
    assert str(result) == "8/16"


def test_invalid_init():
    with pytest.raises(AssertionError):
        lc.Fraction("a", 5)
    with pytest.raises(AssertionError):
        lc.Fraction(1, "b")
    with pytest.raises(AssertionError):
        lc.Fraction(1.5, 2)

def test_mixed_operations():
    a = lc.Fraction(1, 3)
    b = lc.Fraction(2, 5)
    add = a + b
    sub = a - b
    assert str(add) == "11/15"
    assert str(sub) == "-1/15"