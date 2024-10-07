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
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test reverse sorted list
def test_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

# Test unsorted list
def test_unsorted_list():
    assert bubble_sort([4, 2, 1, 8, 7, 6]) == [1, 2, 4, 6, 7, 8]

# Test list with duplicates
def test_list_with_duplicates():
    assert bubble_sort([4, 2, 2, 8, 7, 6]) == [2, 2, 4, 6, 7, 8]

# Test list with negatives
def test_list_with_negatives():
    assert bubble_sort([4, -2, 1, -8, 7, 6]) == [-8, -2, 1, 4, 6, 7]

# Test single element list
def test_single_element_list():
    assert bubble_sort([1]) == [1]

# Test all same elements
def test_all_same_elements():
    assert bubble_sort([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]

# Test random input and measure execution time
def test_random_input():
    random_input = np.random.randint(0, 1000, size=1000).tolist()
    start_time = time.time()
    sorted_output = bubble_sort(random_input)
    end_time = time.time()
    assert sorted_output == sorted(random_input)
    print(f"Execution time for random input: {end_time - start_time} seconds")

# Run tests
if __name__ == "__main__":
    pytest.main()