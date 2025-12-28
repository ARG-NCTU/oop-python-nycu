import sys, os
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lec11_complexity_part2 import bisect_search1, bisect_search2, genSubsets, genPerms

def test_bisect():
    L = list(range(20))
    assert bisect_search1(L, 10) is True
    assert bisect_search2(L, 10) is True
    assert bisect_search1(L, 99) is False

def test_genSubsets():
    s = [1, 2]
    res = genSubsets(s)
    assert len(res) == 4

def test_genPerms():
    p = [1, 2, 3]
    res = genPerms(p)
    assert len(res) == 6
