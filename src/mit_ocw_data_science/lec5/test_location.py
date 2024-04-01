import pytest
from lec5_module import Location

def test_location():
    # Test the Location class
    loc1 = Location(0, 0)
    assert loc1.get_x() == 0
    assert loc1.get_y() == 0

    loc2 = Location(1, 1)
    assert loc2.get_x() == 1
    assert loc2.get_y() == 1

    loc3 = loc1.move(2, 3)
    assert loc3.get_x() == 2
    assert loc3.get_y() == 3

    loc4 = loc2.move(-1, -1)
    assert loc4.get_x() == 0
    assert loc4.get_y() == 0

    assert loc1.dist_from(loc2) == pytest.approx(1.41421356237, rel=1e-9)
    assert loc1.dist_from(loc3) == pytest.approx(3.60555127546, rel=1e-9)
    assert loc2.dist_from(loc3) == pytest.approx(2.23606797749, rel=1e-9)

    assert str(loc1) == '<0, 0>'
    assert str(loc2) == '<1, 1>'
    assert str(loc3) == '<2, 3>'
    assert str(loc4) == '<0, 0>'

