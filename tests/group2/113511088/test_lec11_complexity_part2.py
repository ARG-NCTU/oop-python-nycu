# -*- coding: utf-8 -*-
import pytest

import lec11_complexity_part2 as lec11

@pytest.mark.parametrize("e, expected", [
    (0, True),
    (50, True),
    (99, True),
    (-1, False),
    (100, False),
    (76, True),
    (77, True),
    (78, True),
])
def test_bisect_search1_on_sorted_range(e, expected):
    L = list(range(100))
    assert lec11.bisect_search1(L, e) is expected


@pytest.mark.parametrize("e, expected", [
    (0, True),
    (50, True),
    (99, True),
    (-1, False),
    (100, False),
    (76, True),
    (77, True),
    (78, True),
])
def test_bisect_search2_on_sorted_range(e, expected):
    L = list(range(100))
    assert lec11.bisect_search2(L, e) is expected


def test_bisect_search_empty_list():
    assert lec11.bisect_search1([], 1) is False
    assert lec11.bisect_search2([], 1) is False


def test_genSubsets_size_and_contains():
    L = [1, 2, 3, 4]
    subs = lec11.genSubsets(L)

    # should be 2^n subsets
    assert len(subs) == 2 ** len(L)

    # key subsets should exist
    assert [] in subs
    assert [1] in subs
    assert [2] in subs
    assert [3] in subs
    assert [4] in subs
    assert [1, 2, 3, 4] in subs


def test_genSubsets_does_not_modify_input():
    L = [1, 2, 3]
    before = L.copy()
    _ = lec11.genSubsets(L)
    assert L == before
