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

print(bubble_sort([4, 3, 2, 1]))

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]   ## swap
        suffixSt += 1
print(selection_sort([4, 3, 2, 1]))

def merge(left, right): ## merge two sorted lists
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    ##left part when one list had been used up
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result
print(merge([1, 3, 5, 10], [2, 4]))


def merge_sort(L): 
    if len(L) < 2:
        return L[:] ##return a copy of L
    else:
        print('merge sort: ' + str(L))
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
print(merge_sort([1, 3, 5, 10, 2, 4, 7, 23, 41]))
   
