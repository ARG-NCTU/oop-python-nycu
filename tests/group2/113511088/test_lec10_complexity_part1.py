# -*- coding: utf-8 -*-
import pytest
import lec10_complexity_part1 as lec10

def test_linear_search_found_and_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(L, 4) is True
    assert lec10.linear_search(L, 27) is True
    assert lec10.linear_search(L, 2) is False
    assert lec10.linear_search([], 1) is False


def test_search_sorted_list_behavior():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.search(L, 1) is True
    assert lec10.search(L, 27) is True
    assert lec10.search(L, 8) is False     # stops early at 9
    assert lec10.search(L, -10) is False   # stops early at 1
    assert lec10.search([], 1) is False


def test_isSubset_basic():
    testSet = [1, 2, 3, 4, 5]
    testSet1 = [1, 5, 3]
    testSet2 = [1, 6]

    assert lec10.isSubset(testSet1, testSet) is True
    assert lec10.isSubset(testSet2, testSet) is False
    assert lec10.isSubset([], testSet) is True
    assert lec10.isSubset([1, 1], [1]) is True  # duplicates in L1 still "match" by membership


def test_intersect_unique_and_order_from_L1():
    assert lec10.intersect([1, 2, 3], [2, 4, 3]) == [2, 3]
    assert lec10.intersect([2, 2, 3, 2], [2, 3, 4, 2]) == [2, 3]
    assert lec10.intersect([], [1, 2]) == []
    assert lec10.intersect([1, 2], []) == []
    assert lec10.intersect([1, 1, 1], [1]) == [1]


def test_intersect_does_not_modify_inputs():
    L1 = [1, 2, 2, 3]
    L2 = [2, 3, 4, 2]
    before1 = L1.copy()
    before2 = L2.copy()
    _ = lec10.intersect(L1, L2)
    assert L1 == before1
    assert L2 == before2
