import lec8_classes as lec
from lec8_classes import Coordinate

def coordinate_test():
    a0 = Coordinate (0, 0)
    a1 = Coordinate(5, 12)
    a2 = Coordinate(6, 8)
    assert a1.x == 5 and a1.y ==12
    assert a2.x == 6 and a2.y == 8
    assert a1.distance(a0) == 13
    assert a2.distance(a0) == 10
    print (a1.distance(a0))
    print("The distance from a0 to a1 is " +str(a1.distance(a0)))
coordinate_test()

def fraction_test():
    b1 = lec.Fraction(3, 4)
    b2 = lec.Fraction(1, 4)
    c = b1 + b2
    assert float(c) == 1.0
    print(c)
    print(float(c))
    assert lec.Fraction.__float__(c) == 1.0
    print(float(b1.inverse()))
    try:
        c = lec.Fraction(3.14,2.7)
    except AssertionError:
        pass
fraction_test()

def intset_test():
    s = lec.intSet()
    assert str(s) == "{}"
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(3)
    assert str(s) == "{1,2,3}"
    print (s)
    assert s.member(3) is True
    assert s.member(5) is False
    s.remove(1)
    assert str(s) == "{2,3}"
    print(s)
    try:
        s.remove(1)
    except ValueError as e:
        assert str(e) == "1 not found"
intset_test()
