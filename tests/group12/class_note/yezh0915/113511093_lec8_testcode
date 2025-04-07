import pytest
from src.mit_ocw_exercises.lec8_classes import Coordinate

def test_coordinate_init():
    c = Coordinate(3, 4)
    assert c.x == 3
    assert c.y == 4

def test_coordinate_str():
    c = Coordinate(3, 4)
    assert str(c) == "<3,4>"

def test_coordinate_distance():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.distance(c2) == 5.0
