import add_ipath
import mit_ocw_excercises.lec8_classes as lc
import pytest


def test_coordinate():
    c = lc.Coordinate(7,24)
    origin = lc.Coordinate(0,0)
    assert c.x == 7
    assert c.y == 24
    assert c.distance(origin) == 25
    assert origin.distance(c) == 25
