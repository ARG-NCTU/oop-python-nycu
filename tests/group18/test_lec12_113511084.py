import os
import sys
import pytest
import math

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec12_sorting as lec12

test_cases = [
    [],
    [1],
    [3, 2, 1],
    [5, 1, 4, 2, 8],
    [5, 1, 5, 2, 8],
]

### --- bubble_sort --- ###
@pytest.mark.parametrize("L", test_cases)
def test_bubble_sort(L):
    L_copy = L.copy()
    assert lec12.bubble_sort(L_copy.copy()) == sorted(L)

@pytest.mark.parametrize("L", test_cases)
def test_bubble_sort_np(L):
    L_copy = L.copy()
    assert lec12.bubble_sort_np(L_copy.copy()) == sorted(L)

### --- selection_sort (in-place, no return) --- ###
@pytest.mark.parametrize("L", test_cases)
def test_selection_sort(L):
    L_copy = L.copy()
    lec12.selection_sort(L_copy)
    assert L_copy == sorted(L)

@pytest.mark.parametrize("L", test_cases)
def test_selection_sort_np(L):
    L_copy = L.copy()
    lec12.selection_sort_np(L_copy)
    assert L_copy == sorted(L)

### --- merge_sort --- ###
@pytest.mark.parametrize("L", test_cases)
def test_merge_sort(L):
    assert lec12.merge_sort(L) == sorted(L)

@pytest.mark.parametrize("L", test_cases)
def test_merge_sort_np(L):
    assert lec12.merge_sort_np(L) == sorted(L)
