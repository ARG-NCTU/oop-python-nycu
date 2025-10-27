import lec_test_codes.add_path
import mit_ocw_exercises.lec8_classes as l8
import pytest

def test_coordinate_basic():
    c1 = l8.Coordinate(3, 4)
    c2 = l8.Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert pytest.approx(c1.distance(c2), rel=1e-9) == 5.0
    assert str(c1) == "<3,4>"

def test_coordinate_distance_symmetry():
    a = l8.Coordinate(1, 2)
    b = l8.Coordinate(4, 6)
    assert pytest.approx(a.distance(b), rel=1e-9) == pytest.approx(b.distance(a), rel=1e-9)
    
def test_fraction_str_and_float():
    a = l8.Fraction(1, 4)
    b = l8.Fraction(3, 4)
    c = a + b
    assert str(c) == "16/16" or str(c) == "1/1"  # 因為尚未化簡
    assert pytest.approx(float(c), rel=1e-9) == 1.0
    assert pytest.approx(float(b.inverse()), rel=1e-9) == 4 / 3
    
def test_fraction_add_and_sub():
    a = l8.Fraction(1, 3)
    b = l8.Fraction(1, 6)
    assert str(a + b) == "9/18"  # (1*6 + 3*1)/(3*6) = 9/18
    assert str(a - b) == "3/18"  # (1*6 - 3*1)/(3*6) = 3/18

def test_fraction_assertion_error():
    with pytest.raises(AssertionError):
        l8.Fraction(3.14, 2.7)