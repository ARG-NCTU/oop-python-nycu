# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:21:39 2016

@author: ericgrimson
"""
def bubble_sort(L):
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        # 每次都從1-len(L)的範圍中兩兩相鄰的element比較一次，只要發現其中有至少1組相鄰的element並非遞增，就將swap = False，代表接下來還要再跑一輪for迴圈。
        # 直到一個for迴圈1-len(L)的範圍中沒有任何一組相鄰的element非遞增，就代表排序完畢。
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

def test_bubble_sort():
    testList = [3, 1, 2, 6, 5, 4, 10, 8]
    assert bubble_sort(testList) == [1, 2, 3, 4, 5, 6, 8, 10]


def selection_sort(L):
    # 每次處理[suffixSt:len(L)]的範圍
    # suffixSt會從0逐次遞增到len(L)-1
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        # for迴圈跑遍[suffixSt:len(L)]的範圍，將最小的element放到index = suffixSt的位置上
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt] # 交換
        suffixSt += 1

def test_selection_sort():
    testList = [3, 1, 2, 6, 5, 4, 10, 8]
    selection_sort(testList)
    assert testList == [1, 2, 3, 4, 5, 6, 8, 10]


#將給定的兩個sorted list: left, right合併成一個sorted list
def merge(left, right):
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
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def test_merge_sort():
    testList = [3, 1, 2, 6, 5, 4, 10, 8]
    assert merge_sort(testList) == [1, 2, 3, 4, 5, 6, 8, 10]

# np: No Print
def bubble_sort_np(L):
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

def test_bubble_sort_np():
    testList = [3, 1, 2, 6, 5, 4, 10, 8]
    assert bubble_sort_np(testList) == [1, 2, 3, 4, 5, 6, 8, 10]

def selection_sort_np(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

def test_selection_sort_np():
    testList = [3, 1, 2, 6, 5, 4, 10, 8]
    selection_sort_np(testList)
    assert testList == [1, 2, 3, 4, 5, 6, 8, 10]


def merge_np(left, right):
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
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort_np(L[:middle])
        right = merge_sort_np(L[middle:])
        return merge_np(left, right)

def test_merge_sort_np():
    testList = [3, 1, 2, 6, 5, 4, 10, 8]
    assert merge_sort_np(testList) == [1, 2, 3, 4, 5, 6, 8, 10]