import lec_test_codes.add_path
import mit_ocw_exercises.lec10_complexity_part1 as l10
import pytest

def test_linear_search():
    testList = [1, 4, 2, 8, 5, 7]
    assert l10.linear_search(testList, 5) == True
    assert l10.linear_search(testList, 10) == False
    assert l10.linear_search([], 5) == False
    assert l10.linear_search([5,], 5) == True

def test_search():
    testList = [1, 3, 4, 5, 9, 18, 27]
    assert l10.search(testList, 5) == True
    assert l10.search(testList, 10) == False
    assert l10.search([], 1) == False
    assert l10.search([1], 1) == True
    assert l10.search(testList, 0) == False

