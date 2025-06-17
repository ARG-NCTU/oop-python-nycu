import add_path
import mit_ocw_exercises.lec8_classes as lec8
import pytest
# from oop-python-nycu.src.mit_ocw_exercises.lec8_classes import Coordinate

def test_coordinate_init():
    c = lec8.Coordinate(3, 4)
    assert c.x == 3
    assert c.y == 4

def test_coordinate_str():
    c = lec8.Coordinate(3, 4)
    assert str(c) == "<3,4>"

def test_coordinate_distance():
    c1 = lec8.Coordinate(3, 4)
    c2 = lec8.Coordinate(0, 0)
    assert c1.distance(c2) == 5.0
