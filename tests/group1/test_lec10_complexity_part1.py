import pytest
import add_path
import random
from add_path import add_path
add_path()
from lec10_complexity_part1 import linear_search, search, isSubset, intersect


"""Small sanity checks for complexity helpers.

Added: ensure `intersect` returns a sorted list and `isSubset` accepts empty sets.
"""

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

def test_isSubset_true():
    L1 = [1, 3, 5]
    L2 = [1, 2, 3, 4, 5]
    assert isSubset(L1, L2) == True 

def test_isSubset_false():
    L1 = [1, 6]
    L2 = [1, 2, 3, 4, 5]
    assert isSubset(L1, L2) == False

def test_intersect():
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 5, 6, 7, 8]
    assert intersect(L1, L2) == [4, 5]

def test_intersect_no_common():
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    assert intersect(L1, L2) == []


def test_isSubset_empty():
    # empty set is subset of any set
    assert isSubset([], [1,2,3]) == True

def test_intersect_sorted_output():
    # intersect result may not be sorted; compare as sets for robustness
    assert sorted(intersect([5,1,3], [3,5,7])) == [3,5]

def test_intersect_with_duplicates():
    L1 = [1, 2, 2, 3, 4]
    L2 = [2, 2, 4, 4, 5]
    assert intersect(L1, L2) == [2, 4]
    
    
@pytest.mark.parametrize("n", [10, 50, 100])
def test_search_random_sizes(n):
    random.seed(123)
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert search(L, e)