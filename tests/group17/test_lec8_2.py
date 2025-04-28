def test_Fraction():
    print("Testing Fraction...")
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    c = a + b
    assert str(c) == "16/16"  # not reduced
    assert float(c) == 1.0

    d = b - a
    assert str(d) == "8/16"  # 2/4 not reduced

    inv = b.inverse()
    assert str(inv) == "4/3"
    assert abs(float(inv) - 1.33333) < 1e-4

    try:
        invalid = Fraction(3.14, 2.7)
        assert False, "Should have raised AssertionError"
    except AssertionError:
        pass

    print("Fraction tests passed.\n")
test_Fraction()

