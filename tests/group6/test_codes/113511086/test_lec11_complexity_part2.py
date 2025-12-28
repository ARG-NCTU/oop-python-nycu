import pytest
import mit_ocw_exercises.lec11_complexity_part2 as lec11

# ----------------- bisect_search2 tests -----------------
@pytest.mark.parametrize("L, e, expected", [
    ([0,1,2,3,4,5,6,7,8,9], 5, True),
    ([0,1,2,3,4,5,6,7,8,9], 10, False),
    ([0,1,2,3,4,5,6,7,8,9], -1, False),
    ([], 5, False),
])
def test_bisect_search2(L, e, expected):
    assert lec11.bisect_search2(L, e) == expected


@pytest.mark.slow
@pytest.mark.parametrize("n", [10, 10000, 100000])
def test_bisect_search2_large(n):
    L = list(range(n))
    # test middle value
    assert lec11.bisect_search2(L, n // 2) is True
    # test non-existing value
    assert lec11.bisect_search2(L, n + 1) is False

# ----------------- genSubsets tests -----------------
def test_genSubsets_small():
    L = [1, 2, 3]
    expected = [
        [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]
    ]
    assert lec11.genSubsets(L) == expected

def test_genSubsets_empty():
    assert lec11.genSubsets([]) == [[]]

@pytest.mark.slow
def test_genSubsets_medium():
    L = [1,2,3,4]
    result = lec11.genSubsets(L)
    assert len(result) == 2 ** 4
    # optional: check first and last subset
    assert result[0] == []
    assert result[-1] == [1,2,3,4]
