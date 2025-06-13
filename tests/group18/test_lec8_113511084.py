import os
import sys
import pytest
import math

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec8_classes as lec8

### --- Coordinate class tests --- ###

def test_coordinate_creation_and_str():
    c = lec8.Coordinate(3, 4)
    assert c.x == 3
    assert c.y == 4
    assert str(c) == "<3,4>"

def test_coordinate_distance():
    c1 = lec8.Coordinate(3, 4)
    c2 = lec8.Coordinate(0, 0)
    assert c1.distance(c2) == pytest.approx(5.0)
    assert c2.distance(c1) == pytest.approx(5.0)

### --- Fraction class tests --- ###

def test_fraction_creation_and_str():
    f = lec8.Fraction(3, 5)
    assert f.num == 3
    assert f.denom == 5
    assert str(f) == "3/5"

def test_fraction_add():
    f1 = lec8.Fraction(1, 4)
    f2 = lec8.Fraction(3, 4)
    result = f1 + f2
    assert isinstance(result, lec8.Fraction)
    assert result.num == 16
    assert result.denom == 16
    assert str(result) == "16/16"

def test_fraction_sub():
    f1 = lec8.Fraction(3, 4)
    f2 = lec8.Fraction(1, 4)
    result = f1 - f2
    assert isinstance(result, lec8.Fraction)
    assert result.num == 8
    assert result.denom == 16
    assert str(result) == "8/16"

def test_fraction_float_and_inverse():
    f = lec8.Fraction(2, 5)
    assert float(f) == pytest.approx(0.4)
    inv = f.inverse()
    assert isinstance(inv, lec8.Fraction)
    assert inv.num == 5 and inv.denom == 2
    assert float(inv) == pytest.approx(2.5)

def test_fraction_invalid_type():
    with pytest.raises(AssertionError):
        lec8.Fraction(3.14, 2)

### --- intSet class tests --- ###

def test_intset_insert_and_str():
    s = lec8.intSet()
    assert str(s) == "{}"
    s.insert(3)
    s.insert(4)
    s.insert(3)  # duplicate
    assert str(s) == "{3,4}"

def test_intset_member():
    s = lec8.intSet()
    s.insert(10)
    assert s.member(10) is True
    assert s.member(5) is False

def test_intset_remove_success_and_fail():
    s = lec8.intSet()
    s.insert(1)
    s.insert(2)
    s.remove(1)
    assert str(s) == "{2}"
    with pytest.raises(ValueError) as e:
        s.remove(99)
    assert str(e.value) == "99 not found"
