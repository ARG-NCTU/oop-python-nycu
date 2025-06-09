import add_path
from mit_ocw_exercises.lec8_classes import Coordinate, Fraction, intSet
import math
import pytest

def test_Coordinate():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert math.isclose(c1.distance(c2), 5.0)
    assert str(c1) == "<3,4>"
    assert math.isclose(c2.distance(c1), 5.0)

def test_Fraction():
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b
    d = b - a
    assert str(c) == "16/16"
    assert math.isclose(float(c), 1.0)
    assert math.isclose(float(d), 0.5)
    assert str(a.inverse()) == "4/1"
    assert math.isclose(float(a.inverse()), 4.0)

    try:
        Fraction(3.14, 2.7)
    except AssertionError:
        pass
    else:
        assert False, "Expected AssertionError for non-integers"

def test_intSet():
    s = intSet()
    assert str(s) == "{}"
    
    s.insert(3)
    s.insert(4)
    s.insert(3)
    assert str(s) == "{3,4}"

    assert s.member(3) is True
    assert s.member(5) is False

    s.insert(6)
    assert str(s) == "{3,4,6}"

    s.remove(3)
    assert str(s) == "{4,6}"

    try:
        s.remove(3)
    except ValueError as e:
        assert str(e) == "3 not found"
    else:
        assert False, "Expected ValueError when removing non-existent element"

if __name__ == "__main__":
    test_Coordinate()
    test_Fraction()
    test_intSet()
    print("All tests passed!")
