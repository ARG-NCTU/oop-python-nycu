import copy
import pytest

from lec12 import (  
    bubble_sort, bubble_sort_np,
    selection_sort, selection_sort_np,
    merge_sort, merge_sort_np,
    merge, merge_np
)

# Test cases
unsorted_lists = [
    [],
    [1],
    [2, 1],
    [3, 2, 1],
    [5, 3, 8, 1, 2],
    [1, 2, 2, 1],
    [9, -3, 5, 0, -1, 3],
    list(range(10, 0, -1))
]

@pytest.mark.parametrize("sort_func", [
    bubble_sort, bubble_sort_np,
    selection_sort, selection_sort_np
])
@pytest.mark.parametrize("original", unsorted_lists)
def test_in_place_sorts(sort_func, original):
    input_list = copy.deepcopy(original)
    sort_func(input_list)
    assert input_list == sorted(original), f"{sort_func.__name__} failed for input {original}"

@pytest.mark.parametrize("sort_func", [
    merge_sort, merge_sort_np
])
@pytest.mark.parametrize("original", unsorted_lists)
def test_merge_sorts(sort_func, original):
    result = sort_func(original)
    assert result == sorted(original), f"{sort_func.__name__} failed for input {original}"

@pytest.mark.parametrize("left, right", [
    ([], []),
    ([1], []),
    ([], [2]),
    ([1], [2]),
    ([3, 5], [2, 4]),
    ([1, 3, 5], [2, 4, 6]),
    ([0, 0, 1], [0, 2])
])
def test_merge_functions(left, right):
    expected = sorted(left + right)
    assert merge(left, right) == expected
    assert merge_np(left, right) == expected
