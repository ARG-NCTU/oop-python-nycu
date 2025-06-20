from src.mit_ocw_exercises.lec8_classes import Coordinate, Fraction, intSet

def test_coordinate():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert c1.distance(c2) == 5.0
    assert str(c1) == "<3,4>"
    assert str(c2) == "<0,0>"
    # Symmetry
    assert c1.distance(c2) == c2.distance(c1)
