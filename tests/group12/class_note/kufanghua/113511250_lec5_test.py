import add_path  # if your repo requires this to set up sys.path
import mit_ocw_exercises.lec5_tuples_lists as lec5
import pytest

def test_quotient_and_remainder():
    assert lec5.quotient_and_remainder(10, 3) == (3, 1)
    assert lec5.quotient_and_remainder(17, 5) == (3, 2)
    assert lec5.quotient_and_remainder(8, 4) == (2, 0)
    assert lec5.quotient_and_remainder(22, 7) == (3, 1)

def test_get_data():
    data1 = ((5, "apple"), (3, "banana"), (9, "apple"), (7, "cherry"))
    assert lec5.get_data(data1) == (3, 9, 3)
    data2 = ((100, "x"), (200, "y"), (300, "x"), (50, "z"))
    assert lec5.get_data(data2) == (50, 300, 3)
    data3 = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    assert lec5.get_data(data3) == (1, 7, 2)
