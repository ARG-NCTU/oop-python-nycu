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