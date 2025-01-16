def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pi = partition(items, low, high)
            # Recursively sort elements before and after partition
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def partition(items, low, high):
        pivot = items[high]  # Choose the rightmost element as pivot
        i = low - 1          # Pointer for greater element
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                # Swap if element is smaller than pivot
                items[i], items[j] = items[j], items[i]
        # Swap the pivot element with the greater element at i+1
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)   # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n -1, 0, -1):
        # Swap current root to end
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Heapify the root
        heapify(arr, n, largest)

def sort_and_display(arr):
    print("Initial array:", arr)
    print()

    # Bubble Sort
    arr_copy = arr[:]
    bubble_sort(arr_copy)
    print("Bubble Sort:")
    print(arr_copy)
    print()
    print("=============================================================")

    # Quick Sort
    arr_copy = arr[:]
    quick_sort(arr_copy)
    print("Quick Sort:")
    print(arr_copy)
    print()
    print("=============================================================")

    # Merge Sort
    arr_copy = arr[:]
    merge_sort(arr_copy)
    print("Merge Sort:")
    print(arr_copy)
    print()
    print("=============================================================")

    # Heap Sort
    arr_copy = arr[:]
    heap_sort(arr_copy)
    print("Heap Sort:")
    print(arr_copy)
    print()
    print("=============================================================")

# Example usage
arr = [4, 1, 2, 2, 1, 3, 2]
sort_and_display(arr)
# commit test 2
