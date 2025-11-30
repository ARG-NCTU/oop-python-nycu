import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest

def test_linear_search():
    lst = [3, 1, 4, 2, 5]
    assert lec10.linear_search(lst, 4) == True
    assert lec10.linear_search(lst, 6) == False
    assert lec10.linear_search([], 1) == False


def test_search():
    lst = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.search(lst, 5) == True
    assert lec10.search(lst, 2) == False
    assert lec10.search(lst, 30) == False
    assert lec10.search([], 1) == False

def test_isSubset():
    assert lec10.isSubset([1, 2], [2, 1, 3]) == True
    assert lec10.isSubset([1, 4], [2, 1, 3]) == False
    assert lec10.isSubset([], [1, 2, 3]) == True
    assert lec10.isSubset([1, 2], []) == False


def test_intersect():
    assert lec10.intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert lec10.intersect([1, 1, 2], [1, 2, 2]) == [1, 2]
    assert lec10.intersect([5, 6], [7, 8]) == []
    assert lec10.intersect([], [1, 2]) == []


