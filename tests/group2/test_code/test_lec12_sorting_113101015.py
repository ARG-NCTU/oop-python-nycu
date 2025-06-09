import pytest
import lec12_sorting as lec12

def test_bubble_sort():
    assert lec12.bubble_sort([4, 2, 3, 1]) == [1, 2, 3, 4]
    assert lec12.bubble_sort([4, 2, 3, 1, 5, -1]) == [-1, 1, 2, 3, 4, 5]
    assert lec12.bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]  # already sorted
    assert lec12.bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]  # reverse sorted
    assert lec12.bubble_sort([3, 1, 2, 1]) == [1, 1, 2, 3]  # duplicates
    assert lec12.bubble_sort([-2, -5, 0, 3]) == [-5, -2, 0, 3]  # negative numbers
    assert lec12.bubble_sort([]) == []  # empty list
    assert lec12.bubble_sort([1]) == [1]  # single element

def test_merge_sort():
    assert lec12.merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert lec12.merge_sort([4, 2, 3, 1, 5, -1]) == [-1, 1, 2, 3, 4, 5]
    assert lec12.merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]  # already sorted
    assert lec12.merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]  # reverse sorted
    assert lec12.merge_sort([3, 1, 2, 1]) == [1, 1, 2, 3]  # duplicates
    assert lec12.merge_sort([-2, -5, 0, 3]) == [-5, -2, 0, 3]  # negative numbers
    assert lec12.merge_sort([]) == []  # empty list
    assert lec12.merge_sort([1]) == [1]  # single element

