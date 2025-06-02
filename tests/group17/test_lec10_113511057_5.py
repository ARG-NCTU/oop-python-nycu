import lec_10.py as lec10
import pytest
import time
import random

def test_linear_search():
    assert lec10.linear_search([10, 20, 30, 40], 20) == True
    assert lec10.linear_search([10, 20, 30, 40], 50) == False
    assert lec10.linear_search([], 0) == False

def test_search():
    assert lec10.search([2, 4, 6, 8, 10], 6) == True
    assert lec10.search([2, 4, 6, 8, 10], 5) == False
    assert lec10.search([2, 4, 6, 8, 10], 11) == False
    assert lec10.search([], 3) == False

