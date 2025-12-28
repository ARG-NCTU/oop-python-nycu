# -*- coding: utf-8 -*-

"""
lec10_complexity_part1.py

此檔示範各種在講義中常見的搜尋/集合操作範例，並用以說明時間複雜度：
- `linear_search`：線性掃描查找，時間複雜度 O(n)。
- `search`：假設 L 已排序，遇到大於目標值時可以提前停止，平均/最壞情況視資料排列而定。
- `isSubset`：檢查 L1 是否為 L2 的子集合（不要求排序），採雙重迴圈比對。
- `intersect`：計算兩列表的交集，並去除重複結果。

註：本檔為教學示範，程式簡潔易懂，但非最有效率的實作（例如可使用 set 加速交集/子集合判斷）。
"""


def linear_search(L, e):
    """線性搜尋（Linear search）

    - 輸入: 列表 L 與元素 e
    - 行為: 逐一檢查 L 的每個元素是否等於 e
    - 回傳: 若找到則回傳 True，否則回傳 False
    - 時間複雜度: O(n)
    """
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


testList = [1, 3, 4, 5, 9, 18, 27]


def search(L, e):
    """針對已排序列表的搜尋（可提前終止）

    - 若 L 已排序（遞增），當發現當前元素大於目標 e 時，可以直接回傳 False（未找到），
      因為之後的元素都會更大。
    - 如果找到則回傳 True；掃描完也沒找到則回傳 False。
    - 此作法在某些資料分布下會比完全線性掃描稍快，但最壞情況仍為 O(n)。
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def isSubset(L1, L2):
    """判斷 L1 是否為 L2 的子集合（不需排序）

    - 對於 L1 中的每個元素，嘗試在 L2 中找到對應元素；若有任一元素無法配對，則 L1 不是 L2 的子集合。
    - 實作使用巢狀迴圈，比較直觀但時間複雜度為 O(len(L1) * len(L2))。
    """
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]


def intersect(L1, L2):
    """計算兩個列表的交集並移除重複值

    實作步驟：
    1. 使用巢狀迴圈找出所有出現在兩列表中的元素，暫存到 `tmp`（可能含重複）。
    2. 走訪 `tmp`，將尚未出現在結果 `res` 的元素加入 `res`，藉此去除重複。

    此方法直觀但效率不佳；若改用集合（set）可大幅加速，且程式更簡短。
    """
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res

