import add_path
import mit_ocw_exercises.lec8_classes as lec8
import pytest

def test_Coordinate():
    c = lec8.Coordinate(5,6)
    assert c.x == 5
    assert c.y == 6
    assert str(c) == "<5,6>"
    origin = lec8.Coordinate(0,0)
    assert c.distance(origin) == 7.810249675906654

def test_Fraction():
    num1 = lec8.Fraction(1,4)
    num2 = lec8.Fraction(5,4)
    assert str(num1) == "1/4"
    assert str(num2) == "5/4"
    assert str(num1 + num2) == "24/16"
    assert str(num1 - num2) == "-16/16"
    assert float(num1) == 0.25
    assert float(num2) == 1.25
    assert str(num1.inverse()) == "4/1"
    assert str(num2.inverse()) == "4/5"
    
def test_intSet():
    num1 = lec8.intSet()
    num1.insert(1)
    assert num1.vals == [1]
    num2 = lec8.intSet()
    num2.insert(2)
    assert num2.vals == [2]
    assert num1.member(1) == True
    assert num2.member(1) == False
    num1.insert(2)
    assert str(num1) == '{1,2}'
    
    
    
    
    


    
    