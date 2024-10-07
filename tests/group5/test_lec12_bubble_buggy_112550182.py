def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubble_sort([4, 2, 1, 8, 7, 6]))

def test_bubble_sort():
    assert bubble_sort([4, 2, 1, 8, 7, 6]) == [1, 2, 4, 6, 7, 8]
    assert bubble_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]

test_bubble_sort()
