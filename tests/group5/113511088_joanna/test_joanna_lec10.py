from lec10_final import *

def test_linear_search():
    L = [1, 3, 5, 7]
    assert linear_search(L, 5) == True
    assert linear_search(L, 2) == False

def test_search_sorted():
    L = [1, 3, 5, 7, 9]
    assert search(L, 7) == True
    assert search(L, 4) == False
    assert search(L, 10) == False

def test_isSubset():
    assert isSubset([1, 2], [1, 2, 3]) == True
    assert isSubset([4], [1, 2, 3]) == False
    assert isSubset([], [1, 2, 3]) == True

def test_intersect():
    assert intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersect([1, 2, 2], [2, 2]) == [2]
    assert intersect([], [1, 2]) == []
