import pytest
import lec5_tuples_lists as lec5
import math


def test_quoNrem():
    assert lec5.quotient_and_remainder(13, 4) == (3, 1)
    assert lec5.quotient_and_remainder(9,  3) == (3, 0)
    assert lec5.quotient_and_remainder(-10, 4) == (-3, 2)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        lec5.quotient_and_remainder(5, 0)


def test_getdata():
    assert lec5.get_data(((3, "x"), (9, "y"), (0, "x"), (5, "z"))) == (0, 9, 3)
    assert lec5.get_data(((-5, "m"), (-1, "n"), (5, "m"), (10, "o"))) == (-5, 10, 3)
    assert lec5.get_data(((1999, "A"), (2000, "B"), (2000, "C"),
                          (1998, "A"), (2005, "D"))) == (1998, 2005, 4)


def test_remove_dup():
    L1 = [4, 5, 6, 7]
    L2 = [5, 7, 8]
    L3 = [7, 9]
    lec5.remove_dups_new(L1, L2)
    assert L1 == [4, 6]          # 5、7 被移除
    lec5.remove_dups_new(L2, L3)
    assert L2 == [5, 8]          # 7 被移除

