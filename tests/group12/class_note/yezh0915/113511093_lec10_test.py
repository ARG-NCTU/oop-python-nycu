import pytest
from src.mit_ocw_exercises.lec10_complexity_part1 import linear_search, search, isSubset, intersect

def test_linear_search():
    assert linear_search([1, 2, 3, 4], 3) is True
    assert linear_search([1, 2, 3, 4], 5) is False
    assert linear_search([], 1) is False


