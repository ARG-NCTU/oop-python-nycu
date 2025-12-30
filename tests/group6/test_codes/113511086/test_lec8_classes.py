import add_path
import mit_ocw_exercises.lec8_classes as lec8
import pytest
import math

# =========================
# Tests for Coordinate
# =========================
def test_coordinate_attributes_and_str():
    c = lec8.Coordinate(5, 6)
    assert c.x == 5
    assert c.y == 6
    assert str(c) == "<5,6>"

def test_coordinate_distance():
    c = lec8.Coordinate(5, 6)
    origin = lec8.Coordinate(0, 0)
    # distance should match Pythagorean theorem
    expected_distance = math.sqrt((5 - 0) ** 2 + (6 - 0) ** 2)
    assert c.distance(origin) == expected_distance

def test_coordinate_distance_same_point():
    c1 = lec8.Coordinate(3, 4)
    c2 = lec8.Coordinate(3, 4)
    assert c1.distance(c2) == 0


# =========================
# Tests for Fraction
# =========================
def test_fraction_str_and_float():
    f = lec8.Fraction(1, 4)
    assert str(f) == "1/4"
    assert float(f) == 0.25


def test_intSet_str():
    s = lec8.intSet()
    s.insert(5)
    s.insert(1)
    s.insert(3)
    assert str(s) == "{1,3,5}"

def test_intSet_empty():
    s = lec8.intSet()
    assert str(s) == "{}"
    assert s.member(0) == False
