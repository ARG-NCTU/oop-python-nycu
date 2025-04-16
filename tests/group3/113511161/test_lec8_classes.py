import add_path
import  mit_ocw_exercises.lec8_classes as lec8
import pytest
import random
#from functions import is_even_with_return, is_even_without_return, is_even, bisection_cuberoot_approx

def test_coordinate():
    for i in range(10):
        x1= random.randint(0, 10)
        y1= random.randint(0, 10)
        x2= random.randint(0, 10)
        y2= random.randint(0, 10)
        coor1= lec8.Coordinate(x1,y1)
        coor2 = lec8.Coordinate(x2,y2)
        assert str(coor1) == f"<{x1},{y1}>"
        assert str(coor2) == f"<{x2},{y2}>"
        assert coor1.distance(coor2) == ((x1-x2)**2 + (y1-y2)**2)**0.5
        assert coor2.distance(coor1) == ((x2-x1)**2 + (y2-y1)**2)**0.5
def test_fraction():
    for i in range(10):
        x1= random.randint(1, 10)
        y1= random.randint(1, 10)
        x2= random.randint(1, 10)
        y2= random.randint(1, 10)
        frac1= lec8.Fraction(x1,y1)
        frac2= lec8.Fraction(x2,y2)
        assert str(frac1) == f"{x1}/{y1}"
        assert str(frac2) == f"{x2}/{y2}"
        frac3= frac1+frac2
        assert frac3.num == x1*y2+x2*y1
        assert frac3.denom == y1*y2
        frac3 = frac1-frac2
        assert frac3.num == x1*y2-x2*y1
        assert frac3.denom == y1*y2
        assert float(frac1)== x1/y1
        assert float(frac2)== x2/y2
        assert frac1.inverse().num == y1
        assert frac1.inverse().denom == x1
        assert frac2.inverse().num == y2
        assert frac2.inverse().denom == x2
        assert frac1.inverse().inverse().num == x1
        assert frac1.inverse().inverse().denom == y1
def test_intSet():
    l= [random.randint(1, 100) for i in range(20)]
    s= lec8.intSet()
    for i in l:
        s.insert(i)
    for i in l:
        assert s.member(i) == True
    s.remove(l[13])
    assert s.member(l[13]) == False
