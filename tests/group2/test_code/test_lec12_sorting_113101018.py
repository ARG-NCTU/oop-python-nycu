import pytest
import lec12_sorting as lec12


# ---------- bubble_sort_np ----------
def test_bubble_sort():
    bubble_case_desc = [7, 4, 1, 0]
    assert lec12.bubble_sort_np(bubble_case_desc) == [0, 1, 4, 7]

    bubble_case_single = [42]
    assert lec12.bubble_sort_np(bubble_case_single) == [42]
    unsorted_numbers = [5, 2, 9, 1, 5, 6]
    sorted_expected  = [1, 2, 5, 5, 6, 9]
    assert lec12.bubble_sort_np(unsorted_numbers) == sorted_expected

    single_element_list = [-7]
    assert lec12.bubble_sort_np(single_element_list) == [-7]

# ---------- merge_sort_np ----------
def test_merge_sort():
    merge_case_desc = [9, 3, 2, 0]
    assert lec12.merge_sort_np(merge_case_desc) == [0, 2, 3, 9]

    merge_case_empty = []
    assert lec12.merge_sort_np(merge_case_empty) == []

