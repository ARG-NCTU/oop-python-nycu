from lec8 import Coordinate, Fraction, intSet

def test_coordinate():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert str(c1) == "<3,4>"
    assert c1.distance(c2) == 5.0
    assert c2.distance(c1) == 5.0

def test_fraction_operations():
    a = Fraction(1, 4)
    b = Fraction(3, 4)

    c = a + b
    assert str(c) == "16/16"
    assert float(c) == 1.0

    d = a - b
    assert str(d) == "-8/16"
    assert float(d) == -0.5

    e = a * b
    assert str(e) == "3/16"
    assert float(e) == 3/16

    assert str(b.inverse()) == "4/3"
    assert float(b.inverse()) == 4/3

def test_intset():
    s = intSet()
    assert str(s) == "{}"

    s.insert(3)
    s.insert(4)
    s.insert(3)
    assert str(s) == "{3,4}"

    assert s.member(3)
    assert not s.member(5)

    s.insert(6)
    assert str(s) == "{3,4,6}"

    s.remove(3)
    assert str(s) == "{4,6}"