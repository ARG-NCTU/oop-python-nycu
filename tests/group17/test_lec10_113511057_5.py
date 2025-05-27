import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest
import time
import random

def test_linear_search():
    assert linear_search([10, 20, 30, 40], 20) == True
    assert linear_search([10, 20, 30, 40], 50) == False
    assert linear_search([], 0) == False

def test_search():
    assert search([2, 4, 6, 8, 10], 6) == True
    assert search([2, 4, 6, 8, 10], 5) == False
    assert search([2, 4, 6, 8, 10], 11) == False
    assert search([], 3) == False

