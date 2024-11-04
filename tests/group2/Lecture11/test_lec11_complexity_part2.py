import add_path
import lec11_complexity_part2 as lec11
import pytest

def test_bisect_search2():
    testList= [0,1,2,3,4,5,6,7,8,9]
    assert lec11.bisect_search2(testList, 5) == True
    assert lec11.bisect_search2(testList, 10) == False
    assert lec11.bisect_search2(testList, -1) == False
    assert lec11.bisect_search2([], 5) == False

def test_genSubsets():
    testSet = [1,2,3,4]
    subsets = lec11.genSubsets(testSet)
    assert subsets== [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]]

