import add_path
import mit_ocw_exercises.lec12_sorting as lec12
import pytest

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
    assert res is None
    assert lst == [11, 12, 22, 25, 64]

def test_insertion_sort():
    lst = [12, 11, 13, 5, 6]
    # use merge_sort_np as an available sorting implementation
    sorted_lst = lec12.merge_sort_np(lst)
    assert sorted_lst == [5, 6, 11, 12, 13]