import copy
import pytest
import random

from lec12 import (  
    bubble_sort, bubble_sort_np,
    selection_sort, selection_sort_np,
    merge_sort, merge_sort_np,
    merge, merge_np
)
# Generate random test cases
random_lists = [
    random.sample(range(-100, 100), k) for k in range(0, 20)
]

@pytest.mark.parametrize("sort_func", [
    bubble_sort, bubble_sort_np,
    selection_sort, selection_sort_np
])
@pytest.mark.parametrize("original", random_lists)
def test_random_in_place_sorts(sort_func, original):
    input_list = copy.deepcopy(original)
    sort_func(input_list)
    assert input_list == sorted(original)

@pytest.mark.parametrize("sort_func", [
    merge_sort, merge_sort_np
])
@pytest.mark.parametrize("original", random_lists)
def test_random_merge_sorts(sort_func, original):
    result = sort_func(original)
    assert result == sorted(original)

@pytest.mark.parametrize("sort_func", [
    bubble_sort, bubble_sort_np,
    selection_sort, selection_sort_np
])
def test_idempotency_in_place_sorts(sort_func):
    data = [5, 3, 8, 1, 2]
    sort_func(data)
    sorted_once = data[:]
    sort_func(data)
    assert data == sorted_once

@pytest.mark.parametrize("sort_func", [
    merge_sort, merge_sort_np
])
def test_idempotency_merge_sorts(sort_func):
    data = [5, 3, 8, 1, 2]
    first = sort_func(data)
    second = sort_func(first)
    assert first == second

@pytest.mark.parametrize("a, b, c", [
    ([1], [3], [2]),
    ([1, 3], [4, 5], [2]),
    ([0], [], [1])
])
def test_merge_associativity(a, b, c):
    ab = merge(a, b)
    abc1 = merge(ab, c)
    bc = merge(b, c)
    abc2 = merge(a, bc)
    assert abc1 == abc2

"""@pytest.mark.parametrize("invalid_input", [
    None, 42, "string", {1, 2, 3}, {1: 'a'}, object()
])

def test_type_errors(invalid_input):
    with pytest.raises(TypeError):
        merge_sort(invalid_input)
    with pytest.raises(TypeError):
        merge_sort_np(invalid_input)"""
