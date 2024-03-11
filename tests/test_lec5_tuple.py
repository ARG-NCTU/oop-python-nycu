import add_path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest


# please write a test for quotient_and_remainder function
def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(20, 6) == (3, 2)
    assert lec5.quotient_and_remainder(20, 7) == (2, 6)
    assert lec5.quotient_and_remainder(20, 8) == (2, 4)
    assert lec5.quotient_and_remainder(20, 9) == (2, 2)
    assert lec5.quotient_and_remainder(20, 10) == (2, 0)



