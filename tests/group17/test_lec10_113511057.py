import lec10_complexity_part1 as lec10
import pytest
import time
import random

def test_linear_search():
    assert lec10.linear_search([1, 2, 3, 4], 3) == True
    assert lec10.linear_search([1, 2, 3, 4], 5) == False
    assert lec10.linear_search([], 1) == False

