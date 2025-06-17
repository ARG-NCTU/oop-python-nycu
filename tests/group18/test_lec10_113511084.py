import os
import sys
import pytest
import math

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec10_complexity_part1 as lec10_p1

### --- linear_search --- ###
@pytest.mark.parametrize("L, e, expected", [
    ([1, 3, 4, 5, 9], 4, True),
    ([1, 3, 4, 5, 9], 6, False),
    ([], 1, False),
])
def test_linear_search(L, e, expected):
    assert lec10_p1.linear_search(L, e) == expected

### --- search (sorted, early stopping) --- ###
@pytest.mark.parametrize("L, e, expected", [
    ([1, 3, 4, 5, 9], 4, True),     
    ([1, 3, 4, 5, 9], 6, False),   
    ([1, 3, 4, 5, 9], 10, False),  
    ([], 1, False),               
])
def test_sorted_search(L, e, expected):
    assert lec10_p1.search(L, e) == expected

### --- isSubset --- ###
@pytest.mark.parametrize("L1, L2, expected", [
    ([1, 2], [1, 2, 3], True),    
    ([1, 4], [1, 2, 3], False),    
    ([], [1, 2, 3], True),         
    ([1, 2, 3], [], False),       
])
def test_is_subset(L1, L2, expected):
    assert lec10_p1.isSubset(L1, L2) == expected

### --- intersect --- ###
@pytest.mark.parametrize("L1, L2, expected", [
    ([1, 2, 3], [3, 4, 5], [3]),
    ([1, 2, 3], [4, 5], []),
    ([1, 2, 2, 3], [2, 2, 4], [2]),
    ([], [1, 2, 3], []),
    ([1, 2, 3], [], []),
])
def test_intersect(L1, L2, expected):
    assert lec10_p1.intersect(L1, L2) == expected
