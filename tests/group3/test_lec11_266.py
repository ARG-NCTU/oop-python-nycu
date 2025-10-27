import add_path
import mit_ocw_exercises.lec11_complexity_part2 as lec11
import pytest


def test_bisect_search1():
    testList = list(range(300))
    assert lec11.bisect_search1(testList, 128) == True
    assert lec11.bisect_search1(testList, 500) == False
    assert lec11.bisect_search1([None], 5) == False
    assert lec11.bisect_search1([90], 90) == True
    assert lec11.bisect_search1([64], 8) == False

def test_bisect_search2():
    testList = list(range(600))
    assert lec11.bisect_search2(testList, 512) == True
    assert lec11.bisect_search2(testList, 1000) == False
    assert lec11.bisect_search2([], 10) == False
    assert lec11.bisect_search2([80], 80) == True
    assert lec11.bisect_search2([55], 7) == False