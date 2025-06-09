from lec12_final import *

def test_bubble_sort():
    assert bubble_sort_np([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort_np([]) == []
    assert bubble_sort_np([1]) == [1]

def test_selection_sort():
    assert selection_sort_np([5, 1, 4, 2]) == [1, 2, 4, 5]
    assert selection_sort_np([3, 3, 3]) == [3, 3, 3]

def test_merge_sort():
    assert merge_sort_np([5, 2, 4, 1]) == [1, 2, 4, 5]
    assert merge_sort_np([1, 2, 3]) == [1, 2, 3]
    assert merge_sort_np([]) == []

def test_merge():
    assert merge_np([1, 3], [2, 4]) == [1, 2, 3, 4]
    assert merge_np([], [1, 2]) == [1, 2]
    assert merge_np([3, 5], []) == [3, 5]
