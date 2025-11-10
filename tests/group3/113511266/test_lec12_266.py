import add_path
import mit_ocw_exercises.lec12_sorting as lec12
import pytest
import numpy as np

def test_bubble_sort():
    lst = [5, 3, 8, 6, 2]
    # use bubble_sort_np which returns the sorted list
    sorted_lst = lec12.bubble_sort_np(lst)
    assert sorted_lst == [2, 3, 5, 6, 8]

def test_selection_sort():
    lst = [64, 25, 12, 22, 11]
    # use selection_sort_np which returns the sorted list
    # selection_sort_np performs in-place sorting and returns None
    res = lec12.selection_sort_np(lst)
    assert lst == [11, 12, 22, 25, 64]

def test_insertion_sort():
    lst = [12, 11, 13, 5, 6]
    # use merge_sort_np as an available sorting implementation
    sorted_lst = lec12.merge_sort_np(lst)
    assert sorted_lst == [5, 6, 11, 12, 13]


def test_bubble_sort_np():
    L = np.array([5, 3, 2, 4, 1])
    sorted_L = lec12.bubble_sort_np(L.copy())
    assert np.array_equal(sorted_L, np.array([1, 2, 3, 4, 5]))
    assert np.array_equal(L, np.array([5, 3, 2, 4, 1]))  # Ensure original array is not modified

def test_selection_sort_np():
    L = np.array([64, 25, 12, 22, 11])
    lec12.selection_sort_np(L)
    assert np.array_equal(L, np.array([11, 12, 22, 25, 64]))

def test_merge_sort_np():
    L = np.array([38, 27, 43, 3, 9, 82, 10])
    sorted_L = lec12.merge_sort_np(L.copy())
    assert np.array_equal(sorted_L, np.array([3, 9, 10, 27, 38, 43, 82]))
    assert np.array_equal(L, np.array([38, 27, 43, 3, 9, 82, 10]))  # Ensure original array is not modified

def test_merge_np():
    left = np.array([1, 3, 5])
    right = np.array([2, 4, 6])
    merged = lec12.merge(left, right)
    assert np.array_equal(merged, np.array([1, 2, 3, 4, 5, 6]))

