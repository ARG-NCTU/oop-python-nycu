import pytest
import lec12

def test_bubble_sort():
    lst = [4, 2, 1, 5]
    expected = sorted(lst)
    lec12.bubble_sort(lst)
    assert lst == expected

def test_selection_sort():
    lst = [10, 3, 8, 1]
    expected = sorted(lst)
    lec12.selection_sort(lst)
    assert lst == expected

def test_merge_sort():
    lst = [7, 4, 9, 1]
    sorted_lst = lec12.merge_sort(lst)
    expected = sorted(lst)
    assert sorted_lst == expected
    # 原始 list 不應被修改
    assert lst == [7, 4, 9, 1]

