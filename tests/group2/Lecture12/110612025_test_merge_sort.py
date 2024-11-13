# pytest for merge_sort
import pytest
from lec12_sorting import merge_sort
import numpy as np
import time

def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    assert merge_sort([0]) == [0]

def test_merge_sort_sorted():
    assert merge_sort([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]

def test_merge_sort_unsorted():
    assert merge_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]

def test_merge_sort_duplicates():
    assert merge_sort([4, 2, 4, 2, 1, 2]) == [1, 2, 2, 2, 4, 4]
def test_merge_sort_negatives():
    assert merge_sort([4, -2, -1, -8, 7, 6]) == [-8, -2, -1, 4, 6, 7]
def test_merge_sort_all_same():
    assert merge_sort([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]

# Run tests
if __name__ == "__main__":
    pytest.main()