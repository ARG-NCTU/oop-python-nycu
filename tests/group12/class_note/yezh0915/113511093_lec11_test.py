import pytest
from src.mit_ocw_exercises import lec11_complexity_part2 as lec

def test_bisect_search1_found():
    L = list(range(100))
    assert lec.bisect_search1(L, 76) is True
    assert lec.bisect_search1(L, 0) is True
    assert lec.bisect_search1(L, 99) is True

def test_bisect_search1_not_found():
    L = list(range(100))
    assert lec.bisect_search1(L, -1) is False
    assert lec.bisect_search1(L, 100) is False

def test_bisect_search2_found():
    L = list(range(100))
    assert lec.bisect_search2(L, 76) is True
    assert lec.bisect_search2(L, 0) is True
    assert lec.bisect_search2(L, 99) is True

def test_bisect_search2_not_found():
    L = list(range(100))
    assert lec.bisect_search2(L, -1) is False
    assert lec.bisect_search2(L, 100) is False

def test_genSubsets_empty():
    assert lec.genSubsets([]) == [[]]

def test_genSubsets_single():
    assert lec.genSubsets([1]) == [[], [1]]

def test_genSubsets_multiple():
    result = lec.genSubsets([1, 2])
    expected = [[], [1], [2], [1, 2]]
    # order may differ
    for subset in expected:
        assert subset in result
    assert len(result) == 4

    result = lec.genSubsets([1, 2, 3])
    assert len(result) == 8  # 2^3 subsets

def test_genSubsets_contains_all_subsets():
    s = [1, 2, 3]
    subsets = lec.genSubsets(s)
    assert [] in subsets
    assert [1] in subsets
    assert [2] in subsets
    assert [3] in subsets
    assert [1,2] in subsets
    assert [1,3] in subsets
    assert [2,3] in subsets
    assert [1,2,3] in subsets
