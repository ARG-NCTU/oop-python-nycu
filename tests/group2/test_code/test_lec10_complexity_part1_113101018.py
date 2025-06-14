import pytest
import lec10_complexity_part1 as lec10
import math


# ---------- linear_search ----------
def test_linear_search():
    num_list = [2, 4, 6, 8, 10, 12, 14]
    assert lec10.linear_search(num_list, 2)   is True
    assert lec10.linear_search(num_list, 14)  is True
    assert lec10.linear_search(num_list, 9)   is False
    assert lec10.linear_search(num_list, 100) is False


# ---------- isSubset ----------
def test_subset():
    full_set   = [2, 4, 6, 8, 10]
    sub_set_ok = [2, 8]
    sub_set_ng = [1, 2]

    assert lec10.isSubset(full_set, sub_set_ok) is False       # 2,8 not ⊆ 2,4,6,8,10 → order matters: first arg L1!
    assert lec10.isSubset(full_set, full_set)   is True
    assert lec10.isSubset(sub_set_ok, full_set) is True
    assert lec10.isSubset(full_set, sub_set_ng) is False


# ---------- intersect ----------
def test_intersect():
    list_a = [2, 4, 6, 8, 10]
    list_b = [1, 2, 5, 6, 11]
    list_c = [3, 7, 9]

    assert lec10.intersect(list_a, list_b) == [2, 6]
    assert lec10.intersect(list_a, list_c) == []

