import lec_8.py as lc
import pytest

def test_coordinate():
    c = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0,0)
    assert c.x == 5
    assert c.y == 12
    assert c.distance(origin) == 13
    assert origin.distance(c) == 13

def test_team_7_coordinate():
    c = lc.Coordinate(7, 24)
    origin = lc.Coordinate(0,0)
    assert c.x == 7
    assert c.y == 24
    assert c.distance(origin) == 25
    assert origin.distance(c) == 25