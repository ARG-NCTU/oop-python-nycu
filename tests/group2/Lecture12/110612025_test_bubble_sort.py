# bubble_sort test 
import pytest
import numpy as np
import time
from lec12_sorting import bubble_sort

# Test empty list
def test_empty_list():
    assert bubble_sort([]) == []

# Test sorted list
def test_sorted_list():
    assert bubble_sort([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

# Test reverse sorted list
def test_reverse_sorted_list():
    assert bubble_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]

# Test unsorted list
def test_unsorted_list():
    assert bubble_sort([4, 3, 1, 5, 7, 8]) == [1, 3, 4, 5, 7, 8]

# Test list with duplicates
def test_list_with_duplicates():
    assert bubble_sort([4, 3, 3, 8, 7, 6]) == [3, 3, 4, 6, 7, 8]

# Test list with negatives
def test_list_with_negatives():
    assert bubble_sort([4, -2, 1, -5, 7, 8]) == [-5, -2, 1, 4, 7, 8]

# Test single element list
def test_single_element_list():
    assert bubble_sort([0]) == [0]

# Test all same elements
def test_all_same_elements():
    assert bubble_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]


# Run tests
if __name__ == "__main__":
    pytest.main()