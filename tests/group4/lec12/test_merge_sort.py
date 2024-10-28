# pytest for merge_sort
import pytest
from sorting_111511236 import merge_sort as g4_merge_sort
import numpy as np
import time

def test_merge_sort_empty():
    assert g4_merge_sort([]) == []

def test_merge_sort_single_element():
    assert g4_merge_sort([1]) == [1]

def test_merge_sort_sorted():
    assert g4_merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted():
    assert g4_merge_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_merge_sort_duplicates():
    assert g4_merge_sort([4, 2, 4, 3, 1, 2]) == [1, 2, 2, 3, 4, 4]
def test_merge_sort_negatives():
    assert g4_merge_sort([4, -2, 1, -8, 7, 6]) == [-8, -2, 1, 4, 6, 7]
def test_merge_sort_all_same():
    assert g4_merge_sort([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]

# Test large input
def test_merge_sort_large_input():
    assert g4_merge_sort(list(range(10000, 0, -1))) == list(range(1, 10001))

# Test list with multiple duplicates
def test_merge_sort_list_with_multiple_duplicates():
    assert g4_merge_sort([4, 2, 2, 8, 7, 6, 4, 8, 7]) == [2, 2, 4, 4, 6, 7, 7, 8, 8]

# Test with large number
def test_merge_sort_large_number():
    assert g4_merge_sort([1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]) == [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

# Test random input and measure execution time
def test_random_input():
    random_input = np.random.randint(0, 1000, size=1000).tolist()
    start_time = time.time()
    sorted_output = g4_merge_sort(random_input)
    end_time = time.time()
    assert sorted_output == sorted(random_input)
    print(f"Execution time for random input: {end_time - start_time} seconds")

# Run tests
if __name__ == "__main__":
    pytest.main()
