import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lec11_complexity_part2 import bisect_search1, bisect_search2, genSubsets

# -----------------
# 測試資料 (全域)
# -----------------
# 一個大列表
L_100 = list(range(100)) 
# 一個小列表 (奇數長度)
L_small = [1, 3, 5, 7, 9] 
# 一個小列表 (偶數長度)
L_even = [10, 20, 30, 40] 

# -----------------
# 測試 bisect_search1 (切片版本)
# -----------------
def test_bisect_search1():
    # 測試找到
    assert bisect_search1(L_100, 76) is True
    assert bisect_search1(L_small, 5) is True  # 找中間
    assert bisect_search1(L_small, 1) is True  # 找開頭
    assert bisect_search1(L_small, 9) is True  # 找結尾
    assert bisect_search1(L_even, 20) is True

    # 測試沒找到
    assert bisect_search1(L_small, 6) is False  # 沒找到 (在範圍內)
    assert bisect_search1(L_small, 100) is False # 沒找到 (太大)
    assert bisect_search1(L_small, 0) is False   # 沒找到 (太小)

    # 測試邊界條件
    #assert bisect_search1([], 5) is False        # 空列表
    assert bisect_search1([5], 5) is True       # 單一元素 (找到)
    assert bisect_search1([5], 4) is False      # 單一元素 (沒找到)

# -----------------
# 測試 bisect_search2 (索引版本)
# -----------------
def test_bisect_search2():
    # 測試案例應該和 search1 完全一樣，因為它們的「功能」相同
    
    # 測試找到
    assert bisect_search2(L_100, 76) is True
    assert bisect_search2(L_small, 5) is True  # 找中間
    assert bisect_search2(L_small, 1) is True  # 找開頭
    assert bisect_search2(L_small, 9) is True  # 找結尾
    assert bisect_search2(L_even, 20) is True

    # 測試沒找到
    assert bisect_search2(L_small, 6) is False  # 沒找到 (在範圍內)
    assert bisect_search2(L_small, 100) is False # 沒找到 (太大)
    assert bisect_search2(L_small, 0) is False   # 沒找到 (太小)

    # 測試邊界條件
    assert bisect_search2([], 5) is False        # 空列表
    assert bisect_search2([5], 5) is True       # 單一元素 (找到)
    assert bisect_search2([5], 4) is False      # 單一元素 (沒找到)

# -----------------
# 測試 genSubsets (產生子集)
# -----------------

def test_genSubsets():
    """
    測試 genSubsets (產生冪集合)
    我們不應該依賴子集的順序，所以最好的方法是
    1. 把每個子集排序
    2. 把排好序的子集列表再排序
    3. 跟預期的結果 (也經過同樣處理) 比較
    """
    
    # 測試空列表
    result_empty = genSubsets([])
    assert result_empty == [[]] # 規範定義

    # 測試單一元素
    result_one = genSubsets([1])
    # [[]] + [[1]]
    expected_one = sorted([[], [1]])
    # 把結果也排序，確保順序一致
    sorted_result_one = sorted([sorted(sub) for sub in result_one])
    assert sorted_result_one == expected_one

    # 測試兩個元素
    result_two = genSubsets([1, 2])
    # [[]] + [[1]] + [[2], [1, 2]]
    expected_two = sorted([[], [1], [2], [1, 2]])
    sorted_result_two = sorted([sorted(sub) for sub in result_two])
    assert len(result_two) == 4 # 2^2
    assert sorted_result_two == expected_two

    # 測試三個元素
    result_three = genSubsets([1, 2, 3])
    expected_three = sorted([
        [], [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3]
    ])
    sorted_result_three = sorted([sorted(sub) for sub in result_three])
    assert len(result_three) == 8 # 2^3
    assert sorted_result_three == expected_three