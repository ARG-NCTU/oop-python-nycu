import pytest
import add_path  # Ensure module path is correct
from lec8 import Coordinate, Fraction, intSet

def test_coordinate():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert c1.distance(c2) == 5.0  # (3^2 + 4^2) ** 0.5 = 5
    assert str(c1) == "<3,4>"
    assert c2.distance(c1) == 5.0
    c3 = Coordinate(-2, -2)
    assert c3.distance(c2) == 2.8284271247461903  # sqrt(8)

def test_fraction():
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b
    assert str(c) == "4/4"
    assert float(c) == 1.0
    d = a - b
    assert str(d) == "-2/4"
    assert float(d) == -0.5
    assert str(b.inverse()) == "4/3"
    assert float(b.inverse()) == 1.3333333333333333
    with pytest.raises(AssertionError):
        Fraction(3.14, 2.7)
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 0)

def test_intSet():
    s = intSet()
    assert str(s) == "{}"
    s.insert(3)
    s.insert(4)
    s.insert(3)  # Duplicate, should not add
    assert str(s) == "{3,4}"
    assert s.member(3) is True
    assert s.member(5) is False
    s.insert(6)
    assert str(s) == "{3,4,6}"
    s.remove(3)
    assert str(s) == "{4,6}"
    with pytest.raises(ValueError, match="3 not found"):
        s.remove(3)
