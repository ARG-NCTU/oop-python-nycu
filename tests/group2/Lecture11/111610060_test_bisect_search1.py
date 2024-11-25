import pytest
import lec11_complexity_part2 as lec11

def test_bisect_search1():
    test_list = [1,2,4,5,6,8,9]
    assert lec11.bisect_search1(test_list, 6) == True
    assert lec11.bisect_search1(test_list, 5) == True
    assert lec11.bisect_search1(test_list, 11) == False
    assert lec11.bisect_search1(test_list, 3) == False
    assert lec11.bisect_search1([5], 5) == True
    with pytest.raises(IndexError):
        lec11.bisect_search1([], 10)
