import lec8_classes as lec
from lec8_classes import Coordinate
import pytest

def test_coordinate():
    a0 = Coordinate(0, 0)
    a1 = Coordinate(5, 12)
    a2 = Coordinate(6, 8)
    assert a1.x == 5 and a1.y == 12
    assert a2.x == 6 and a2.y == 8
    assert a1.distance(a0) == 13
    assert a2.distance(a0) == 10

def test_fraction():
    b1 = lec.Fraction(3, 4)
    b2 = lec.Fraction(1, 4)
    c = b1 + b2
    assert float(c) == 1.0
    assert lec.Fraction.__float__(c) == 1.0
    assert float(b1.inverse()) == 4/3
    with pytest.raises(AssertionError):
        lec.Fraction(3.14, 2.7)

def test_intset():
    s = lec.intSet()
    assert str(s) == "{}"
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(3)
    assert str(s) == "{1,2,3}"
    assert s.member(3) is True
    assert s.member(5) is False
    s.remove(1)
    assert str(s) == "{2,3}"
    with pytest.raises(ValueError, match="1 not found"):
        s.remove(1)