from lec8_final import *
import pytest

def test_coordinate():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.distance(c2) == 5.0
    assert str(c1) == "<3,4>"

def test_fraction_add_sub_float_inverse():
    f1 = Fraction(1, 4)
    f2 = Fraction(3, 4)
    f3 = f1 + f2
    f4 = f2 - f1
    assert str(f3) == "16/16"
    assert str(f4) == "8/16"
    assert float(f3) == 1.0
    inv = f2.inverse()
    assert isinstance(inv, Fraction)
    assert str(inv) == "4/3"

def test_fraction_assertion():
    with pytest.raises(AssertionError):
        Fraction(1.5, 3)

def test_intset_insert_member_remove():
    s = intSet()
    assert str(s) == "{}"
    s.insert(3)
    s.insert(4)
    s.insert(3)
    assert str(s) == "{3,4}"
    assert s.member(3)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert str(s) == "{4}"
    with pytest.raises(ValueError):
        s.remove(42)
