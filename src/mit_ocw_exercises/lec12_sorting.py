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
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
 

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

def selection_sort_np(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
 

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
    
def test_sorting_algorithms():
    print("\n--- Testing Sorting Algorithms ---")
    
    test_cases = [
        [],
        [1],
        [2, 1],
        [3, 1, 2],
        [5, 3, 8, 6, 2],
        [9, 8, 7, 6, 5],
        [1, 2, 3, 4, 5],
        [4, 5, 5, 4, 3, 3],
    ]
    
    for case in test_cases:
        expected = sorted(case)

        # Bubble sort
        result_bubble = bubble_sort(case[:])
        assert result_bubble == expected, f"bubble_sort failed on input {case}"

        # Selection sort (non-printing returns None so we check after sort)
        sel_case = case[:]
        selection_sort(sel_case)
        assert sel_case == expected, f"selection_sort failed on input {case}"

        # Merge sort
        result_merge = merge_sort(case[:])
        assert result_merge == expected, f"merge_sort failed on input {case}"

        # Bubble sort no print
        result_bubble_np = bubble_sort_np(case[:])
        assert result_bubble_np == expected, f"bubble_sort_np failed on input {case}"

        # Selection sort no print
        sel_np_case = case[:]
        selection_sort_np(sel_np_case)
        assert sel_np_case == expected, f"selection_sort_np failed on input {case}"

        # Merge sort no print
        result_merge_np = merge_sort_np(case[:])
        assert result_merge_np == expected, f"merge_sort_np failed on input {case}"

    print("All sorting tests passed successfully.")

# Run the test
test_sorting_algorithms()
