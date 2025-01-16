import pytest
from lec8_source_code import Coordinate, Fraction, intSet

# Test Coordinate class
def test_coordinate():
    c = Coordinate(3, 4)
    origin = Coordinate(0, 0)

    # Test attributes
    assert c.x == 3
    assert origin.x == 0

    # Test distance calculation
    assert c.distance(origin) == pytest.approx(5.0, rel=1e-9)

    # Test string representation
    assert str(c) == "<3,4>"

# Test Fraction class
def test_fraction():
    a = Fraction(3, 4)
    b = Fraction(3, 4)

    # Test addition
    c = a + b
    assert str(c) == "3/2"  # Resulting fraction is 6/4, reduced to 3/2
    assert float(c) == 1.5

    # Test subtraction
    d = b - a
    assert str(d) == "0/1"  # Zero numerator, denominator defaults to 1
    assert float(d) == 0.0

    # Test float conversion
    assert float(a) == 0.75

    # Test inversion
    inv_b = b.inverse()
    assert str(inv_b) == "4/3"
    assert float(inv_b) == pytest.approx(1.3333333333333333, rel=1e-9)

    # Test invalid input
    with pytest.raises(AssertionError):
        Fraction(3.14, 2.7)  # Numerator and denominator must be integers

    # Test division
    e = a.divide(b)
    assert str(e) == "4/12"  # Division result without reduction

    # Test reduction
    f = Fraction(2, 4)
    reduced_f = f.reduce()
    assert str(reduced_f) == "1/2"  # Reduced fraction

# Test intSet class
def test_intSet():
    s = intSet()

    # Test string representation for empty set
    assert str(s) == "{}"

    # Test inserting elements
    s.insert(3)
    s.insert(4)
    s.insert(3)  # Duplicate insertions should have no effect
    assert str(s) == "{3,4}"

    # Test membership
    assert s.member(3) is True
    assert s.member(5) is False

    # Test removing elements
    s.remove(3)
    assert str(s) == "{4}"

    # Test removing a non-existent element
    with pytest.raises(ValueError, match="5 not found"):
        s.remove(5)
