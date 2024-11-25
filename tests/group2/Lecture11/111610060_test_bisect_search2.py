import pytest
import lec11_complexity_part2 as lec11

def test_bisect_search2():
    test_list = [2,4,6,8,10]
    assert lec11.bisect_search1(test_list, 6) == True
    assert lec11.bisect_search1(test_list, 5) == False
    assert lec11.bisect_search1(test_list, 11) == False
    assert lec11.bisect_search1(test_list, 3) == False
    assert lec11.bisect_search1([], 10) == False
    assert lec11.bisect_search1([1], 1) == True