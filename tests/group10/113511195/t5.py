import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest


def test_quotient_and_remainder():
    # fresh inputs / expected outputs
    assert lec5.quotient_and_remainder(37, 5) == (7, 2)
    assert lec5.quotient_and_remainder(41, 6) == (6, 5)
    assert lec5.quotient_and_remainder(42, 7) == (6, 0)
    assert lec5.quotient_and_remainder(99, 8) == (12, 3)
    assert lec5.quotient_and_remainder(100, 33) == (3, 1)