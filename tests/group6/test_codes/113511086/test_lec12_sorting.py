# mit_ocw_exercises/lec12_sorting.py

def bubble_sort(L):
    """
    Returns a sorted copy of L using bubble sort.
    """
    L = L[:]  # copy to avoid mutating input
    n = len(L)

    for i in range(n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


def selection_sort(L):
    """
    Returns a sorted copy of L using selection sort.
    """
    L = L[:]  # copy to avoid mutating input
    n = len(L)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]

    return L


def merge_sort(L):
    """
    Returns a sorted copy of L using merge sort.
    """
    if len(L) <= 1:
        return L[:]

    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Helper function for merge_sort.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
