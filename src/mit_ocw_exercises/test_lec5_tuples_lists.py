# src/mit_ocw_exercises/test_lec5_tuples_lists.py

import math
import pytest
from .lec5_tuples_lists import (
    quotient_and_remainder,
    get_data,
    sum_elem_method1,
    sum_elem_method2,
    remove_dups,
    remove_dups_new,
)

# ---------- quotient_and_remainder ----------

@pytest.mark.parametrize(
    "x,y,q,r",
    [
        (5, 3, 1, 2),
        (10, 2, 5, 0),
        (0, 7, 0, 0),
        (17, 5, 3, 2),
        (-7, 3, -3, 2),   # Python // 是 floor 除法
        (7, -3, -3,  -2 % -3),  # 嚴格檢查 Python 定義
    ],
)
def test_qr_values(x, y, q, r):
    got_q, got_r = quotient_and_remainder(x, y)
    assert got_q == q
    assert got_r == r
    # 檢查一致性：x == q*y + r
    assert x == got_q * y + got_r

def test_qr_zero_division():
    with pytest.raises(ZeroDivisionError):
        quotient_and_remainder(5, 0)

# ---------- get_data ----------

def test_get_data_basic():
    test = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    assert get_data(test) == (1, 7, 2)

def test_get_data_more_unique():
    tswift = ((2014, "Katy"), (2014, "Harry"), (2012, "Jake"), (2010, "Taylor"), (2008, "Joe"))
    assert get_data(tswift) == (2008, 2014, 5)

def test_get_data_empty_raises():
    with pytest.raises(ValueError):
        get_data(tuple())

# ---------- sum methods ----------

@pytest.mark.parametrize("L", [[], [1], [1,2,3,4], list(range(100))])
def test_sum_methods(L):
    assert sum_elem_method1(L) == sum(L)
    assert sum_elem_method2(L) == sum(L)

# ---------- remove_dups / remove_dups_new ----------

@pytest.mark.parametrize(
    "L1,L2,expected",
    [
        ([1,2,3,4], [1,2,5,6], [3,4]),
        ([1,1,2,2,3], [2], [1,1,3]),
        ([], [1,2], []),
        ([5,5,5], [5], []),
        ([1,2,3], [], [1,2,3]),
    ],
)
def test_remove_dups_correct(L1, L2, expected):
    remove_dups(L1, L2)
    assert L1 == expected

@pytest.mark.parametrize(
    "L1,L2,expected",
    [
        ([1,2,3,4], [1,2,5,6], [3,4]),
        ([1,1,2,2,3], [2], [1,1,3]),
        ([5,5,5], [5], []),
    ],
)
def test_remove_dups_new_correct(L1, L2, expected):
    remove_dups_new(L1, L2)
    assert L1 == expected

