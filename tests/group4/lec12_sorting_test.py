import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec12_sorting import bubble_sort, selection_sort, merge_sort, merge, bubble_sort_np, selection_sort_np, merge_sort_np
import numpy as np

def test_bubble_sort():
    L = [5, 3, 2, 4, 1]
    sorted_L = bubble_sort(L.copy())
    assert sorted_L == [1, 2, 3, 4, 5]
    assert L == [5, 3, 2, 4, 1]  # Ensure original list is not modified

def test_selection_sort():
    L = [64, 25, 12, 22, 11]
    selection_sort(L)
    assert L == [11, 12, 22, 25, 64]

def test_merge_sort():
    L = [38, 27, 43, 3, 9, 82, 10]
    sorted_L = merge_sort(L.copy())
    assert sorted_L == [3, 9, 10, 27, 38, 43, 82]
    assert L == [38, 27, 43, 3, 9, 82, 10]  # Ensure original list is not modified

def test_merge():
    left = [1, 3, 5]
    right = [2, 4, 6]
    merged = merge(left, right)
    assert merged == [1, 2, 3, 4, 5, 6]

def test_bubble_sort_np():
    L = np.array([5, 3, 2, 4, 1])
    sorted_L = bubble_sort_np(L.copy())
    assert np.array_equal(sorted_L, np.array([1, 2, 3, 4, 5]))
    assert np.array_equal(L, np.array([5, 3, 2, 4, 1]))  # Ensure original array is not modified

def test_selection_sort_np():
    L = np.array([64, 25, 12, 22, 11])
    selection_sort_np(L)
    assert np.array_equal(L, np.array([11, 12, 22, 25, 64]))

def test_merge_sort_np():
    L = np.array([38, 27, 43, 3, 9, 82, 10])
    sorted_L = merge_sort_np(L.copy())
    assert np.array_equal(sorted_L, np.array([3, 9, 10, 27, 38, 43, 82]))
    assert np.array_equal(L, np.array([38, 27, 43, 3, 9, 82, 10]))  # Ensure original array is not modified

def test_merge_np():
    left = np.array([1, 3, 5])
    right = np.array([2, 4, 6])
    merged = merge(left, right)
    assert np.array_equal(merged, np.array([1, 2, 3, 4, 5, 6]))

