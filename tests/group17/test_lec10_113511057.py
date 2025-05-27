import add_path
import mit_ocw_exercises.lec10_complexity_part1 as lec10
import pytest
import time
import random

def test_linear_search():
    assert linear_search([1, 2, 3, 4], 3) == True
    assert linear_search([1, 2, 3, 4], 5) == False
    assert linear_search([], 1) == False

