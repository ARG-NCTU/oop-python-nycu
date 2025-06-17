import pytest
import lec8_classes as lec8
import math

def test_coordinate():
    c1 = lec8.Coordinate(5, 6)
    c2 = lec8.Coordinate(2, 2)
    
    # Check attributes
    assert c1.x == 5 and c1.y == 6
    assert c2.x == 2 and c2.y == 2

    # Distance formula: sqrt((5-2)^2 + (6-2)^2) = sqrt(9+16) = 5.0
    assert math.isclose(c1.distance(c2), 5.0, rel_tol=1e-9)

    # String representation
    assert str(c1) == "<5,6>"
    assert str(c2) == "<2,2>"

def test_fraction():
    a = lec8.Fraction(1, 4)
    b = lec8.Fraction(3, 4)
    c = a + b

    # Check addition and float conversion
    assert float(c) == 1.0
    assert lec8.Fraction.__float__(c) == 1.0

    # Check inverse
    inv = b.inverse()
    assert math.isclose(float(inv), 4/3, rel_tol=1e-9)
    assert isinstance(inv, lec8.Fraction)

    # Ensure only integers allowed
    with pytest.raises(AssertionError):
        lec8.Fraction(3.14, 2.7)

    # Check string representation (optional, depending on implementation)
    assert str(a) == "1/4"
    assert str(b) == "3/4"
    assert str(c) == "16/16"

def test_intset():
    s = lec8.intSet()
    assert str(s) == "{}"  # Empty set initially

    # Insert elements
    s.insert(5)
    s.insert(7)
    s.insert(6)
    assert str(s) == "{5,6,7}"

    # Membership test
    assert s.member(3) is False
    assert s.member(7) is True

    # Insert duplicate (should not change set)
    s.insert(6)
    assert str(s) == "{5,6,7}"

    # Insert new
    s.insert(3)
    assert str(s) == "{3,5,6,7}"

    # Remove
    s.remove(5)
    assert str(s) == "{3,6,7}"

    # Remove non-existent element
    with pytest.raises(ValueError) as excinfo:
        s.remove(5)
    assert "5 not found" in str(excinfo.value)


