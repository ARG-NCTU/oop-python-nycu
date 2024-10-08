def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def test_bubbleSort_0():
    assert bubbleSort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubbleSort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert bubbleSort([3, 1, 2, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubbleSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubbleSort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert bubbleSort([1]) == [1]
    assert bubbleSort([]) == []

def test_bubbleSort_1():
    assert bubbleSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubbleSort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert bubbleSort([1]) == [1]
    assert bubbleSort([]) == []

def test_bubbleSort_2():
    assert bubbleSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubbleSort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
    assert bubbleSort([1]) == [1]
    assert bubbleSort([]) == []
