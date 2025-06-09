import pytest
import lec11_complexity_part2 as lec11
import math

def test_bisect_search():
    testList = []
    for i in range(100):
        testList.append(i)
    assert lec11.bisect_search1(testList,76) == True
    assert lec11.bisect_search2(testList,76) == True
    assert lec11.bisect_search1(testList,100) == False
    assert lec11.bisect_search2(testList,100) == False

def test_gensubset():
    testSet = [1,2,3,4]
    assert lec11.genSubsets(testSet) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
    testSet2 = []
    assert lec11.genSubsets(testSet2) == [[]]
