import pytest
import lec8_classes as lec8
import math


# ---------- Coordinate ----------
def test_coordinate():
    c1 = lec8.Coordinate(4, 6)
    c2 = lec8.Coordinate(1, 2)
    # Δx = 3, Δy = 4  ⇒ distance = 5
    assert (c1.x, c1.y) == (4, 6)
    assert (c2.x, c2.y) == (1, 2)
    assert c1.distance(c2) == 5.0
    assert str(c1) == "<4,6>"
    point_p = lec8.Coordinate(7, 1)
    point_q = lec8.Coordinate(3, -2)
    assert (point_p.x, point_p.y) == (7, 1)
    assert (point_q.x, point_q.y) == (3, -2)
    assert point_p.distance(point_q) == 5.0            # Δx=4, Δy=3
    assert str(point_p) == "<7,1>"


# ---------- Fraction ----------
def test_fraction():
    a = lec8.Fraction(1, 3)
    b = lec8.Fraction(2, 3)
    c = a + b                 # 1/3 + 2/3 = 1
    assert float(c) == 1.0
    assert lec8.Fraction.__float__(c) == 1.0
    # b.inverse() = 3/2 = 1.5
    assert float(b.inverse()) == 1.5


def test_assertionerror():
    with pytest.raises(AssertionError):
        lec8.Fraction(3.14, 2.7)


# ---------- intSet ----------
def test_intset():
    s = lec8.intSet()
    assert str(s) == "{}"          # 空集合

    s.insert(1)
    s.insert(2)
    s.insert(2)                    # 重複插入無效
    assert str(s) == "{1,2}"

    assert s.member(0) is False
    assert s.member(1) is True

    s.insert(4)
    assert str(s) == "{1,2,4}"

    s.remove(2)
    assert str(s) == "{1,4}"

    s.insert(2)
    assert str(s) == "{1,2,4}"

    # 再移除 2，之後再移除一次應拋錯
    s.remove(2)
    assert str(s) == "{1,4}"

    with pytest.raises(ValueError) as exc:
        s.remove(2)
    assert str(exc.value) == "2 not found"

