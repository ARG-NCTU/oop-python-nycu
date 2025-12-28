import add_path
import lec8_classes as lec8
import math

def test_coordinate_init_and_str():
    c = lec8.Coordinate(3, 4)
    assert c.x == 3
    assert c.y == 4
    assert str(c) == "<3,4>"