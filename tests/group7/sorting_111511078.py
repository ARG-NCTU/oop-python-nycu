import time
import random

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)
        arr[:] = sorted(L + R)  # Inline merging

def sorting(sort_func):
    arr = [random.randint(0, 100) for _ in range(random.randint(5, 10))]
    print(f"Sorting with: {sort_func.__name__}")
    print("Before:", arr)
    start = time.time()
    sort_func(arr)
    print("After:", arr)
    print(f"Time taken: {time.time() - start:.6f} seconds\n")

if __name__ == "__main__":
    for sort_func in [merge_sort, insertion_sort, bubble_sort]:
        sorting(sort_func)

