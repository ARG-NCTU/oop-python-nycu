import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest

def test_linear_search():
    testList = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(testList, 3) == True
    assert lec10.linear_search(testList, 6) == False
    assert lec10.linear_search([], 1) == False
    assert lec10.linear_search([10], 10) == True
    assert lec10.linear_search([10], 5) == False

def test_search():
    testList = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.search(testList, 3) == True
    assert lec10.search(testList, 6) == False
    assert lec10.search(testList, 1) == True
    assert lec10.search(testList, 27) == True
    assert lec10.search(testList, 30) == False
    assert lec10.search([], 1) == False
    assert lec10.search([10], 10) == True
    assert lec10.search([10], 5) == False
    assert lec10.search([1,2,3,4,5], 4) == True

def test_isSubset():
    testSet = [1, 2, 3, 4, 5]
    testSet1 = [1, 5, 3]
    testSet2 = [1, 6]
    assert lec10.isSubset(testSet1, testSet) == True
    assert lec10.isSubset(testSet2, testSet) == False
    assert lec10.isSubset([], testSet) == True
    assert lec10.isSubset(testSet, testSet) == True
    assert lec10.isSubset([10], testSet) == False

def test_intersect():
    L1 = [1, 2, 3, 4, 5]
    L2 = [3, 4, 5, 6, 7]
    L3 = [6, 7, 8]
    L4 = [1, 1, 2, 2, 3]
    L5 = [2, 2, 3, 3, 4]
    assert lec10.intersect(L1, L2) == [3, 4, 5]
    assert lec10.intersect(L1, L3) == []
    assert lec10.intersect(L2, L3) == [6, 7]
    assert lec10.intersect(L4, L5) == [2, 3]
    assert lec10.intersect([], L1) == []
    assert lec10.intersect(L1, []) == []
    assert lec10.intersect([], []) == []
