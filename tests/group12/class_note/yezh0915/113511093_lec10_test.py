import pytest
#from src.mit_ocw_exercises.lec10_complexity_part1 import linear_search, search, isSubset, intersect

def test_linear_search():
    assert linear_search([1, 2, 3, 4], 3) is True
    assert linear_search([1, 2, 3, 4], 5) is False
    assert linear_search([], 1) is False

def test_search():
    assert search([1, 2, 3, 4, 5], 3) is True
    assert search([1, 2, 3, 4, 5], 6) is False
    assert search([], 1) is False
    # test for sorted input (should stop early)
    assert search([1, 2, 4, 10], 5) is False

def test_isSubset():
    assert isSubset([1, 2], [1, 2, 3]) is True
    assert isSubset([1, 4], [1, 2, 3]) is False
    assert isSubset([], [1, 2, 3]) is True
    assert isSubset([1], []) is False

def test_intersect():
    assert intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersect([1, 2], [3, 4]) == []
    assert intersect([], [1, 2]) == []
    assert intersect([1, 2, 2], [2, 2, 3]) == [2]

