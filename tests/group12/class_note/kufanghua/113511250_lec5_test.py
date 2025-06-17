import add_path  # if your repo requires this to set up sys.path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest

def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(10, 3) == (3, 1)
    assert lec5.quotient_and_remainder(17, 5) == (3, 2)
    assert lec5.quotient_and_remainder(8, 4) == (2, 0)
    assert lec5.quotient_and_remainder(22, 7) == (3, 1)
