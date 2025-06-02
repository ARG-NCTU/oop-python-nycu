import lec8
import pytest

def test_coordinate():
    c=lec8.Coordinate(5,7)
    d=lec8.Coordinate(2,3)
    assert c.distance(d)==5
    assert str(c)=="<5,7>"

def test_fraction():
    c=lec8.Fraction(4,5)
    d=lec8.Fraction(1,10)
    sum = c + d
    assert sum.num==9
    assert sum.denom==10
    assert str(c)=="4/5"

def test_intSet():
    c=lec8.intSet()
    c.insert(3)
    c.insert(2)
    c.insert(4)
    assert str(c)=="{2,3,4}"
    c.remove(3)
    assert str(c)=="{2,4}"
    assert c.member(3)==False
