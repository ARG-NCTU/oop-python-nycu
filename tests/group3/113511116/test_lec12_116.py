import add_path
import mit_ocw_exercises.lec12_sorting as lec12
import pytest

def test_bubble_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = lec12.bubble_sort(arr)
    assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]

def test_selection_sort():
    arr = [64, 25, 12, 22, 11]
    sorted_arr = lec12.selection_sort(arr)
    assert sorted_arr == [11, 12, 22, 25, 64]

def test_merge_sort():
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = lec12.merge_sort(arr)
    assert sorted_arr == [3, 9, 10, 27, 38, 43, 82]


def test_merge():
    left = [1, 3, 5]
    right = [2, 4, 6]
    merged = lec12.merge(left, right)
    assert merged == [1, 2, 3, 4, 5, 6]

def test_bubble_sort_np():
    arr = [5, 1, 4, 2, 8]
    sorted_arr = lec12.bubble_sort_np(arr)
    assert sorted_arr == [1, 2, 4, 5, 8]


def test_selection_sort_np():
    arr = [64, 25, 12, 22, 11]
    sorted_arr = lec12.selection_sort_np(arr)
    assert sorted_arr == [11, 12, 22, 25, 64]

def test_merge_sort_np():
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = lec12.merge_sort_np(arr)
    assert sorted_arr == [3, 9, 10, 27, 38, 43, 82]
    arr1 = [5,45,23,87,1,4,99,34,12]
    sorted_arr1 = lec12.merge_sort_np(arr1)
    assert sorted_arr1 == [1,4,5,12,23,34,45,87,99]
5
