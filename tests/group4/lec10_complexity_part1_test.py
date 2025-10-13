import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec10_complexity_part1 import linear_search, search, isSubset, intersect


def test_linear_search():
    testList = [1, 3, 4, 5, 9, 18, 27]
    assert linear_search(testList, 3) == True
    assert linear_search(testList, 6) == False
    assert linear_search([], 1) == False
    assert linear_search([10], 10) == True
    assert linear_search([10], 5) == False

def test_search():
    testList = [1, 3, 4, 5, 9, 18, 27]
    assert search(testList, 3) == True
    assert search(testList, 6) == False
    assert search(testList, 1) == True
    assert search(testList, 27) == True
    assert search(testList, 30) == False
    assert search([], 1) == False
    assert search([10], 10) == True
    assert search([10], 5) == False

def test_isSubset():
    testSet = [1, 2, 3, 4, 5]
    testSet1 = [1, 5, 3]
    testSet2 = [1, 6]
    assert isSubset(testSet1, testSet) == True
    assert isSubset(testSet2, testSet) == False
    assert isSubset([], testSet) == True
    assert isSubset(testSet, testSet) == True
    assert isSubset([10], testSet) == False

def test_intersect():
    L1 = [1, 2, 3, 4, 5]
    L2 = [3, 4, 5, 6, 7]
    L3 = [6, 7, 8]
    L4 = [1, 1, 2, 2, 3]
    L5 = [2, 2, 3, 3, 4]
    assert intersect(L1, L2) == [3, 4, 5]
    assert intersect(L1, L3) == []
    assert intersect(L2, L3) == [6, 7]
    assert intersect(L4, L5) == [2, 3]
    assert intersect([], L1) == []
    assert intersect(L1, []) == []
    assert intersect([], []) == []