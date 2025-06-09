import pytest

def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

def test_isSubset():
    assert isSubset([1, 2, 3], [1, 2, 3, 4, 5]) == True
    assert isSubset([1, 2, 3], [4, 5]) == False
    assert isSubset([], [1, 2, 3]) == True
    assert isSubset([1, 2, 3], []) == False
    assert isSubset([1, 2, 3], [3, 2, 1]) == True
    assert isSubset([1, 2, 3], [1, 2, 3]) == True
    assert isSubset([1, 2, 3], [1, 2, 3, 4]) == True
    assert isSubset([1, 2, 3], [2, 3]) == False