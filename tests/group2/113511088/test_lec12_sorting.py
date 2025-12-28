# -*- coding: utf-8 -*-
import pytest
import lec12_sorting as lec12


@pytest.mark.parametrize("L", [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [5, 1, 1, 3, 2],
    [-1, -3, 0, 2, 2],
])
def test_bubble_sort_np_correct(L):
    arr = L.copy()
    out = lec12.bubble_sort_np(arr)
    assert out == sorted(L)
    # bubble_sort_np is in-place (returns same list object)
    assert out is arr


@pytest.mark.parametrize("L", [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [5, 1, 1, 3, 2],
    [-1, -3, 0, 2, 2],
])
def test_selection_sort_np_correct(L):
    arr = L.copy()
    out = lec12.selection_sort_np(arr)
    assert out == sorted(L)
    assert out is arr


@pytest.mark.parametrize("L", [
    [],
    [1],
    [2, 1],
    [3, 1, 2],
    [5, 1, 1, 3, 2],
    [-1, -3, 0, 2, 2],
])
def test_merge_sort_np_correct_and_not_mutate(L):
    arr = L.copy()
    out = lec12.merge_sort_np(arr)
    assert out == sorted(L)
    # merge_sort_np returns a NEW list (does not modify input)
    assert arr == L
    assert out is not arr


def test_merge_np_handles_duplicates_stably_in_order():
    # <= means when equal, take from left first
    left = [1, 2, 2]
    right = [2, 3]
    assert lec12.merge_np(left, right) == [1, 2, 2, 2, 3]


def test_print_versions_work_and_sort(capsys):
    L1 = [3, 1, 2]
    out1 = lec12.bubble_sort(L1)
    _ = capsys.readouterr()  # swallow prints
    assert out1 == [1, 2, 3]

    L2 = [3, 1, 2]
    out2 = lec12.selection_sort(L2)
    _ = capsys.readouterr()
    assert out2 == [1, 2, 3]

    L3 = [3, 1, 2]
    out3 = lec12.merge_sort(L3)
    _ = capsys.readouterr()
    assert out3 == [1, 2, 3]
    # merge_sort returns new list (L3 should remain same as original)
    assert L3 == [3, 1, 2]


def test_merge_sort_print_version_does_not_mutate_input(capsys):
    L = [5, 4, 3, 2, 1]
    before = L.copy()
    out = lec12.merge_sort(L)
    _ = capsys.readouterr()
    assert out == [1, 2, 3, 4, 5]
    assert L == before
