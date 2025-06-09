import pytest 

def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res

def test_intersect():
    assert intersect([1, 2, 3], [3, 4, 5]) == [3]
    assert intersect([1, 2, 2, 3], [2, 3, 3]) == [2, 3]
    assert intersect([], [1, 2, 3]) == []
    assert intersect([1, 2, 3], []) == []
    assert intersect([1, 2, 3], [4, 5, 6]) == []