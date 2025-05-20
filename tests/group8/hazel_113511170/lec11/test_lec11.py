#import add_path
import lec11 as lec11
import pytest

def test_bisect_search2():
    testList= [1,2,4,8,16,32,64,128,256,512]
    assert lec11.bisect_search2(testList, 128) == True
    assert lec11.bisect_search2(testList, 10) == False
    assert lec11.bisect_search2(testList, -1) == False
    assert lec11.bisect_search2([], 5) == False

def test_genSubsets():
    testSet = [1,2,3,4]
    subsets = lec11.genSubsets(testSet)
    assert subsets== [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3],[4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4]]

