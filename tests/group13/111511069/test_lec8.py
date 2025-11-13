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
    assert str(c2) == f"<{x2},{y2}>"

def test_fraction():
    n1 = random.randint(1, 100)
    d1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    d2 = random.randint(1, 100)

    f1 = l8.Fraction(n1, d1)
    f2 = l8.Fraction(n2, d2)

    assert f1.num == n1 and f1.denom == d1
    assert f2.num == n2 and f2.denom == d2
    assert str(f1) == f"{n1}/{d1}"
    assert str(f2) == f"{n2}/{d2}"
    assert float(f1) == pytest.approx(n1 / d1)
    assert float(f2) == pytest.approx(n2 / d2)

def test_fraction_add_sub():
    n1 = random.randint(1, 100)
    d1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    d2 = random.randint(1, 100)

    f1 = l8.Fraction(n1, d1)
    f2 = l8.Fraction(n2, d2)

    f_add = f1 + f2
    assert float(f_add) == pytest.approx(n1/d1 + n2/d2)

    f_sub = f1 - f2
    assert float(f_sub) == pytest.approx(n1/d1 - n2/d2)
