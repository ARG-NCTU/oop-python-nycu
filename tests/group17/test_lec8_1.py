import add_path
import mit_ocw_exercises.lec8_classes as lc
import pytest

def test_coordinate():
    c = lc.Coordinate(6, 8)
    origin = lc.Coordinate(0, 0)
    assert c.x == 6
    assert c.y == 8
    assert c.distance(origin) == 10.0



