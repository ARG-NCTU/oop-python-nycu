from lec11_final import *

def test_bisect_search1():
    L = list(range(100))
    assert bisect_search1(L, 76) == True
    assert bisect_search1(L, -1) == False
    assert bisect_search1([], 0) == False

def test_bisect_search2():
    L = list(range(100))
    assert bisect_search2(L, 76) == True
    assert bisect_search2(L, 100) == False
    assert bisect_search2([], 1) == False

def test_genSubsets():
    result = genSubsets([1, 2])
    expected = [[], [1], [2], [1, 2]]
    assert sorted(result) == sorted(expected)

    result = genSubsets([])
    assert result == [[]]

    result = genSubsets([1])
    assert result == [[], [1]]
