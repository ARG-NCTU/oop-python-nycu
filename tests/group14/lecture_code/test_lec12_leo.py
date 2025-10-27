# -*- coding: utf-8 -*-
"""
Sorting demos (verbose and non-verbose versions)
"""

from typing import List

def bubble_sort(L: List[int]) -> List[int]:
    """氣泡排序（含過程輸出），回傳同一個 list 物件。"""
    swap = False
    while not swap:
        print('bubble sort:', L)
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j-1], L[j] = L[j], L[j-1]
    return L

def selection_sort(L: List[int]) -> List[int]:
    """選擇排序（含過程輸出），回傳同一個 list 物件。"""
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort:', L)
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L

def merge(left: List[int], right: List[int]) -> List[int]:
    """合併（含過程輸出）。"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    while i < len(left):
        result.append(left[i]); i += 1
    while j < len(right):
        result.append(right[j]); j += 1
    print('merge:', left, '&', right, '->', result)
    return result

def merge_sort(L: List[int]) -> List[int]:
    """合併排序（含過程輸出），回傳新 list。"""
    print('merge sort:', L)
    if len(L) < 2:
        return L[:]
    middle = len(L) // 2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)

# ---------- Non-verbose（不輸出過程）版本 ----------

def bubble_sort_np(L: List[int]) -> List[int]:
    """氣泡排序（不輸出過程），回傳同一個 list 物件。"""
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j-1], L[j] = L[j], L[j-1]
    return L

def selection_sort_np(L: List[int]) -> List[int]:
    """選擇排序（不輸出過程），回傳同一個 list 物件。"""
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L

def merge_np(left: List[int], right: List[int]) -> List[int]:
    """合併（不輸出過程）。"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    while i < len(left):
        result.append(left[i]); i += 1
    while j < len(right):
        result.append(right[j]); j += 1
    return result

def merge_sort_np(L: List[int]) -> List[int]:
    """合併排序（不輸出過程），回傳新 list。"""
    if len(L) < 2:
        return L[:]
    middle = len(L) // 2
    left = merge_sort_np(L[:middle])
    right = merge_sort_np(L[middle:])
    return merge_np(left, right)

# ---------- 簡單測試 ----------
if __name__ == "__main__":
    data = [9, 1, 5, 3, 7, 2, 8, 6, 4]

    # verbose 版本（會印步驟）
    print("== Verbose ==")
    a = data[:]  # 複本
    bubble_sort(a)
    assert a == sorted(data)

    b = data[:]
    selection_sort(b)
    assert b == sorted(data)

    c = merge_sort(data[:])  # 回傳新 list
    assert c == sorted(data)

    # non-verbose 版本（不印步驟）
    print("\n== Non-verbose ==")
    d = data[:]
    bubble_sort_np(d)
    assert d == sorted(data)

    e = data[:]
    selection_sort_np(e)
    assert e == sorted(data)

    f = merge_sort_np(data[:])
    assert f == sorted(data)

    print("\nAll tests passed.")

