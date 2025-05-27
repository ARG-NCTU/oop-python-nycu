import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest
import time
import random

def test_linear_search():
    assert linear_search([1, 2, 3, 4], 3) == True
    assert linear_search([1, 2, 3, 4], 5) == False
    assert linear_search([], 1) == False

def test_search():
    assert search([1, 3, 5, 7], 3) == True
    assert search([1, 3, 5, 7], 2) == False
    assert search([1, 3, 5, 7], 8) == False
    assert search([], 1) == False

def test_isSubset():
    assert isSubset([1, 2], [1, 2, 3, 4]) == True
    assert isSubset([1, 5], [1, 2, 3]) == False
    assert isSubset([], [1, 2]) == True
    assert isSubset([], []) == True
    assert isSubset([1], []) == False
def test_intersect():
    assert intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersect([1, 1, 2], [1, 2, 2]) == [1, 2]
    assert intersect([], [1, 2]) == []
    assert intersect([1, 2], []) == []
    assert intersect([], []) == []  