import pytest
from lec10_complexity_part1 import linear_search, search, isSubset, intersect

testList = [1, 3, 4, 5, 9, 18, 27]

testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

def test_linear_search():
    assert linear_search(testList, 5) is True
    assert linear_search(testList, 1) is True  
    assert linear_search(testList, 27) is True 
    
    assert linear_search(testList, 6) is False
    assert linear_search(testList, 100) is False
    
    assert linear_search([], 5) is False

def test_search_sorted():
    assert search(testList, 5) is True
    assert search(testList, 27) is True
    
    assert search(testList, 6) is False 
    
    assert search(testList, 100) is False
    
    assert search([], 5) is False

def test_isSubset():
    assert isSubset(testSet1, testSet) is True
    
    assert isSubset(testSet2, testSet) is False
    
    assert isSubset([], testSet) is True
    
    assert isSubset([1], []) is False
    assert isSubset([], []) is True

def test_intersect():
    L1 = [1, 2, 3, 4]
    L2 = [3, 4, 5, 6]
    assert intersect(L1, L2) == [3, 4]

    L_no_match = [1, 2]
    L_no_match_2 = [3, 4]
    assert intersect(L_no_match, L_no_match_2) == []

    assert intersect(L1, []) == []
    assert intersect([], L2) == []

def test_intersect_with_duplicates():
    L1 = [1, 2, 2, 3, 5]
    L2 = [2, 2, 4, 5]
    
    assert sorted(intersect(L1, L2)) == [2, 5]