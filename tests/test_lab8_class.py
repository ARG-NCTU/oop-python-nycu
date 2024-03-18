import add_path
import mit_ocw_exercises.lec8_classes as lc

def test_5_frac():
    quarter = lc.Fraction(1, 4)
    half = lc.Fraction(1,2)
    assert quarter.num == 1
    assert quarter.denom == 4
    sum = half.__add__(quarter)
    assert sum.num == 6
    assert sum.denom == 8
