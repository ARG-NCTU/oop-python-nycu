import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Corrected tuple assignment
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


class sortingObject:
    def __init__(self, sort_type):
        self.sort_type = sort_type
        self.arr = self.generate_random_array()

    def generate_random_array(self):
        random.seed(time.time())
        size = random.randint(5, 10)  # Corrected to have two arguments
        return [random.randint(0, 100) for _ in range(size)]
    
    def sort_and_measure(self, arr):
        start_time = time.time()
        self.sort_type(arr)
        end_time = time.time()
        return end_time - start_time

    def print_results(self):
        arr = self.generate_random_array()  # Generate a new random array
        print(f"Sorting using: {self.sort_type.__name__}")
        print("Unsorted array:", arr)
        time_taken = self.sort_and_measure(arr)
        print("Sorted array:", arr)
        print(f"Time taken: {time_taken:.6f} seconds")

# Example usage
if __name__ == "__main__":
    for sort_func in [merge_sort, insertion_sort, bubble_sort]:
        tester = sortingObject(sort_func)
        tester.print_results()
        print("=============================================================")
