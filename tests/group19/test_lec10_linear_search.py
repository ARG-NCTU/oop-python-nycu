import pytest

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

def test_linear_search():
    # Test cases
    assert linear_search([1, 2, 3, 4, 5], 3) == True
    assert linear_search([1, 2, 3, 4, 5], 6) == False
    assert linear_search([], 1) == False
    assert linear_search(['a', 'b', 'c'], 'b') == True
    assert linear_search(['a', 'b', 'c'], 'd') == False

