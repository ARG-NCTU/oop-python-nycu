# -*- coding: utf-8 -*-
import pytest

import lec8_classes as lec8

def test_coordinate_basic():
    c1 = lec8.Coordinate(3, 4)
    c2 = lec8.Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert c1.distance(c2) == 5.0
    assert str(c1) == "<3,4>"


def test_fraction_add_sub_float_inverse():
    a = lec8.Fraction(1, 4)
    b = lec8.Fraction(3, 4)

    c = a + b
    assert str(c) == "16/16"
    assert float(c) == 1.0

    d = b - a
    assert str(d) == "8/16"
    assert float(d) == 0.5

    inv = b.inverse()
    assert str(inv) == "4/3"
    assert float(inv) == pytest.approx(4/3)


def test_fraction_invalid_types():
    with pytest.raises(AssertionError):
        lec8.Fraction(3.14, 2)


def test_fraction_denom_zero():
    with pytest.raises(AssertionError):
        lec8.Fraction(1, 0)


def test_fraction_inverse_zero_num():
    with pytest.raises(AssertionError):
        lec8.Fraction(0, 5).inverse()


def test_intset_workflow():
    s = lec8.intSet()
    assert str(s) == "{}"

    s.insert(3)
    s.insert(4)
    s.insert(3)  # duplicate
    assert str(s) == "{3,4}"

    assert s.member(3) is True
    assert s.member(5) is False

    s.insert(6)
    assert str(s) == "{3,4,6}"

    s.remove(3)
    assert str(s) == "{4,6}"

    with pytest.raises(ValueError) as e:
        s.remove(3)
    assert str(e.value) == "3 not found"
