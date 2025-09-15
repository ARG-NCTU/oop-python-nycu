import add_path
import mit_ocw_exercises.lec8_classes as lec8
import pytest


def test_Coordinate():
    c1 = lec8.Coordinate(3, 4)
    c2 = lec8.Coordinate(0, 0)
    c3 = lec8.Coordinate(-3, -4)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert str(c1) == "<3,4>"
    assert str(c2) == "<0,0>"
    assert c1.distance(c2) == 5.0 
    assert c2.distance(c1) == 5.0
    assert c1.distance(c3) == 10.0

