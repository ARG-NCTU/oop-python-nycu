import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest
import time
import random
def test_linear_search():
    assert linear_search([10, 20, 30, 40], 20) == True
    assert linear_search([10, 20, 30, 40], 50) == False
    assert linear_search([], 0) == False

def test_search():
    assert search([2, 4, 6, 8, 10], 6) == True
    assert search([2, 4, 6, 8, 10], 5) == False
    assert search([2, 4, 6, 8, 10], 11) == False
    assert search([], 3) == False

def test_isSubset():
    assert isSubset([3, 5], [1, 3, 5, 7]) == True
    assert isSubset([3, 6], [1, 3, 5, 7]) == False
    assert isSubset([], [10, 20]) == True
    assert isSubset([], []) == True
    assert isSubset([4], []) == False

def test_intersect():
    assert intersect([7, 8, 9], [8, 9, 10]) == [8, 9]
    assert intersect([5, 5, 6], [5, 6, 6]) == [5, 6]
    assert intersect([], [3, 4]) == []
    assert intersect([3, 4], []) == []
    assert intersect([], []) == []
