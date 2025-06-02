import lec_10.py as lec10
import pytest
import time
import random

def test_linear_search():
    assert lec10.linear_search([1, 2, 3, 4], 3) == True
    assert lec10.linear_search([1, 2, 3, 4], 5) == False
    assert lec10.linear_search([], 1) == False

def test_search():
    assert lec10.search([1, 3, 5, 7], 3) == True
    assert lec10.search([1, 3, 5, 7], 2) == False
    assert lec10.search([1, 3, 5, 7], 8) == False
    assert lec10.search([], 1) == False