import add_path
import lec11 as lec11
import pytest

def test_bisect_search1():
    testList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert lec11.bisect_search1(testList, 0) == True
    assert lec11.bisect_search1(testList, 9) == True
    assert lec11.bisect_search1(testList, 10) == False
    assert lec11.bisect_search1(testList, -1) == False
    assert lec11.bisect_search1([3], 3) == True
    assert lec11.bisect_search1([3], 4) == False

def test_bisect_search2():
    testList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert lec11.bisect_search2(testList, 0) == True
    assert lec11.bisect_search2(testList, 9) == True
    assert lec11.bisect_search2(testList, 10) == False
    assert lec11.bisect_search2(testList, -1) == False
    assert lec11.bisect_search2([], 5) == False
    assert lec11.bisect_search2([3], 3) == True
    assert lec11.bisect_search2([3], 4) == False

def test_genSubsets():
    testSet = [1, 2, 3, 4]
    expected = [
        [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
        [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]
    ]
    result = lec11.genSubsets(testSet)
    # Sort inner lists and outer list for comparison
    assert sorted([sorted(sub) for sub in result]) == sorted([sorted(sub) for sub in expected])
