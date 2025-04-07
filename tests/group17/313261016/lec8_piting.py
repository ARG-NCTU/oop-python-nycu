import add_path
import lec8_classes as lec8
import pytest


def test_coordinate():
    c = lec8.Coordinate(3, 4)
    origin = lec8.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
