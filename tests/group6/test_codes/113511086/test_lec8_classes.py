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

def test_fraction_add_subtract():
    f1 = lec8.Fraction(1, 4)
    f2 = lec8.Fraction(5, 4)
    # addition
    result_add = f1 + f2
    assert isinstance(result_add, lec8.Fraction)
    assert result_add.num == 1*4 + 5*4  # 4 + 20 = 24
    assert result_add.den == 4*4        # 16
    assert str(result_add) == "24/16"
    # subtraction
    result_sub = f1 - f2
    assert result_sub.num == 1*4 - 5*4  # -16
    assert result_sub.den == 16
    assert str(result_sub) == "-16/16"

def test_fraction_inverse():
    f = lec8.Fraction(3, 5)
    inv = f.inverse()
    assert inv.num == 5
    assert inv.den == 3
    # inverse of inverse returns original
    assert inv.inverse().num == f.num
    assert inv.inverse().den == f.den


# =========================
# Tests for intSet
# =========================
def test_intSet_insert_and_member():
    s = lec8.intSet()
    s.insert(1)
    assert s.member(1) == True
    assert s.member(2) == False
    # insert duplicate should not change vals
    s.insert(1)
    assert s.vals == [1]
    # insert multiple values
    s.insert(3)
    s.insert(2)
    assert s.vals == [1, 2, 3]  # should be sorted

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
