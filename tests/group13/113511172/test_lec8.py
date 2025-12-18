import lec_test_codes.add_path
import mit_ocw_exercises.lec8_classes as l8
import pytest

def test_coordinate_basic():
    c1 = l8.Coordinate(3, 4)
    c2 = l8.Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert pytest.approx(c1.distance(c2), rel=1e-9) == 5.0
    assert str(c1) == "<3,4>"