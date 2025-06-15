import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest


def test_linear_search():
    assert lec10.linear_search([1, 2, 3, 4], 3) is True
    assert lec10.linear_search([1, 2, 3, 4], 5) is False
    assert lec10.linear_search([], 1) is False

def test_search():
    assert lec10.search([1, 2, 3, 4, 5], 3) is True
    assert lec10.search([1, 2, 3, 4, 5], 6) is False
    assert lec10.search([], 1) is False
    # test for sorted input (should stop early)
    assert lec10.search([1, 2, 4, 10], 5) is False

def test_isSubset():
    assert lec10.isSubset([1, 2], [1, 2, 3]) is True
    assert lec10.isSubset([1, 4], [1, 2, 3]) is False
    assert lec10.isSubset([], [1, 2, 3]) is True
    assert lec10.isSubset([1], []) is False

def test_intersect():
    assert lec10.intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert lec10.intersect([1, 2], [3, 4]) == []
    assert lec10.intersect([], [1, 2]) == []
    assert lec10.intersect([1, 2, 2], [2, 2, 3]) == [2]

