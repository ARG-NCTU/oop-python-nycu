# mit_ocw_exercises/lec12_sorting.py

def bubble_sort(L):
    """Returns a sorted copy of L using bubble sort."""
    L = L[:]  # copy to avoid mutating input
    n = len(L)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swapped = True
        if not swapped:
            break  # list is already sorted
    return L


def selection_sort(L):
    """Returns a sorted copy of L using selection sort."""
    L = L[:]
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if L[j] < L[min_index]:
                min_index = j
        if min_index != i:
            L[i], L[min_index] = L[min_index], L[i]
    return L


def merge_sort(L):
    """Returns a sorted copy of L using merge sort (optimized with indices)."""
    def merge_inplace(L, start, end):
        if end - start <= 1:
            return L[start:end]
        mid = (start + end) // 2
        left = merge_inplace(L, start, mid)
        right = merge_inplace(L, mid, end)
        return merge(left, right)

    return merge_inplace(L, 0, len(L))


def merge(left, right):
    """Helper function for merge_sort."""
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
