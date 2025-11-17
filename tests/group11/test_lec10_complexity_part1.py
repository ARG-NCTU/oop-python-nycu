import pytest
from lec10_complexity_part1 import linear_search, search, isSubset, intersect

# -----------------
# 測試資料 (全域)
# -----------------
# 用於 linear_search 和 search
testList = [1, 3, 4, 5, 9, 18, 27]

# 用於 isSubset 和 intersect
testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

# -----------------
# 測試 linear_search
# -----------------
def test_linear_search():
    """測試 linear_search (標準線性搜尋)"""
    # 測試找到
    assert linear_search(testList, 5) is True
    assert linear_search(testList, 1) is True  # 測試第一個
    assert linear_search(testList, 27) is True # 測試最後一個
    
    # 測試沒找到
    assert linear_search(testList, 6) is False
    assert linear_search(testList, 100) is False
    
    # 測試空列表
    assert linear_search([], 5) is False

# -----------------
# 測試 search
# -----------------
def test_search_sorted():
    """測試 search (假設列表已排序)"""
    # 測試找到
    assert search(testList, 5) is True
    assert search(testList, 27) is True # 測試最後一個
    
    # 測試沒找到 (應提早退出)
    # L[i] > e (例如 i=4, L[i]=9, e=6)
    assert search(testList, 6) is False 
    
    # 測試沒找到 (比所有都大)
    assert search(testList, 100) is False
    
    # 測試空列表
    assert search([], 5) is False

# -----------------
# 測試 isSubset
# -----------------
def test_isSubset():
    """測試 isSubset"""
    # 測試為 True (testSet1 是 testSet 的子集)
    assert isSubset(testSet1, testSet) is True
    
    # 測試為 False (testSet2 不是 testSet 的子集, 因為 6)
    assert isSubset(testSet2, testSet) is False
    
    # 測試空集 (空集是任何集合的子集)
    assert isSubset([], testSet) is True
    
    # 測試某集合是空集的子集 (False, 除非 L1 也是空集)
    assert isSubset([1], []) is False
    assert isSubset([], []) is True

# -----------------
# 測試 intersect
# -----------------
def test_intersect():
    """測試 intersect (交集)"""
    L1 = [1, 2, 3, 4]
    L2 = [3, 4, 5, 6]
    # 結果的順序取決於 L1，所以 [3, 4] 是確定的
    assert intersect(L1, L2) == [3, 4]

    L_no_match = [1, 2]
    L_no_match_2 = [3, 4]
    assert intersect(L_no_match, L_no_match_2) == []

    # 測試空列表
    assert intersect(L1, []) == []
    assert intersect([], L2) == []

def test_intersect_with_duplicates():
    """測試 intersect (含重複項)"""
    # 你的 intersect 邏輯會處理重複
    L1 = [1, 2, 2, 3, 5]
    L2 = [2, 2, 4, 5]
    
    # tmp 會是 [2, 2, 2, 2, 5]
    # res 會是 [2, 5]
    # 為了保險起見，我們用 sorted() 來比較，忽略順序
    assert sorted(intersect(L1, L2)) == [2, 5]