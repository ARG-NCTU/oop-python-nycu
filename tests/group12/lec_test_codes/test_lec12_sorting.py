import lec_test_codes.add_path
import mit_ocw_exercises.lec12_sorting as l12
import pytest

def test_bubble_sort():
    testList = [5, 3, 6, 2, 10, 1]
    assert l12.bubble_sort(testList) == [1, 2, 3, 5, 6, 10]
    assert l12.bubble_sort([]) == []
    assert l12.bubble_sort([1]) == [1]
    assert l12.bubble_sort([2, 1]) == [1, 2]
    assert l12.bubble_sort([1, 2]) == [1, 2]
    assert l12.bubble_sort([1, 1, 1]) == [1, 1, 1]

def test_selection_sort():
    testList = [5, 3, 6, 2, 10, 1]
    assert l12.selection_sort(testList) == [1, 2, 3, 5, 6, 10]
    assert l12.selection_sort([]) == []
    assert l12.selection_sort([1]) == [1]
    assert l12.selection_sort([2, 1]) == [1, 2]
    assert l12.selection_sort([1, 2]) == [1, 2]
    assert l12.selection_sort([1, 1, 1]) == [1, 1, 1]
    
def test_merge():
    assert l12.merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert l12.merge([], []) == []
    assert l12.merge([1], []) == [1]
    assert l12.merge([], [1]) == [1]
    assert l12.merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert l12.merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert l12.merge([1, 3, 5], [2]) == [1, 2, 3, 5]
    assert l12.merge([2], [1, 3, 5]) == [1, 2, 3, 5]

def test_merge_sort():
    testList = [5, 3, 6, 2, 10, 1]
    assert l12.merge_sort(testList) == [1, 2, 3, 5, 6, 10]
    assert l12.merge_sort([]) == []
    assert l12.merge_sort([1]) == [1]
    assert l12.merge_sort([2, 1]) == [1, 2]
    assert l12.merge_sort([1, 2]) == [1, 2]
    assert l12.merge_sort([1, 1, 1]) == [1, 1, 1]

