# -*- coding: utf-8 -*-
"""
lec12_sorting.py

教學用的排序演算法範例檔，包含多種排序的直觀實作：
- `bubble_sort` / `bubble_sort_np`: 泡沫排序 (有/無印出中間步驟)
- `selection_sort` / `selection_sort_np`: 選擇排序 (有/無印出中間步驟)
- `merge` / `merge_np` 與 `merge_sort` / `merge_sort_np`: 合併排序（遞迴分治）

說明：以教學為主的實作，包含印出中間步驟的版本（用於展示排序過程），
以及不印出的版本（後綴 `_np`，np = no print），便利測試與效能比較。
"""


def bubble_sort(L):
    """泡沫排序（Bubble Sort）- 帶有中間步驟輸出

    行為：重複掃描列表，若相鄰元素順序錯誤則交換；每一輪保證至少將一個元素放到正確位置。
    本版本在每次外層迴圈開始時會印出目前列表，用於教學示範。
    時間複雜度：O(n^2)
    """
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

def selection_sort(L):
    """選擇排序（Selection Sort）- 帶有中間步驟輸出

    行為：維護已排序的前綴區間（suffixSt 表示已排序區間的起始位置），
    每次從未排序部分選出最小值並放到前綴區的末端。
    本版本會在每次外層迴圈印出目前列表，用於示範排序進度。
    時間複雜度：O(n^2)
    """
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
 

def merge(left, right):
    """合併兩個已排序的子序列，回傳合併後的已排序結果。

    - left, right: 皆為已排序的列表
    - 採雙指標掃描，逐一取出較小元素加入結果
    - 回傳一個新的已排序列表
    此版本會印出合併前後的狀態以便觀察遞迴過程。
    """
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):
    """合併排序（Merge Sort）- 遞迴分治實作

    - 若列表長度小於 2，回傳其淺複本
    - 否則分成左右兩半遞迴排序，最後以 `merge` 合併
    時間複雜度：O(n log n)
    此實作在每次呼叫時會印出當前處理的子列，方便教學觀察。
    """
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def bubble_sort_np(L):
    """泡沫排序（不印出中間步驟）- 與 `bubble_sort` 相同但不印出。

    這個版本適合於測試或效能比較，避免印出造成的干擾。
    """
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

def selection_sort_np(L):
    """選擇排序（不印出中間步驟）- 與 `selection_sort` 相同但不印出。
    """
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
 

def merge_np(left, right):
    """合併兩個已排序序列（不印出中間步驟）。"""
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort_np(L):
    """合併排序（不印出中間步驟）。

    與 `merge_sort` 相同但呼叫 `merge_np` 做最終合併，避免教學用的印出。
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort_np(L[:middle])
        right = merge_sort_np(L[middle:])
        return merge_np(left, right)
    
