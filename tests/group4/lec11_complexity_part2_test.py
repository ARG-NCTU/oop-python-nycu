import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec11_complexity_part2 import bisect_search1, bisect_search2, genSubsets

def test_bisect_search1():
    testList = list(range(300))
    assert bisect_search1(testList, 128) == True
    assert bisect_search1(testList, 500) == False
    assert bisect_search1([None], 5) == False
    assert bisect_search1([90], 90) == True
    assert bisect_search1([64], 8) == False

def test_bisect_search2():
    testList = list(range(600))
    assert bisect_search2(testList, 512) == True
    assert bisect_search2(testList, 1000) == False
    assert bisect_search2([], 10) == False
    assert bisect_search2([80], 80) == True
    assert bisect_search2([55], 7) == False

def test_genSubsets():
    assert list(genSubsets([1, 2, 3])) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert list(genSubsets([1])) == [[], [1]]
    assert list(genSubsets([])) == [[]]
