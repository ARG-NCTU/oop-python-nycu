import pytest
import lec10_complexity_part1 as lec10
import math

def test_linear_search():
    testList = [1, 3, 4, 5, 9, 18, 27]
    assert lec10.linear_search(testList,1) == True
    assert lec10.linear_search(testList,3) == True
    assert lec10.linear_search(testList,27) == True
    assert lec10.linear_search(testList,2) == False
    testList = [2,2,2,2,2,6,7,8]
    assert lec10.linear_search(testList,1) == False
    assert lec10.linear_search(testList,3) == False
    assert lec10.linear_search(testList,27) == False
    assert lec10.linear_search(testList,2) == True
testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]
def test_subset():
    assert lec10.isSubset(testSet,testSet1) == False
    assert lec10.isSubset(testSet,testSet) == True
    assert lec10.isSubset(testSet1,testSet) == True
    assert lec10.isSubset(testSet,testSet2) == False
    assert lec10.isSubset(testSet2,testSet) == False
    assert lec10.isSubset(testSet2,testSet2) == True

def test_intersect():
    assert lec10.intersect(testSet,testSet1) == [1,3,5]
    assert lec10.intersect(testSet,testSet2) == [1]
    
    #
