import add_path
import mit_ocw_exercises.lec8_classes as lc
import pytest

def test_coordinate():
    c = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0,0)
    assert c.x == 5
    assert c.y == 12
    assert c.distance(origin) == 13
    assert lc.Coordinate.distance(c, origin) == 13
    assert origin.distance(c) == 13
    
def test_point():
    p = lc.Point(5, 12)
    assert p.x == 5
    assert p.y == 12
    assert p.distance() == 13
    assert p.distance(lc.Coordinate(0,0)) == 13