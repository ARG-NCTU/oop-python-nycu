import pytest
from lec5 import (
    quotient_and_remainder,
    get_data,
    sum_elem_method1,
    sum_elem_method2,
    remove_dups,
    remove_dups_new,
)

def test_quotient_and_remainder():
    assert quotient_and_remainder(10, 3) == (3, 1)
    assert quotient_and_remainder(20, 5) == (4, 0)
    assert quotient_and_remainder(7, 2) == (3, 1)

def test_get_data():
    test_data = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))
    result = get_data(test_data)
    assert result == (1, 7, 2)

    tswift = ((2014, "Katy"), (2014, "Harry"), (2012, "Jake"), (2010, "Taylor"), (2008, "Joe"))
    result = get_data(tswift)
    assert result == (2008, 2014, 5)

def test_sum_elem_method1():
    assert sum_elem_method1([1, 2, 3, 4]) == 10
    assert sum_elem_method1([0, 0, 0]) == 0
    assert sum_elem_method1([-1, -2, -3]) == -6

def test_sum_elem_method2():
    assert sum_elem_method2([1, 2, 3, 4]) == 10
    assert sum_elem_method2([0, 0, 0]) == 0
    assert sum_elem_method2([-1, -2, -3]) == -6

def test_remove_dups():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups(L1, L2)
    assert L1 == [2, 3, 4]
    assert L2 == [1, 2, 5, 6]

def test_remove_dups_new():
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 5, 6]
    remove_dups_new(L1, L2)
    assert L1 == [3, 4]
    assert L2 == [1, 2, 5, 6]