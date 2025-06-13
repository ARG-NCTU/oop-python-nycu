import os
import sys
import pytest
import math

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec11_complexity_part2 as lec11

sorted_list = list(range(100))

### --- bisect_search1 --- ###
@pytest.mark.parametrize("L, e, expected", [
    ([5], 5, True),
    ([5], 2, False),
    (list(range(100)), 76, True),
    (list(range(100)), 101, False),
])
def test_bisect_search1(L, e, expected):
    assert lec11.bisect_search1(L, e) == expected

### --- bisect_search2 --- ###
@pytest.mark.parametrize("L, e, expected", [
    ([], 10, False),
    ([5], 5, True),
    ([5], 2, False),
    (sorted_list, 76, True),
    (sorted_list, 101, False),
])
def test_bisect_search2(L, e, expected):
    assert lec11.bisect_search2(L, e) == expected

### --- genSubsets --- ###
def test_gen_subsets_base_case():
    assert lec11.genSubsets([]) == [[]]

def test_gen_subsets_single():
    assert lec11.genSubsets([1]) == [[], [1]]

def test_gen_subsets_two():
    subsets = lec11.genSubsets([1, 2])
    expected = [[], [1], [2], [1, 2]]
    assert sorted(subsets) == sorted(expected)

def test_gen_subsets_full():
    from math import comb
    base = [1, 2, 3, 4]
    subsets = lec11.genSubsets(base)
    assert len(subsets) == 2 ** len(base)
    for s in subsets:
        assert all(x in base for x in s)
