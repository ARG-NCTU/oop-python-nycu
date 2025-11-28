import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lec8_classes

def test_coordinate_distance():
    c1 = lec8_classes.Coordinate(0, 0)
    c2 = lec8_classes.Coordinate(3, 4)
    assert c1.distance(c2) == 5.0

def test_coordinate_str():
    c = lec8_classes.Coordinate(10, 20)
    assert str(c) == "<10,20>"
