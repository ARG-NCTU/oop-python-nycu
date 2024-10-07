# test_bubble_sort.py

import pytest
from lec12_sorting import bubble_sort

def test_bubble_sort():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert bubble_sort([1]) == [1]  # Single element
    assert bubble_sort([]) == []  # Empty list
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]  # Already sorted
    assert bubble_sort([2, 3, 1]) == [1, 2, 3]  # Unsorted
    assert bubble_sort([1, 0, -1]) == [-1, 0, 1]  # Negative numbers

if __name__ == "__main__":
    pytest.main()
