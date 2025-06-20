from src.mit_ocw_exercises.lec8_classes import Coordinate, Fraction, intSet

def test_coordinate():
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    assert c1.distance(c2) == 5.0
    assert str(c1) == "<3,4>"
    assert str(c2) == "<0,0>"
    # Symmetry
    assert c1.distance(c2) == c2.distance(c1)
def test_fraction():
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b
    assert isinstance(c, Fraction)
    assert str(c) == "16/16" or str(c) == "4/4"  # Depending on implementation
    assert float(c) == 1.0
    d = b - a
    assert isinstance(d, Fraction)
    assert str(d) == "8/16" or str(d) == "2/4"
    assert float(d) == 0.5
    inv = b.inverse()
    assert str(inv) == "4/3"
    # Test assertion error for non-int input
    try:
        Fraction(1.5, 2)
        assert False, "Should raise AssertionError for non-integer numerator"
    except AssertionError:
        pass
def test_intSet():
    s = intSet()
    assert str(s) == "{}"
    s.insert(3)
    s.insert(4)
    s.insert(3)  # Duplicate
    assert str(s) == "{3,4}"
    assert s.member(3) is True
    assert s.member(5) is False
    s.insert(6)
    assert str(s) == "{3,4,6}"
    s.remove(3)
    assert str(s) == "{4,6}"
    try:
        s.remove(3)
        assert False, "Should raise ValueError when removing non-member"
    except ValueError as e:
        assert str(e) == "3 not found"

if __name__ == "__main__":
    test_coordinate()
    test_fraction()
    test_intSet()
    print("All tests passed.")
