import pytest
import random
from add_path import add_path
add_path()
from lec10_complexity_part1 import linear_search, search, isSubset, intersect

"""
Lec 10 Tests: Complexity checks.
"""

def test_linear_search_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert linear_search(L, 5) == True

def test_linear_search_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert linear_search(L, 7) == False

def test_search_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert search(L, 9) == True

def test_search_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert search(L, 10) == False

def test_isSubset_true():
    assert isSubset([1, 3, 5], [1, 2, 3, 4, 5]) == True 

def test_isSubset_false():
    assert isSubset([1, 6], [1, 2, 3, 4, 5]) == False

def test_intersect():
    assert intersect([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]) == [4, 5]

def test_intersect_no_common():
    assert intersect([1, 2, 3], [4, 5, 6]) == []

def test_isSubset_empty():
    assert isSubset([], [1,2,3]) == True

def test_intersect_sorted_output():
    assert sorted(intersect([5,1,3], [3,5,7])) == [3,5]

@pytest.mark.parametrize("n", [10, 50, 100])
def test_search_random_sizes(n):
    random.seed(123)
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert search(L, e)
# End of file
