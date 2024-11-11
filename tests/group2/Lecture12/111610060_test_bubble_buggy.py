import pytest

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

assert bubble_sort([3, 2, 1]) == [1, 2, 3]
assert bubble_sort([4, 3, 1, 8, 9, 6]) == [1, 3, 4, 6, 8, 9]
assert bubble_sort([2, 3, 8, 5, 7]) == [2, 3, 5, 8, 7]
assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert bubble_sort([]) == []
assert bubble_sort([1]) == [1]

if __name__ == '__main__':
    pytest.main()