import add_path
import pytest
import mit_ocw_exercises.lec8_classes as lec8
import math
def test_cor():
    c = lec8.Coordinate(7, 12)
    origin = lec8.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert origin.x == origin.y == 0
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5