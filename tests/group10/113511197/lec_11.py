
import pytest
from lec11_complexity_part2 import bisect_search1, bisect_search2, genSubsets


L_100 = list(range(100)) 

L_small = [1, 3, 5, 7, 9] 

L_even = [10, 20, 30, 40] 

def test_bisect_search1():
   
    assert bisect_search1(L_100, 76) is True
    assert bisect_search1(L_small, 5) is True  # 找中間
    assert bisect_search1(L_small, 1) is True  # 找開頭
    assert bisect_search1(L_small, 9) is True  # 找結尾
    assert bisect_search1(L_even, 20) is True

    assert bisect_search1(L_small, 6) is False  # 沒找到 (在範圍內)
    assert bisect_search1(L_small, 100) is False # 沒找到 (太大)
    assert bisect_search1(L_small, 0) is False   # 沒找到 (太小)

    assert bisect_search1([5], 5) is True       # 單一元素 (找到)
    assert bisect_search1([5], 4) is False      # 單一元素 (沒找到)


def test_bisect_search2():

    assert bisect_search2(L_100, 76) is True
    assert bisect_search2(L_small, 5) is True  # 找中間
    assert bisect_search2(L_small, 1) is True  # 找開頭
    assert bisect_search2(L_small, 9) is True  # 找結尾
    assert bisect_search2(L_even, 20) is True

    assert bisect_search2(L_small, 6) is False  # 沒找到 (在範圍內)
    assert bisect_search2(L_small, 100) is False # 沒找到 (太大)
    assert bisect_search2(L_small, 0) is False   # 沒找到 (太小)

    assert bisect_search2([], 5) is False        # 空列表
    assert bisect_search2([5], 5) is True       # 單一元素 (找到)
    assert bisect_search2([5], 4) is False      # 單一元素 (沒找到)



def test_genSubsets():

    result_empty = genSubsets([])
    assert result_empty == [[]] 
    result_one = genSubsets([1])

    expected_one = sorted([[], [1]])

    sorted_result_one = sorted([sorted(sub) for sub in result_one])
    assert sorted_result_one == expected_one

    result_two = genSubsets([1, 2])

    expected_two = sorted([[], [1], [2], [1, 2]])
    sorted_result_two = sorted([sorted(sub) for sub in result_two])
    assert len(result_two) == 4 
    assert sorted_result_two == expected_two
    result_three = genSubsets([1, 2, 3])
    expected_three = sorted([
        [], [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3]
    ])
    sorted_result_three = sorted([sorted(sub) for sub in result_three])
    assert len(result_three) == 8 
    assert sorted_result_three == expected_three