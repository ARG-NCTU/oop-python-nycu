import pytest
import lec8_classes as lec8
import math

def test_coordinate():
    c1 = lec8.Coordinate(5, 6)
    c2 = lec8.Coordinate(2, 2)
    assert c1.x == 5 and c1.y == 6
    assert c2.x == 2 and c2.y == 2
    assert c1.distance(c2) == 5.0  # (3^2 + 4^2) ** 0.5 = 5
    assert str(c1) == "<5,6>"

def test_fraction():
    a = lec8.Fraction(1,4)
    b = lec8.Fraction(3,4)
    c = a + b
    assert float(c) == 1.0
    assert lec8.Fraction.__float__(c) == 1.0
    assert float(b.inverse()) == 1.3333333333333333
    try:
        c = lec8.Fraction(3.14,2.7)
    except AssertionError:
        pass

def test_intset():
    s = lec8.intSet()
    assert str(s) == "{}"  # 初始集合應該是空的##

    s.insert(5)
    s.insert(6)
    s.insert(6)  # 重複插入應該無效
    assert str(s) == "{5,6}"

    assert s.member(3) is False
    assert s.member(5) is True

    s.insert(3)
    assert str(s) == "{3,5,6}"

    s.remove(5)
    assert str(s) == "{3,6}"

    try:
        s.remove(5)  # 應該拋出 ValueError
    except ValueError as e:
        assert str(e) == "5 not found"
