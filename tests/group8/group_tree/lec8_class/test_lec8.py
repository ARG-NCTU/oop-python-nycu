import lec8
import pytest

def test_coordinate():
    c=lec8.Coordinate(4,6)
    d=lec8.Coordinate(1,2)
    assert c.distance(d)==5
    assert str(c)=="<4,6>"

def test_fraction():
    c=lec8.Fraction(4,6)
    d=lec8.Fraction(1,2)
    sum=c.__add__(d)
    assert sum.num==14
    assert sum.denom==12
    assert str(c)=="4/6"

def test_intSet():
    c=lec8.intSet()
    c.insert(1)
    c.insert(2)
    c.insert(3)
    assert str(c)=="{1,2,3}"
    c.remove(3)
    assert str(c)=="{1,2}"
    assert c.member(3)==False
