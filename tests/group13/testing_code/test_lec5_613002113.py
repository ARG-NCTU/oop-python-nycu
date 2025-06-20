import practice.lec5_module as lec5
import pytest
import random

def test_position():
    position1 = lec5.Location(3, 4)
    position2 = lec5.Location(0, 0)
    
    assert position1.get_x() == 3
    assert position1.get_y() == 4
    assert position1.dist_from(position2) == pytest.approx(5.0)
    assert str(position1) == "<3, 4>"
    
    position3 = position1.move(1, -1)
    assert position3.get_x() == 4
    assert position3.get_y() == 3
    assert position1.dist_from(position3) == pytest.approx(1.4142135623730951)
    assert position3.dist_from(position1) == pytest.approx(1.4142135623730951)