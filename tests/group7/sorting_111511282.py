def bubble_sort(arr):
    n = len(arr)
    ind = list(range(n))
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ind[j], ind[j+1] = ind[j+1], ind[j]
                swapped = True
        print(f"After round {i+1}:")
        print("Array: ", arr)
        print("Index: ", ind, "\n")
        if not swapped:
            break

def quick_sort(arr, low, high, ind):
    if low < high:
        pi = partition(arr, low, high, ind)
        quick_sort(arr, low, pi - 1, ind)
        quick_sort(arr, pi + 1, high, ind)
    return arr

def partition(arr, low, high, ind):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            ind[i], ind[j] = ind[j], ind[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    ind[i + 1], ind[high] = ind[high], ind[i + 1]
    print(f"Partition at index {i+1}:")
    print("Array: ", arr)
    print("Index: ", ind, "\n")
    return i + 1

def insertion_sort(arr):
    n = len(arr)
    ind = list(range(n))
    for i in range(1, n):
        key = arr[i]
        key_index = ind[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            ind[j + 1] = ind[j]
            j -= 1
        arr[j + 1] = key
        ind[j + 1] = key_index
        print(f"After inserting index {i}:")
        print("Array: ", arr)
        print("Index: ", ind, "\n")

def sort_and_display(arr):
    print("Initial array:", arr)
    
    # Bubble Sort
    print("\nBubble Sort:")
    arr_copy = arr[:]
    bubble_sort(arr_copy)
    print("=============================================================\n")

    # Quick Sort
    print("Quick Sort:")
    arr_copy = arr[:]
    quick_sort(arr_copy, 0, len(arr_copy) - 1, list(range(len(arr_copy))))
    print("=============================================================\n")

    # Insertion Sort
    print("Insertion Sort:")
    arr_copy = arr[:]
    insertion_sort(arr_copy)

arr = [4, 1, 2, 2, 1, 3, 2]

sort_and_display(arr)