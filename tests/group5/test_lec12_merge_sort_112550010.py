def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
 
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
    return arr

def test_merge_0():
    assert mergeSort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]

def test_merge_1():
    assert mergeSort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

def test_merge_2():
    assert mergeSort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]

def test_merge_3():
    assert mergeSort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

def test_merge_4():
    assert mergeSort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]

def test_merge_5():
    assert mergeSort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]


