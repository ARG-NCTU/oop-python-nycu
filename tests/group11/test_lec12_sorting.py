import pytest
from lec12_sorting import bubble_sort_np, selection_sort_np, merge_sort_np, merge_np

# -----------------
# 測試 Bubble Sort (有回傳值)
# -----------------
def test_bubble_sort_np():
    # 測試基本案例
    L1 = [5, 1, 4, 2, 8]
    assert bubble_sort_np(L1) == [1, 2, 4, 5, 8]
    
    # 測試已排序
    L2 = [1, 2, 3]
    assert bubble_sort_np(L2) == [1, 2, 3]
    
    # 測試反向
    L3 = [3, 2, 1]
    assert bubble_sort_np(L3) == [1, 2, 3]
    
    # 測試含重複
    L4 = [2, 1, 3, 2, 1]
    assert bubble_sort_np(L4) == [1, 1, 2, 2, 3]
    
    # 測試含負數
    L5 = [-10, 5, 0, -2]
    assert bubble_sort_np(L5) == [-10, -2, 0, 5]
    
    # 測試邊界：空列表
    assert bubble_sort_np([]) == []
    
    # 測試邊界：單一元素
    assert bubble_sort_np([42]) == [42]

# -----------------
# 測試 Selection Sort (就地修改, 無回傳值)
# -----------------
def test_selection_sort_np():
    # 測試基本案例
    L1 = [5, 1, 4, 2, 8]
    return_val = selection_sort_np(L1) # 呼叫函式
    assert return_val is None           # 1. 斷言它沒有回傳值
    assert L1 == [1, 2, 4, 5, 8]      # 2. 斷言「原始列表」被修改了
    
    # 測試反向
    L3 = [3, 2, 1]
    selection_sort_np(L3)
    assert L3 == [1, 2, 3]
    
    # 測試含重複
    L4 = [2, 1, 3, 2, 1]
    selection_sort_np(L4)
    assert L4 == [1, 1, 2, 2, 3]
    
    # 測試邊界：空列表
    L_empty = []
    selection_sort_np(L_empty)
    assert L_empty == []
    
    # 測試邊界：單一元素
    L_single = [42]
    selection_sort_np(L_single)
    assert L_single == [42]

# -----------------
# 測試 Merge Sort (有回傳值, 不修改原列表)
# -----------------
def test_merge_sort_np():
    # 測試基本案例
    L1 = [5, 1, 4, 2, 8]
    L1_original = L1[:] # 建立一個複本
    
    result = merge_sort_np(L1)
    assert result == [1, 2, 4, 5, 8]    # 1. 斷言回傳值正確
    assert L1 == L1_original          # 2. 斷言原始列表「未被修改」
    
    # 測試反向
    L3 = [3, 2, 1]
    assert merge_sort_np(L3) == [1, 2, 3]
    
    # 測試含重複
    L4 = [2, 1, 3, 2, 1]
    assert merge_sort_np(L4) == [1, 1, 2, 2, 3]
    
    # 測試邊界：空列表
    assert merge_sort_np([]) == []
    
    # 測試邊界：單一元素
    assert merge_sort_np([42]) == [42]

# -----------------
# 測試 merge 輔助函式
# -----------------
def test_merge_np():
    # 測試標準合併
    left = [1, 3, 5]
    right = [2, 4, 6]
    assert merge_np(left, right) == [1, 2, 3, 4, 5, 6]
    
    # 測試不均勻合併 (右邊比較長)
    left_short = [1, 5]
    right_long = [2, 4, 6, 8]
    assert merge_np(left_short, right_long) == [1, 2, 4, 5, 6, 8]
    
    # 測試不均勻合併 (左邊比較長)
    left_long = [1, 5, 7, 9]
    right_short = [2, 6]
    assert merge_np(left_long, right_short) == [1, 2, 5, 6, 7, 9]
    
    # 測試含空列表
    assert merge_np([], [1, 2]) == [1, 2]
    assert merge_np([1, 2], []) == [1, 2]
    assert merge_np([], []) == []