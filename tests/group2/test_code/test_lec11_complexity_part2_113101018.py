import pytest
import lec11_complexity_part2 as lec11
import math


# ---------- bisect_search ----------
def test_bisect_search():
    ascending_0_to_99 = list(range(100))           # 0‥99
    assert lec11.bisect_search1(ascending_0_to_99, 50) is True
    assert lec11.bisect_search2(ascending_0_to_99, 50) is True
    assert lec11.bisect_search1(ascending_0_to_99, 101) is False
    assert lec11.bisect_search2(ascending_0_to_99, 101) is False


# ---------- genSubsets ----------
def test_gensubset():
    base_set = [10, 20, 30]
    expected_subsets = [
        [], [10], [20], [10, 20], [30],
        [10, 30], [20, 30], [10, 20, 30]
    ]
    assert lec11.genSubsets(base_set) == expected_subsets

    empty_input = []
    assert lec11.genSubsets(empty_input) == [[]]

