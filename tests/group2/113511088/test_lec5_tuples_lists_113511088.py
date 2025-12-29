# -*- coding: utf-8 -*-
import pytest

import lec5_tuples_lists_113511088 as lec5

@pytest.mark.parametrize("L, expected", [
    ([1, 2, 3, 4], 10),
    ([0], 0),
    ([], 0),
    ([-1, -2, -3], -6),
    ([10, -5, 2], 7),
    ([1.5, 2.5, 3.0], 7.0),
])
def test_sum_elem_method1(L, expected):
    assert lec5.sum_elem_method1(L) == expected


@pytest.mark.parametrize("L, expected", [
    ([1, 2, 3, 4], 10),
    ([0], 0),
    ([], 0),
    ([-1, -2, -3], -6),
    ([10, -5, 2], 7),
    ([1.5, 2.5, 3.0], 7.0),
])
def test_sum_elem_method2(L, expected):
    assert lec5.sum_elem_method2(L) == expected


@pytest.mark.parametrize("L", [
    [1, 2, 3, 4],
    [],
    [-3, 0, 3],
    [1.2, 3.4],
])
def test_two_methods_same_result(L):
    assert lec5.sum_elem_method1(L) == lec5.sum_elem_method2(L)


def test_original_list_not_modified():
    L = [1, 2, 3, 4]
    before = L.copy()
    lec5.sum_elem_method1(L)
    lec5.sum_elem_method2(L)
    assert L == before


def test_non_numeric_raises_typeerror():
    with pytest.raises(TypeError):
        lec5.sum_elem_method1([1, "2", 3])

    with pytest.raises(TypeError):
        lec5.sum_elem_method2([1, "2", 3])
