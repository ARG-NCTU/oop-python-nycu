import pytest
import random
import time
from mit_ocw_exercises.lec12_sorting import bubble_sort, selection_sort, merge_sort

@pytest.mark.parametrize("L, expected", [
    ([1, 3, 5, 7, 2, 6, 25, 18, 13], [1,2,3,5,6,7,13,18,25]),
    ([5, 4, 3, 2, 1], [1,2,3,4,5]),
    ([], [])
])
def test_bubble_sort(L, expected):
    assert bubble_sort(L) == expected

@pytest.mark.parametrize("L, expected", [
    ([1, 3, 5, 7, 2, 6, 25, 18, 13], [1,2,3,5,6,7,13,18,25]),
    ([5, 4, 3, 2, 1], [1,2,3,4,5]),
    ([], [])
])
def test_selection_sort(L, expected):
    assert selection_sort(L) == expected

@pytest.mark.parametrize("L, expected", [
    ([1, 3, 5, 7, 2, 6, 25, 18, 13], [1,2,3,5,6,7,13,18,25]),
    ([5, 4, 3, 2, 1], [1,2,3,4,5]),
    ([], [])
])
def test_merge_sort(L, expected):
    assert merge_sort(L) == expected

@pytest.mark.slow
def test_sort_performance():
    sorting_methods = [("bubble sort", bubble_sort),
                       ("selection sort", selection_sort),
                       ("merge sort", merge_sort)]
    test_list = [random.randint(0, 100) for _ in range(5000)]

    for name, func in sorting_methods:
        start = time.time()
        func(test_list)
        end = time.time()
        print(f"{name} time: {end-start:.4f}s")
