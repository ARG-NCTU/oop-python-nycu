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
    assert lec5.quotient_and_remainder(20, 11) == (1, 9)
    assert lec5.quotient_and_remainder(20, 12) == (1, 8)
    assert lec5.quotient_and_remainder(20, 13) == (1, 7)
    assert lec5.quotient_and_remainder(20, 14) == (1, 6)
    assert lec5.quotient_and_remainder(20, 15) == (1, 5)


