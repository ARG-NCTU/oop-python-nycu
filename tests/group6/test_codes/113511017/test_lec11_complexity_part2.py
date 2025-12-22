import lec_test_codes.add_path
import mit_ocw_exercises.lec11_complexity_part2 as l11
import pytest


#############################
# Test bisect_search1
#############################
def test_bisect_search1_found():
    L = list(range(0, 100))
    assert l11.bisect_search1(L, 0) is True
    assert l11.bisect_search1(L, 50) is True
    assert l11.bisect_search1(L, 99) is True


def test_bisect_search1_not_found():
    L = list(range(0, 100))
    assert l11.bisect_search1(L, -1) is False
    assert l11.bisect_search1(L, 100) is False
    with pytest.raises(IndexError) as e:
        l11.bisect_search1([], 5)
    assert "list index out of range" in str(e.value)

def test_bisect_search2_found():
    L = list(range(0, 100))
    assert l11.bisect_search2(L, 0) is True
    assert l11.bisect_search2(L, 50) is True
    assert l11.bisect_search2(L, 99) is True

def test_bisect_search2_not_found():
    L = list(range(0, 100))
    assert l11.bisect_search2(L, -1) is False
    assert l11.bisect_search2(L, 100) is False
    assert l11.bisect_search2([], 5) is False

def test_bisect_search1_and_2_equivalence():
    L = list(range(0, 30))
    for e in range(-1, 32):
        assert l11.bisect_search1(L, e) == l11.bisect_search2(L, e)

def test_genSubsets_basic():
    result = l11.genSubsets([1, 2])
    expected = [[], [1], [2], [1, 2]]
    assert sorted(result) == sorted(expected)

def test_genSubsets_three_elements():
    result = l11.genSubsets([1, 2, 3])
    expected = [
        [],
        [1], [2], [3],
        [1, 2], [1, 3], [2, 3],
        [1, 2, 3],
    ]
    assert sorted(result) == sorted(expected)

def test_genSubsets_empty():
    assert l11.genSubsets([]) == [[]]

def test_genSubsets_length_property():
    for n in range(6):
        L = list(range(n))
        subsets = l11.genSubsets(L)
        assert len(subsets) == 2 ** n, f"Expected 2^{n} subsets"

def test_combined_behavior():
    """確保三個函式能同時正常運作"""
    nums = list(range(10))
    assert l11.bisect_search2(nums, 5)
    subsets = l11.genSubsets([1, 2, 3])
    assert [1, 2] in subsets