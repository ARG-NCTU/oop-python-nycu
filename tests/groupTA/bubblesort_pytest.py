import pytest
from bubble_sort import bubble_sort

def test_empty_list():
    assert bubble_sort([]) == []

def test_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicates():
    assert bubble_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

def test_negative_numbers():
    assert bubble_sort([-2, -1, -3, 0]) == [-3, -2, -1, 0]
