import add_path
import lec8_classes as lec8
import pytest

def test_Coordinate():
    c = lec8.Coordinate(3,4)
    origin = lec8.Coordinate(0,0)
    assert c.x == 3
    assert origin.x == 0
    assert c.distance(origin) == 5.0
    assert lec8.Coordinate.distance(c, origin) == 5.0
    assert origin.distance(c) == 5.0
    assert str(c) == "<3,4>"

def test_Fraction():
    a = lec8.Fraction(1,4)
    b = lec8.Fraction(3,4)
    c = a + b # c is a Fraction object
    assert str(c) == "16/16"
    assert lec8.Fraction.__float__(c) == 1.0
    assert str(a - b) == "-8/16"
    assert str(a.inverse()) == "4/1"
    assert str(b.inverse()) == "4/3"

def test_intSet():
    s = lec8.intSet()
    assert s.__str__() == "{}"
    s.insert(3)
    s.insert(4)
    s.insert(3)
    assert s.__str__() == "{3,4}"
    assert s.member(3) == True
    assert s.member(5) == False
    s.insert(6)
    assert s.__str__() == "{3,4,6}"
    s.remove(3)
    assert s.__str__() == "{4,6}"
