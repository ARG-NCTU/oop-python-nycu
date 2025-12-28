import add_path
import lec8_classes as lec8
import math

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