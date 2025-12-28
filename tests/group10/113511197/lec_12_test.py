
"""
pytest version of sorting algorithms
"""
from typing import List

def bubble_sort(L: List[int]) -> List[int]:
    """Bubble sort with print statements for debugging."""
    swap = False
    while not swap:
        print('bubble sort:', L)
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j-1], L[j] = L[j], L[j-1]  # Swap adjacent elements
    return L

def selection_sort(L: List[int]) -> List[int]:
    """Selection sort with print statements for debugging."""
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort:', L)
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:  # Find minimum in unsorted portion
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L

def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists into one sorted list."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    # Append remaining elements
    while i < len(left):
        result.append(left[i]); i += 1
    while j < len(right):
        result.append(right[j]); j += 1
    print('merge:', left, '&', right, '->', result)
    return result

def merge_sort(L: List[int]) -> List[int]:
    """Merge sort with print statements for debugging. Returns new list."""
    print('merge sort:', L)
    if len(L) < 2:
        return L[:]
    middle = len(L) // 2
    left = merge_sort(L[:middle])  # Recursively sort left half
    right = merge_sort(L[middle:])  # Recursively sort right half
    return merge(left, right)

def bubble_sort_np(L: List[int]) -> List[int]:
    """Bubble sort without print statements (np = no print)."""
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j-1], L[j] = L[j], L[j-1]
    return L

def selection_sort_np(L: List[int]) -> List[int]:
    """Selection sort without print statements (np = no print)."""
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L

def merge_np(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists without print statements (np = no print)."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    while i < len(left):
        result.append(left[i]); i += 1
    while j < len(right):
        result.append(right[j]); j += 1
    return result

def merge_sort_np(L: List[int]) -> List[int]:
    """Merge sort without print statements (np = no print). Returns new list."""
    if len(L) < 2:
        return L[:]
    middle = len(L) // 2
    left = merge_sort_np(L[:middle])
    right = merge_sort_np(L[middle:])
    return merge_np(left, right)

# ---------- pytest tests ----------

import pytest
from copy import deepcopy

@pytest.mark.parametrize("func", [
    bubble_sort, selection_sort, merge_sort,
    bubble_sort_np, selection_sort_np, merge_sort_np
])
@pytest.mark.parametrize("data", [
    [], [1], [2, 1], [3, 2, 1],
    [9, 1, 5, 3, 7, 2, 8, 6, 4],
    [0, -1, 2, -3, 4, -5],
    [1, 3, 2, 2, 3, 1]
])
def test_sort_correctness(func, data):
    """Test that all sorting functions produce correct sorted output."""
    L = deepcopy(data)
    # merge_sort 會回傳新 list
    result = func(L if "merge" not in func.__name__ else data[:])
    assert result == sorted(data)

def test_inplace_behavior():
    """Test that bubble_sort and selection_sort modify the list in-place."""
    L1 = [3, 1, 2]
    L2 = [3, 1, 2]
    id_before1 = id(L1)
    id_before2 = id(L2)
    bubble_sort(L1)
    selection_sort(L2)
    assert id(L1) == id_before1
    assert id(L2) == id_before2
    assert L1 == [1, 2, 3]
    assert L2 == [1, 2, 3]

def test_merge_sort_new_object():
    """Test that merge_sort returns a new list, not the original."""
    L = [3, 1, 2]
    out = merge_sort(L)
    assert out is not L
    assert out == [1, 2, 3]

def test_verbose_output(capsys):
    """Test that verbose (with print) versions produce expected debug output."""
    L = [3, 2, 1]
    bubble_sort(L)
    captured = capsys.readouterr().out
    assert "bubble sort" in captured

    selection_sort([3, 2, 1])
    captured = capsys.readouterr().out
    assert "selection sort" in captured

    merge_sort([3, 2, 1])
    captured = capsys.readouterr().out
    assert "merge sort" in captured
    assert "merge:" in captured
