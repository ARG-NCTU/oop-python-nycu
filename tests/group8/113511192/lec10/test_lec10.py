import add_path
import lec10 as lec10
import pytest
import time
import random
def test_linear_search():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(L, 3) == True
    assert lec10.linear_search(L, 18) == True
    assert lec10.linear_search(L, 100) == False
    assert lec10.linear_search([], 1) == False

def test_search():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.search(L, 3) == True
    assert lec10.search(L, 4) == True
    assert lec10.search(L, 2) == False
    assert lec10.search([], 1) == False
    assert lec10.search([1, 2, 3], 0) == False

def test_isSubset():
    assert lec10.isSubset([1, 3], [1, 2, 3, 4]) == True
    assert lec10.isSubset([1, 5, 3], [1, 2, 3, 4, 5]) == True
    assert lec10.isSubset([1, 6], [1, 2, 3, 4, 5]) == False
    assert lec10.isSubset([], [1, 2, 3]) == True
    assert lec10.isSubset([1], []) == False

def test_intersect():
    assert lec10.intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert lec10.intersect([1, 2], [3, 4]) == []
    assert lec10.intersect([], [1, 2]) == []
    assert lec10.intersect([1, 1, 2], [1, 2, 2]) == [1, 2]
