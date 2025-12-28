import add_path
import lec8_classes as lec8
import math
import pytest

def test_coordinate_init_and_str():
    c = lec8.Coordinate(3, 4)
    assert c.x == 3
    assert c.y == 4
    assert str(c) == "<3,4>"

def test_coordinate_distance_origin():
    c = lec8.Coordinate(3, 4)
    origin = lec8.Coordinate(0, 0)
    assert c.distance(origin) == 5.0

def test_coordinate_distance_symmetry():
    c1 = lec8.Coordinate(3, 4)
    c2 = lec8.Coordinate(0, 0)
    assert c1.distance(c2) == c2.distance(c1)

def test_coordinate_distance_call_via_class_method_style():
    c1 = lec8.Coordinate(3, 4)
    c2 = lec8.Coordinate(0, 0)
    # Equivalent to c1.distance(c2)
    assert lec8.Coordinate.distance(c1, c2) == 5.0


def test_fraction_init_sets_fields():
    f = lec8.Fraction(1, 4)
    assert f.num == 1
    assert f.denom == 4

def test_fraction_init_requires_ints():
    with pytest.raises(AssertionError):
        lec8.Fraction(3.14, 2)

    with pytest.raises(AssertionError):
        lec8.Fraction(3, 2.7)

    with pytest.raises(AssertionError):
        lec8.Fraction("3", 2)
    
def test_fraction_str():
    f = lec8.Fraction(1, 4)
    assert str(f) == "1/4"

def test_fraction_add():
    a = lec8.Fraction(1, 4)
    b = lec8.Fraction(3, 4)
    c = a + b
    assert isinstance(c, lec8.Fraction)
    assert (c.num, c.denom) == (16, 16)  # (1*4 + 4*3)/(4*4) = 16/16
    assert str(c) == "16/16"

def test_fraction_sub():
    a = lec8.Fraction(3, 4)
    b = lec8.Fraction(1, 4)
    c = a - b
    assert isinstance(c, lec8.Fraction)
    assert (c.num, c.denom) == (8, 16)  # (3*4 - 4*1)/(4*4) = 8/16
    assert str(c) == "8/16"

def test_fraction_float():
    f = lec8.Fraction(1, 4)
    assert float(f) == 0.25

def test_fraction_float_via_dunder_call():
    f = lec8.Fraction(1, 4)
    assert lec8.Fraction.__float__(f) == 0.25

def test_fraction_inverse():
    f = lec8.Fraction(1, 4)
    inv = f.inverse()
    assert isinstance(inv, lec8.Fraction)
    assert (inv.num, inv.denom) == (4, 1)
    assert str(inv) == "4/1"
    assert float(inv) == 4.0

def test_fraction_sub_does_not_mutate_operands():
    a = lec8.Fraction(3, 4)
    b = lec8.Fraction(1, 4)
    _ = a - b
    assert (a.num, a.denom) == (3, 4)
    assert (b.num, b.denom) == (1, 4)

def test_intset_init_empty_str():
    s = lec8.intSet()
    assert str(s) == "{}"
    assert s.vals == []

def test_intset_insert_unique():
    s = lec8.intSet()
    s.insert(3)
    s.insert(4)
    s.insert(3)  # duplicate should not be added
    assert sorted(s.vals) == [3, 4]
    assert str(s) == "{3,4}"

def test_intset_remove_existing():
    s = lec8.intSet()
    s.insert(4)
    s.insert(6)
    s.remove(4)
    assert s.member(4) is False
    assert s.member(6) is True
    assert str(s) == "{6}"

def test_intset_remove_missing_raises_valueerror_message():
    s = lec8.intSet()
    s.insert(1)
    with pytest.raises(ValueError) as excinfo:
        s.remove(99)
    assert str(excinfo.value) == "99 not found"

def test_intset_str_sorts_output():
    s = lec8.intSet()
    s.insert(10)
    s.insert(2)
    s.insert(7)
    # __str__ sorts before joining
    assert str(s) == "{2,7,10}"

def test_intset_multiple_operations_sequence_matches_lecture_asserts():
    s = lec8.intSet()
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

    with pytest.raises(ValueError) as excinfo:
        s.remove(3)
    assert str(excinfo.value) == "3 not found"