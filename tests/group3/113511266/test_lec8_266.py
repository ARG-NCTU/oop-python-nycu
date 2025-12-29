import add_path
import mit_ocw_exercises.lec8_classes as lec8
import pytest

def test_Coordinate():
    c1 = lec8.Coordinate(6, 8)
    c2 = lec8.Coordinate(3, 4)
    c3 = lec8.Coordinate(0, 0)
    assert c1.x == 6 and c1.y == 8
    assert c2.x == 3 and c2.y == 4
    assert str(c1) == "<6,8>"
    assert str(c2) == "<3,4>"
    assert c1.distance(c2) == 5.0 
    assert c2.distance(c1) == 5.0
    assert c1.distance(c3) == 10.0

def test_Fraction():
    a = lec8.Fraction(1, 2)
    b = lec8.Fraction(3, 4)
    c = a + b
    assert str(c) == "10/8"
    assert float(c) == 1.25
    d = b - a
    assert str(d) == "2/8"
    assert float(d) == 0.25
    e = b.inverse()
    assert str(e) == "4/3"
    assert float(e) == 1.3333333333333333

def test_intSet():
    s = lec8.intSet()
    assert str(s) == "{}"  

    s.insert(3)
    s.insert(4)
    s.insert(3)  
    assert str(s) == "{3,4}"

    assert s.member(3) is True
    assert s.member(5) is False

    s.insert(6)
    assert str(s) == "{3,4,6}"

    s.remove(3)
    assert str(s) == "{4,6}"

    try:
        s.remove(3)  
    except ValueError as e:
        assert str(e) == "3 not found"
    else:
        assert False, "Expected ValueError not raised"