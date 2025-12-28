import sys, os
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lec10_complexity_part1 import linear_search, search, isSubset, intersect

def test_linear_search():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert linear_search(L, 5) is True
    assert linear_search(L, 99) is False

def test_search_sorted():
    L = [1, 3, 5, 7, 9]
    assert search(L, 3) is True
    assert search(L, 2) is False 

def test_intersect():
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 5, 6, 7]
    res = intersect(L1, L2)
    assert 4 in res and 5 in res
    assert 1 not in res
