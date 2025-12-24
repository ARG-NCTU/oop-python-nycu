import unittest
import random

# NOTE: Commented out local dependency to ensure script runs standalone.
# from add_path import add_path
# add_path()
# from lec12_sorting import bubble_sort_np, selection_sort_np, merge_sort_np

# ==============================================================================
# 1. Sorting Algorithm Implementations 🔢
# ==============================================================================

def bubble_sort_np(L: list) -> list:
    """
    Bubble Sort (氣泡排序)
    Complexity: O(N^2)
    Strategy: Repeatedly swap adjacent elements if they are in wrong order.
    """
    L = L[:]  # Create a copy to avoid modifying original list in-place if needed
    n = len(L)
    for i in range(n):
        # Optimization: track if any swap happened
        swapped = False
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swapped = True
        # If no elements were swapped, list is already sorted
        if not swapped:
            break
    return L

def selection_sort_np(L: list) -> list:
    """
    Selection Sort (選擇排序)
    Complexity: O(N^2)
    Strategy: Find the minimum element in the unsorted portion and swap it to the front.
    """
    L = L[:]  # Copy list
    n = len(L)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if L[j] < L[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        L[i], L[min_idx] = L[min_idx], L[i]
    return L

def merge_sort_np(L: list) -> list:
    """
    Merge Sort (合併排序)
    Complexity: O(N log N)
    Strategy: Divide and Conquer. Recursively split list in half, sort, then merge.
    """
    # Base case: A list of 0 or 1 elements is already sorted
    if len(L) <= 1:
        return L

    # Divide
    mid = len(L) // 2
    left = merge_sort_np(L[:mid])
    right = merge_sort_np(L[mid:])

    # Merge
    return merge(left, right)

def merge(left: list, right: list) -> list:
    """Helper function to merge two sorted lists."""
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ==============================================================================
# 2. Unit Tests (unittest) 🧪
# ==============================================================================

class TestSortingAlgorithms(unittest.TestCase):
    """
    測試所有排序演算法。
    Tests: Bubble Sort, Selection Sort, Merge Sort.
    """
    
    def setUp(self):
        """
        設定測試用的列表數據
        """
        # 亂序列表
        self.unsorted_list = [6, 2, 7, 3, 5, 9, 1, 4, 8, 0]
        # 已排序的標準答案
        self.sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 含有重複元素的列表
        self.duplicate_list = [5, 2, 8, 2, 5, 1, 8]
        self.duplicate_sorted = [1, 2, 2, 5, 5, 8, 8]
        # 空列表
        self.empty_list = []
        # 單一元素列表
        self.single_element_list = [42]
        # 負數列表
        self.negative_list = [3, -1, -5, 2]
        self.negative_sorted = [-5, -1, 2, 3]

    def test_bubble_sort_np(self):
        """測試氣泡排序 (Bubble Sort)"""
        # 
        self.assertEqual(bubble_sort_np(list(self.unsorted_list)), self.sorted_list)
        self.assertEqual(bubble_sort_np(list(self.duplicate_list)), self.duplicate_sorted)
        self.assertEqual(bubble_sort_np(list(self.empty_list)), self.empty_list)
        self.assertEqual(bubble_sort_np(list(self.single_element_list)), self.single_element_list)
        self.assertEqual(bubble_sort_np(list(self.negative_list)), self.negative_sorted)

    def test_selection_sort_np(self):
        """測試選擇排序 (Selection Sort)"""
        # 
        self.assertEqual(selection_sort_np(list(self.unsorted_list)), self.sorted_list)
        self.assertEqual(selection_sort_np(list(self.duplicate_list)), self.duplicate_sorted)
        self.assertEqual(selection_sort_np(list(self.empty_list)), self.empty_list)
        self.assertEqual(selection_sort_np(list(self.negative_list)), self.negative_sorted)

    def test_merge_sort_np(self):
        """測試合併排序 (Merge Sort)"""
        # 
        self.assertEqual(merge_sort_np(list(self.unsorted_list)), self.sorted_list)
        self.assertEqual(merge_sort_np(list(self.duplicate_list)), self.duplicate_sorted)
        self.assertEqual(merge_sort_np(list(self.empty_list)), self.empty_list)
        self.assertEqual(merge_sort_np(list(self.single_element_list)), self.single_element_list)

# ==============================================================================
# Main Execution
# ==============================================================================
if __name__ == '__main__':
    print("Running Sorting Tests...")
    # argv parameter allows this to run in Jupyter notebooks and standard terminals
    unittest.main(argv=['first-arg-is-ignored'], exit=False)