import add_path
import mit_ocw_exercises.lec8_classes as l8 # type: ignore
import pytest

import random

def test_coordinate():
    x1 = random.uniform(-100, 100)
    y1 = random.uniform(-100, 100)
    x2 = random.uniform(-100, 100)
    y2 = random.uniform(-100, 100)

    c1 = l8.Coordinate(x1, y1)
    c2 = l8.Coordinate(x2, y2)
    assert c1.x == x1 and c1.y == y1
    assert c2.x == x2 and c2.y == y2
    expected_distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    assert c1.distance(c2) == pytest.approx(expected_distance)
    assert str(c1) == f"<{x1},{y1}>"