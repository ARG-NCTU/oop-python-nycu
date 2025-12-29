import pytest
import lec10_complexity_part1 as lec

# ==========================================
# 1. Linear Search (線性搜尋)
# 適用於任何無序列表，O(N)
# ==========================================

@pytest.mark.parametrize(
    "L, e, expect",
    [
        # --- 基礎整數測試 ---
        ([], 10, False),                  # 空列表
        ([10], 10, True),                 # 單一元素命中
        ([10], 20, False),                # 單一元素未命中
        ([5, 2, 9, 1, 7], 9, True),       # 一般命中
        ([5, 2, 9, 1, 7], 3, False),      # 一般未命中
        
        # --- 重複元素 ---
        ([1, 2, 2, 2, 3], 2, True),       # 列表中有多個目標
        
        # --- 邊界位置 ---
        ([10, 20, 30, 40], 10, True),     # 頭部命中
        ([10, 20, 30, 40], 40, True),     # 尾部命中
        
        # --- 不同資料型態 (Python list 特性) ---
        (["apple", "banana", "cherry"], "banana", True), # 字串搜尋
        (["a", "b", "c"], "z", False),                   # 字串未命中
    ]
)
def test_linear_search_comprehensive(L, e, expect):
    assert lec.linear_search(L, e) == expect


# ==========================================
# 2. Search (針對已排序列表的優化搜尋)
# 假設 L 遞增排序，O(N) 但有早停機制
# ==========================================

@pytest.mark.parametrize(
    "L, e, expect",
    [
        # --- 基礎測試 ---
        ([], 1, False),
        ([1, 2, 3], 1, True),
        ([1, 2, 3], 3, True),
        ([1, 2, 3], 2, True),
        
        # --- 早停 (Early Stopping) 測試 ---
        # 邏輯：當 L[i] > e 時，程式應立即回傳 False
        ([2, 4, 6, 8, 10], 5, False),     # 遇到 6 時發現 6 > 5，應早停
        ([2, 4, 6, 8, 10], 1, False),     # 比最小值還小 (第一個元素就早停)
        
        # --- 掃描到底 ---
        ([2, 4, 6, 8, 10], 12, False),    # 比最大值還大 (需掃完整個 list)
        
        # --- 負數區間 ---
        ([-10, -5, 0, 5, 10], -5, True),  # 負數命中
        ([-10, -5, 0, 5, 10], -3, False), # 負數區間未命中 (0 > -3 早停)
    ]
)
def test_search_sorted_logic(L, e, expect):
    assert lec.search(L, e) == expect


def test_search_behavior_on_unsorted_list():
    """
    特意測試：當輸入未排序列表時，這個函式會發生什麼事？
    這能驗證演算法是否真的依賴 '大於即停止' 的邏輯。
    """
    # 列表未排序：5 在 3 之後
    unsorted_L = [1, 3, 5, 2, 4] 
    
    # search(2) 會失敗，因為遇到 3 時 (3 > 2) 就會停止檢查，
    # 儘管 2 其實在後面。這證明了它依賴排序性質。
    assert lec.search(unsorted_L, 2) is False 
    
    # 相比之下，linear_search 應該要找得到
    assert lec.linear_search(unsorted_L, 2) is True


# ==========================================
# 3. isSubset (子集檢查)
# 檢查 L1 是否包含於 L2
# ==========================================

@pytest.mark.parametrize(
    "L1, L2, expect",
    [
        # --- 基礎邏輯 ---
        ([1, 2], [1, 2, 3, 4], True),       # 真子集
        ([1, 5], [1, 2, 3, 4], False),      # 有元素不在 L2
        ([1, 2, 3], [1, 2, 3], True),       # 集合相等
        
        # --- 空集合邏輯 ---
        ([], [1, 2, 3], True),              # 空集是任何集合的子集
        ([], [], True),                     # 空集是空集的子集
        ([1], [], False),                   # 非空不能包含於空
        
        # --- 重複元素與順序 ---
        ([2, 1], [1, 2, 3], True),          # L1順序不影響結果
        ([1, 1, 1], [1, 2], True),          # L1重複元素不影響 (視為 Set 邏輯)
        
        # --- 字串列表 ---
        (["a", "c"], ["a", "b", "c", "d"], True),
        (["a", "z"], ["a", "b", "c"], False),
    ]
)
def test_isSubset_variations(L1, L2, expect):
    assert lec.isSubset(L1, L2) is expect


# ==========================================
# 4. Intersect (交集)
# 回傳兩列表共同元素，不重複，順序依據 L1
# ==========================================

def test_intersect_order_and_uniqueness():
    """
    測試重點：
    1. 去重 (Uniqueness)
    2. 順序性 (Order preservation by L1)
    """
    # L1: 順序是 5 -> 2 -> 3 -> 5
    # L2: 包含 2, 5, 9
    # 交集元素應為: 5, 2
    L1 = [5, 2, 3, 5, 2]
    L2 = [2, 5, 9]
    
    result = lec.intersect(L1, L2)
    
    # 驗證內容正確
    assert 5 in result
    assert 2 in result
    assert 3 not in result
    assert 9 not in result
    
    # 驗證去重 (長度應為 2)
    assert len(result) == 2
    
    # 驗證順序 (必須跟隨 L1 的出現順序：先 5 再 2)
    assert result == [5, 2]

def test_intersect_empty_cases():
    assert lec.intersect([], [1, 2, 3]) == []
    assert lec.intersect([1, 2], []) == []
    assert lec.intersect([], []) == []

def test_intersect_no_common_elements():
    assert lec.intersect([1, 2], [3, 4]) == []

def test_intersect_strings():
    L1 = ["red", "blue", "green", "red"]
    L2 = ["green", "red", "yellow"]
    # L1順序: red 先出現，green 後出現
    assert lec.intersect(L1, L2) == ["red", "green"]
