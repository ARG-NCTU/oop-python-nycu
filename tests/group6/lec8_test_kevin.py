import add_path
import mit_ocw_exercises.lec8_classes as lc
import pytest


# Test Coordinate Class
def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0, 0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
    assert str(c) == "<3,4>"


# Test intSet Class
def test_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)


# Test Fraction Class
def test_fraction():
    half = lc.Fraction(1, 2)
    quarter = lc.Fraction(1, 4)
    assert half.num == 1
    assert half.denom == 2
    assert quarter.num == 1
    assert quarter.denom == 4

    # Test Fraction Addition
    sum_fraction = half + quarter
    assert sum_fraction.num == 6
    assert sum_fraction.denom == 8

    # Test Fraction String and Float Representation
    assert str(half) == "1/2"
    assert float(half) == 0.5
    assert str(quarter.inverse()) == "4/1"


# Test Coordinate Variations
@pytest.mark.parametrize("x, y, expected_distance", [
    (3, 4, 5),
    (5, 12, 13),
    (9, 40, 41),
    (7, 24, 25),
    (6, 8, 10)
])
def test_various_coordinates(x, y, expected_distance):
    c = lc.Coordinate(x, y)
    origin = lc.Coordinate(0, 0)
    assert c.x == x
    assert c.y == y
    assert c.distance(origin) == expected_distance
    assert origin.distance(c) == expected_distance


# Test intSet with Different Data
@pytest.mark.parametrize("insert_vals, remove_val, remaining_vals", [
    ([100, 200, 300], 100, [200, 300]),
    ([7, 9], 7, [9]),
    ([8, 7], 8, [7]),
])
def test_various_intsets(insert_vals, remove_val, remaining_vals):
    s = lc.intSet()
    for val in insert_vals:
        s.insert(val)
    assert all(s.member(val) for val in insert_vals)
    s.remove(remove_val)
    assert not s.member(remove_val)
    assert all(s.member(val) for val in remaining_vals)


# Test Additional Fraction Operations
def test_fraction_operations():
    p = lc.Fraction(2, 5)
    q = lc.Fraction(1, 5)

    # Test Addition and Subtraction
    sum_fraction = p + q
    assert str(sum_fraction) == "15/25"
    sub_fraction = p - q
    assert str(sub_fraction) == "5/25"

    # Test Float and Inverse
    assert float(p) == 0.4
    assert str(p.inverse()) == "5/2"


# Custom Test for a Student or Group
def test_custom_ella_practices():
    ella = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0, 0)
    assert ella.distance(origin) == 13

    a = lc.Fraction(3, 4)
    assert str(a) == '3/4'
    assert float(a) == 0.75
    assert str(a.inverse()) == '4/3'

    b = lc.Fraction(2, 5)
    assert str(b) == '2/5'
    assert float(b) == 0.4

    # Test Fraction Addition
    c = a + b
    assert str(c) == '23/20'
    assert float(c) == 1.15

    # Test intSet Operations
    pra_set = lc.intSet()
    pra_set.insert(3)
    pra_set.insert(4)
    assert pra_set.member(3)
    assert pra_set.member(4)
    pra_set.remove(3)
    assert not pra_set.member(3)


if __name__ == "__main__":
    pytest.main()

