import pytest
from lec8_classes import Coordinate, Fraction, intSet

def test_coordinate():
    c = Coordinate(3, 4)
    origin = Coordinate(0, 0)
    assert str(c) == "<3,4>"
    assert c.distance(origin) == 5.0
    assert origin.distance(c) == 5.0

def test_fraction():
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b
    assert str(c) == "16/16"
    assert float(c) == pytest.approx(1.0)
    assert float(b.inverse()) == pytest.approx(4/3)
    with pytest.raises(AssertionError):
        Fraction(3.14, 2)

def test_intSet():
    s = intSet()
    assert str(s) == "{}"
    s.insert(3)
    s.insert(4)
    s.insert(3)
    assert str(s) == "{3,4}"
    assert s.member(3)
    assert not s.member(5)
    s.insert(6)
    assert str(s) == "{3,4,6}"
    s.remove(3)
    assert str(s) == "{4,6}"
    with pytest.raises(ValueError):
        s.remove(3)
