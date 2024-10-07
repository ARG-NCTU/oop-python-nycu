import random
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
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

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def test_sort(): 
    n = 20    #n is the number of elements in the array
    arr = [random.randint(0, 500) for i in range(n)]
    print("Original array:", arr)
    print("-----------------------------------------------")
    #bubble_sort
    arr_copy = arr.copy()
    t1 = time.time()
    bubble_sort(arr_copy)
    t2 = time.time()
    print("Bubble sorted array:   ", arr_copy)
    print("Time taken:", t2 - t1)
    print("-----------------------------------------------")
    
    #insertion_sort
    arr_copy = arr.copy()
    t1 = time.time()
    insertion_sort(arr_copy)
    t2 = time.time()
    print("Insertion sorted array:", arr_copy)
    print("Time taken:", t2 - t1)
    print("-----------------------------------------------")
    
    #merge_sort
    arr_copy = arr.copy()
    t1=time.time()
    merge_sort(arr_copy)
    t2=time.time()
    print("Merge sorted array:    ", arr_copy)
    print("Time taken:", t2 - t1)
    print("-----------------------------------------------")
    
test_sort() # 20 elements in the array
