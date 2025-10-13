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
