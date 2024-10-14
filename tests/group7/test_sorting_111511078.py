import pytest
from sorting_111511078 import bubble_sort, insertion_sort, merge_sort

# Test data
test_cases = [
    ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
    ([3, 0, -2, 10, 4], [-2, 0, 3, 4, 10]),
    ([], []),  # Empty array
    ([1], [1]),  # Single element
    ([2, 2, 2], [2, 2, 2]),  # Identical elements
]

@pytest.mark.parametrize("input_data, expected", test_cases)
def test_bubble_sort(input_data, expected):
    bubble_sort(input_data)
    assert input_data == expected

@pytest.mark.parametrize("input_data, expected", test_cases)
def test_insertion_sort(input_data, expected):
    insertion_sort(input_data)
    assert input_data == expected

@pytest.mark.parametrize("input_data, expected", test_cases)
def test_merge_sort(input_data, expected):
    merge_sort(input_data)
    assert input_data == expected
