import pytest

def couting_sort(arr):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        count[arr[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(0, n):
        arr[i] = output[i]
    return arr

def test_couting_sort():
    assert couting_sort([1, 4, 1, 2, 7, 5, 2]) == [1, 1, 2, 2, 4, 5, 7]
    assert couting_sort([1, 4, 1, 2, 7, 5, 2, 8, 9, 0]) == [0, 1, 1, 2, 2, 4, 5, 7, 8, 9]
    assert couting_sort([1, 4, 1, 2, 7, 5, 2, 8, 9, 0, 0, 0]) == [0, 0, 0, 1, 1, 2, 2, 4, 5, 7, 8, 9]
    assert couting_sort([1, 4, 1, 2, 7, 5, 2, 8, 9, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 4, 5, 7, 8, 9]
    assert couting_sort([1, 4, 1, 2, 7, 5, 2, 8, 9]) == [1, 1, 2, 2, 4, 5, 7, 8, 9]
