import add_path
import pytest
import mit_ocw_exercises.lec8_classes as lec8
import math
def test_cor():
    c = lec8.Coordinate(1, 2)
    origin = lec8.Coordinate(0,0)
    assert c.x == 1
    assert c.y == 2
    assert origin.x == origin.y == 0
    assert c.distance(origin) == math.sqrt(5)
    assert origin.distance(c) == math.sqrt(5)
    assert str(c) == "<1,2>"

def test_frac():
    a=lec8.Fraction(1,4)
    b=lec8.Fraction(3,4)
    c=a+b
    d=lec8.Fraction(1,1)
    assert a.num == 1 
    assert str(a) == "1/4"
    #assert a+b == c
    print(a+b)
    print(c)
    print(a-b)
    print(str(a-b))
    print(float(a))
    print(float(c))
    print(a*b)
    print(a.inverse())
test_frac()
