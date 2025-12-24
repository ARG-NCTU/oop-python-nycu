import unittest
import random
import time
import sys
import matplotlib.pyplot as plt

# Increase recursion depth just in case for very large N (Merge Sort)
sys.setrecursionlimit(2000)

# ==============================================================================
# 1. Sorting Algorithms 🔢
# ==============================================================================

def bubble_sort_np(L: list) -> list:
    """
    Complexity: O(N^2) - Very slow for large N.
    """
    L = L[:]  # Copy
    n = len(L)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swapped = True
        if not swapped:
            break
    return L

def selection_sort_np(L: list) -> list:
    """
    Complexity: O(N^2) - Slow, but minimizes swaps compared to Bubble.
    """
    L = L[:]
    n = len(L)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if L[j] < L[min_idx]:
                min_idx = j
        L[i], L[min_idx] = L[min_idx], L[i]
    return L

def merge_sort_np(L: list) -> list:
    """
    Complexity: O(N log N) - Fast, stable, consistent.
    """
    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = merge_sort_np(L[:mid])
    right = merge_sort_np(L[mid:])

    return merge(left, right)

def merge(left: list, right: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ==============================================================================
# 2. Performance Benchmarking 🏎️
# ==============================================================================

def compare_performance():
    print("\n" + "="*50)
    print(f"{'🚀 ALGORITHM RACE':^50}")
    print("="*50)
    
    sizes = [500, 1000, 2000]
    
    print(f"{'Size (N)':<10} | {'Bubble (s)':<12} | {'Selection (s)':<12} | {'Merge (s)':<12}")
    print("-" * 56)

    for n in sizes:
        # Generate random list once per size to ensure fairness
        data = [random.randint(0, 10000) for _ in range(n)]
        
        # Time Bubble Sort
        start = time.perf_counter()
        bubble_sort_np(data)
        t_bubble = time.perf_counter() - start
        
        # Time Selection Sort
        start = time.perf_counter()
        selection_sort_np(data)
        t_select = time.perf_counter() - start
        
        # Time Merge Sort
        start = time.perf_counter()
        merge_sort_np(data)
        t_merge = time.perf_counter() - start
        
        print(f"{n:<10} | {t_bubble:<12.5f} | {t_select:<12.5f} | {t_merge:<12.5f}")

    print("-" * 56)
    print("Note: Notice how Bubble/Selection time quadruples (approx) when N doubles,")
    print("while Merge sort grows much slower.")

# ==============================================================================
# 3. Unit Tests 🧪
# ==============================================================================

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.unsorted = [6, 2, 7, 3, 5, 9, 1, 4, 8, 0]
        self.sorted_ref = sorted(self.unsorted)
        
    def test_all_sorts(self):
        # Testing all logic ensures functionality before benchmarking
        self.assertEqual(bubble_sort_np(self.unsorted), self.sorted_ref)
        self.assertEqual(selection_sort_np(self.unsorted), self.sorted_ref)
        self.assertEqual(merge_sort_np(self.unsorted), self.sorted_ref)

# ==============================================================================
# Main Execution
# ==============================================================================
if __name__ == '__main__':
    # 1. Run Unit Tests first to ensure correctness
    print("running tests...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortingAlgorithms)
    unittest.TextTestRunner(verbosity=1).run(suite)
    
    # 2. Run Performance Benchmark
    
    compare_performance()