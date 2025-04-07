import add_path
import mit_ocw_exercises.lec11_complexity_part2 as lec11
import pytest

def test_bisect_search2():
    testList= [0,1,2,3,4,5,6,7,8,9]
    assert lec11.bisect_search2(testList, 7) == True
    assert lec11.bisect_search2(testList, 11) == False
    assert lec11.bisect_search2(testList, -8) == False
    assert lec11.bisect_search2([], 1) == False

def test_genSubsets():
    testSet = [1,2,3]
    subsets = lec11.genSubsets(testSet)
    assert subsets== [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]