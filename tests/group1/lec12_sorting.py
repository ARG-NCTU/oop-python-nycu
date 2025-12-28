# -*- coding: utf-8 -*-
"""
Lecture 12: Sorting Algorithms

Examples of various sorting algorithms with complexity analysis:

Algorithms covered:
1. Bubble Sort - O(n^2) time, O(1) space (naive)
2. Selection Sort - O(n^2) time, O(1) space (naive)
3. Merge Sort - O(n log n) time, O(n) space (divide & conquer)

Each algorithm is implemented twice:
- WITH print statements (for visualization/debugging)
- WITHOUT print statements (_np suffix = no print)

Time Complexities:
- Bubble & Selection: O(n^2) - quadratic
- Merge Sort: O(n log n) - optimal for comparison-based sorting

@author: ericgrimson
"""
from add_path import add_path
add_path()

def bubble_sort(L):
    """Bubble sort - repeatedly swaps adjacent elements if out of order.
    
    Time complexity: O(n^2) - worst and average case
    Space complexity: O(1) - sorts in-place
    
    Algorithm:
    - Compare adjacent pairs
    - Swap if left > right
    - Repeat until no swaps occur
    - Larger elements "bubble" to the end
    
    Args:
        L: List to sort (modified in-place)
    
    Returns:
        Sorted list (same object)
    """
    swap = False
    while not swap:
        print('bubble sort: ' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

def selection_sort(L):
    """Selection sort - repeatedly finds minimum and moves to front.
    
    Time complexity: O(n^2) - always, even with sorted input
    Space complexity: O(1) - sorts in-place
    
    Algorithm:
    - Find minimum element in unsorted portion
    - Swap with first position of unsorted portion
    - Move boundary forward
    - Repeat until entire list is sorted
    
    Args:
        L: List to sort (modified in-place)
    
    Returns:
        Sorted list (same object)
    """
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L 

def merge(left, right):
    """Merge two sorted lists into a single sorted list.
    
    Time complexity: O(n + m) where n=len(left), m=len(right)
    Space complexity: O(n + m) for result list
    
    Algorithm:
    - Compare first elements of left and right
    - Append smaller to result
    - Advance pointer in the list it came from
    - When one list exhausted, append rest of other list
    
    Args:
        left: First sorted list
        right: Second sorted list
    
    Returns:
        Merged sorted list combining both inputs
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print('merge: ' + str(left) + '&' + str(right) + ' to ' + str(result))
    return result

def merge_sort(L):
    """Merge sort - divide & conquer algorithm using recursion.
    
    Time complexity: O(n log n) - always, optimal for comparison-based sort
    Space complexity: O(n) - requires temporary arrays for merging
    
    Algorithm:
    1. Divide: Split list in half
    2. Conquer: Recursively sort both halves
    3. Combine: Merge sorted halves
    
    Much more efficient than bubble/selection sort for large lists!
    
    Args:
        L: List to sort (creates new sorted list, doesn't modify original)
    
    Returns:
        New sorted list
    """
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def bubble_sort_np(L):
    """Bubble sort without print statements (faster for testing/benchmarking)."""
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

def selection_sort_np(L):
    """Selection sort without print statements (faster for testing/benchmarking)."""
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L 

def merge_np(left, right):
    """Merge two sorted lists without print statements."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort_np(L):
    """Merge sort without print statements (faster for testing/benchmarking)."""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort_np(L[:middle])
        right = merge_sort_np(L[middle:])
        return merge_np(left, right)


# ===== Comparison and Testing Functions =====

def compare_sorting_methods():
    """Compare the three sorting algorithms on the same input."""
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(test_list)
    
    print("\n=== Sorting Algorithm Comparison ===")
    print(f"Original list: {test_list}\n")
    
    # Test bubble sort
    result_bubble = bubble_sort_np(test_list.copy())
    assert result_bubble == expected, "Bubble sort failed"
    print(f"✓ Bubble Sort (O(n²)): {result_bubble}")
    
    # Test selection sort
    result_selection = selection_sort_np(test_list.copy())
    assert result_selection == expected, "Selection sort failed"
    print(f"✓ Selection Sort (O(n²)): {result_selection}")
    
    # Test merge sort
    result_merge = merge_sort_np(test_list.copy())
    assert result_merge == expected, "Merge sort failed"
    print(f"✓ Merge Sort (O(n log n)): {result_merge}")
    
    print("\nAll sorting algorithms produced correct results!")


if __name__ == "__main__":
    # Run comparison
    compare_sorting_methods()
