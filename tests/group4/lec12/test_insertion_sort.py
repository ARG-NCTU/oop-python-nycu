# test_bubble_sort.py

import pytest
from sorting_111511236 import bubble_sort as g4_bubble_sort

def test_bubble_sort():
    assert g4_bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert g4_bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert g4_bubble_sort([1]) == [1]  # Single element
    assert g4_bubble_sort([]) == []  # Empty list
    assert g4_bubble_sort([1, 2, 3]) == [1, 2, 3]  # Already sorted
    assert g4_bubble_sort([2, 3, 1]) == [1, 2, 3]  # Unsorted
    assert g4_bubble_sort([1, 0, -1]) == [-1, 0, 1]  # Negative numbers

if __name__ == "__main__":
    pytest.main()
