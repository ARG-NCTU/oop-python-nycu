import add_path
import lec10 as lec10
import pytest

# -------- linear_search --------
def test_linear_search():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(L, 3)
    assert lec10.linear_search(L, 18)
    assert not lec10.linear_search(L, 100)
    assert not lec10.linear_search([], 1)

def test_linear_search_edge_cases():
    assert lec10.linear_search([1], 1)
    assert not lec10.linear_search([1], 2)
    assert lec10.linear_search([5, 5, 5], 5)
    assert not lec10.linear_search([5, 5, 5], 6)

# -------- search (recursive or binary) --------
def test_search():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.search(L, 3)
    assert lec10.search(L, 4)
    assert not lec10.search(L, 2)
    assert not lec10.search([], 1)
    assert not lec10.search([1, 2, 3], 0)

def test_search_edge_cases():
    assert lec10.search([1], 1)
    assert not lec10.search([1], 0)
    assert lec10.search([2, 2, 2, 2], 2)
    assert not lec10.search([2, 2, 2, 2], 3)

# -------- isSubset --------
def test_isSubset():
    assert lec10.isSubset([1, 3], [1, 2, 3, 4])
    assert lec10.isSubset([1, 5, 3], [1, 2, 3, 4, 5])
    assert not lec10.isSubset([1, 6], [1, 2, 3, 4, 5])
    assert lec10.isSubset([], [1, 2, 3])
    assert not lec10.isSubset([1], [])

def test_isSubset_edge_cases():
    assert lec10.isSubset([1, 1, 2], [1, 2, 2, 3])  # duplicate allowed if count is enough
    assert lec10.isSubset([], [])  # empty subset of empty set is valid
    assert lec10.isSubset([], [1])  # empty is subset of any

# -------- intersect --------
def test_intersect():
    assert lec10.intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert lec10.intersect([1, 2], [3, 4]) == []
    assert lec10.intersect([], [1, 2]) == []
    assert lec10.intersect([1, 1, 2], [1, 2, 2]) == [1, 2]

def test_intersect_edge_cases():
    assert lec10.intersect([1], [1]) == [1]
    assert lec10.intersect([1], [2]) == []
    assert lec10.intersect([1, 2, 3], [3, 2, 1]) == [1, 2, 3]  # order may vary depending on implementation
    assert lec10.intersect([], []) == []
