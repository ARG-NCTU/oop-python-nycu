import tests.group15.lecture_test_code.add_path
import mit_ocw_exercises.lec10_complexity_part1 as l10

import pytest

@pytest.mark.parametrize(
    "L,e,expect",
    [
        ([], 0, False),
        ([5], 5, True),
        ([5], -1, False),
        ([1, 2, 3, 4], 1, True),
        ([1, 2, 3, 4], 4, True),
        ([1, 2, 3, 4], 3, True),
        ([1, 2, 3, 4], 9, False),
        ([1, 1, 2, 2], 1, True),
    ],  
)
def test_linear_search_various(L, e, expect):
    assert l10.linear_search(L, e) is expect


@pytest.mark.parametrize(
    "L,e,expect",
    [
        ([], 1, False),
        ([1], 1, True),
        ([1], 0, False),
        ([1, 3, 4, 5, 9, 18, 27], 1, True),
        ([1, 3, 4, 5, 9, 18, 27], 27, True),
        ([1, 3, 4, 5, 9, 18, 27], 6, False),
        ([-5, -1, 0, 2, 7], -5, True),
        ([-5, -1, 0, 2, 7], -2, False),
        ([-2, -1, -1, 0, 3], -1, True),
        ([2, 4, 6, 8], 1, False),
        ([2, 4, 6, 8], 10, False),
    ],
)
def test_search_sorted_assumption(L, e, expect):
    assert l10.search(L, e) is expect


@pytest.mark.parametrize(
    "L1,L2,expect",
    [
        ([], [], True),
        ([], [1, 2, 3], True),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 3], [1, 2, 3, 4, 5], True),
        ([1, 6], [1, 2, 3, 4, 5], False),
        ([1, 1], [1], True),
        ([1], [], False),
        ([-1, 0], [-2, -1, 0, 1], True),
    ],
)
def test_isSubset_more_cases(L1, L2, expect):
    assert l10.isSubset(L1, L2) is expect


@pytest.mark.parametrize(
    "L1,L2,expect_set",
    [
        ([], [], set()),
        ([1, 2, 3], [], set()),
        ([1, 2, 3], [4, 5], set()),
        ([1, 2, 3], [3, 2, 1], {1, 2, 3}),
        ([1, 2, 3, 4, 5], [2, 4, 6], {2, 4}),
        ([1, 1, 2], [1, 1, 3], {1}),
        ([-2, -1, 0, 1], [-1, 1, 2], {-1, 1}),
    ],
)
def test_intersect_uniqueness_and_values(L1, L2, expect_set):
    got = set(l10.intersect(L1, L2))
    assert got == expect_set
    assert len(got) == len(l10.intersect(L1, L2))


def test_intersect_order_irrelevant():
    L1 = [3, 2, 2, 1]
    L2 = [2, 3, 3, 0]
    out = l10.intersect(L1, L2)
    assert set(out) == {2, 3}
    assert len(out) == 2
