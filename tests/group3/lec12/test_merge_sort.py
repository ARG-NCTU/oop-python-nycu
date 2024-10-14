# pytest for merge_sort
import pytest
from lec12_sorting import merge_sort
import numpy as np
import time

def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    assert merge_sort([1]) == [1]

def test_merge_sort_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted():
    assert merge_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_merge_sort_duplicates():
    assert merge_sort([4, 2, 4, 3, 1, 2]) == [1, 2, 2, 3, 4, 4]
def test_merge_sort_negatives():
    assert merge_sort([4, -2, 1, -8, 7, 6]) == [-8, -2, 1, 4, 6, 7]
def test_merge_sort_all_same():
    assert merge_sort([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]

# Test random input and measure execution time
def test_random_input():
    random_input = np.random.randint(0, 1000, size=1000).tolist()
    start_time = time.time()
    sorted_output = merge_sort(random_input)
    end_time = time.time()
    assert sorted_output == sorted(random_input)
    print(f"Execution time for random input: {end_time - start_time} seconds")

# Run tests
if __name__ == "__main__":
    pytest.main()
