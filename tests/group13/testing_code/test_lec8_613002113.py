import add_path
import pytest
import mit_ocw_exercises.lec8_classes as lec8
import math

def test_cor():
    c = lec8.Coordinate(3, 4)
    origin = lec8.Coordinate(0, 0)
    assert c.x == 3
    assert c.y == 4
    assert origin.x == origin.y == 0
    assert c.distance(origin) == math.sqrt(25)
    assert origin.distance(c) == math.sqrt(25)
    assert str(c) == "<3,4>"

def test_frac():
    a = lec8.Fraction(2, 5)
    b = lec8.Fraction(7, 10)
    c = a + b
    d = lec8.Fraction(9, 10)
    assert a.num == 2
    assert str(a) == "2/5"

test_cor()
test_frac()