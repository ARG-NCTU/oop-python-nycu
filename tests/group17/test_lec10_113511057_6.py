import lec_10.py as lec10
import pytest
import time
import random
def test_linear_search():
    assert lec10.linear_search([10, 20, 30, 40], 20) == True
    assert lec10.linear_search([10, 20, 30, 40], 50) == False
    assert lec10.linear_search([], 0) == False

def test_search():
    assert lec10.search([2, 4, 6, 8, 10], 6) == True
    assert lec10.search([2, 4, 6, 8, 10], 5) == False
    assert lec10.search([2, 4, 6, 8, 10], 11) == False
    assert lec10.search([], 3) == False

def test_isSubset():
    assert lec10.isSubset([3, 5], [1, 3, 5, 7]) == True
    assert lec10.isSubset([3, 6], [1, 3, 5, 7]) == False
    assert lec10.isSubset([], [10, 20]) == True
    assert lec10.isSubset([], []) == True
    assert lec10.isSubset([4], []) == False

def test_intersect():
    assert lec10.intersect([7, 8, 9], [8, 9, 10]) == [8, 9]
    assert lec10.intersect([5, 5, 6], [5, 6, 6]) == [5, 6]
    assert lec10.intersect([], [3, 4]) == []
    assert lec10.intersect([3, 4], []) == []
    assert lec10.intersect([], []) == []
