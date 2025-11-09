import pytest
import add_path
from lec10_complexity_part1 import linear_search, search, isSubset, intersect

def test_linear_search_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    e = 5
    assert linear_search(L, e) == True

def test_linear_search_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    e = 7
    assert linear_search(L, e) == False

def test_search_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    e = 9
    assert search(L, e) == True
 
def test_search_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    e = 10
    assert search(L, e) == False
