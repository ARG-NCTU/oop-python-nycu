# bubble_sort_test.py

def bubble_sort(arr):
    n = len(arr)  # Get the length of the list
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr  # Return the sorted list

# Test function
if __name__ == "__main__":
    test_arr = [5, 8, 7, 3, 9, 2]
    sorted_arr = bubble_sort(test_arr)
    print(f"Original list: {test_arr}")
    print(f"Sorted list: {sorted_arr}")

