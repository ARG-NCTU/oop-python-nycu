import mit_ocw_exercises.lec8_classes as lec8


def test_coordinate_and_fraction_and_intset():
    c1 = lec8.Coordinate(3,4)
    c2 = lec8.Coordinate(0,0)
    assert c1.distance(c2) == 5.0
    assert str(c1) == "<3,4>"

    a = lec8.Fraction(1,4)
    b = lec8.Fraction(3,4)
    c = a + b
    assert isinstance(c, lec8.Fraction)
    assert float(c) == 1.0

    s = lec8.intSet()
    assert str(s) == "{}"
    s.insert(3)
    s.insert(4)
    assert s.member(3) is True
    s.remove(3)
    assert s.member(3) is False
