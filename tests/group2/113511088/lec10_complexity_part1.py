# -*- coding: utf-8 -*-
"""
lec10_search_113511088.py
Search / subset / intersection utilities
"""

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


def search(L, e):
    """
    Assumes L is sorted (ascending).
    Returns True if e in L, else False.
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def isSubset(L1, L2):
    """
    Returns True if every element in L1 appears in L2 (membership by equality).
    """
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(L1, L2):
    """
    Returns a list of unique elements that appear in both L1 and L2.
    Order follows first appearance in L1.
    """
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)

    res = []
    for e in tmp:
        if e not in res:
            res.append(e)
    return res


if __name__ == "__main__":
    # optional quick checks
    testList = [1, 3, 4, 5, 9, 18, 27]
    print(linear_search(testList, 4))
    print(search(testList, 9))
    print(search(testList, 8))

    testSet = [1, 2, 3, 4, 5]
    testSet1 = [1, 5, 3]
    testSet2 = [1, 6]
    print(isSubset(testSet1, testSet))
    print(isSubset(testSet2, testSet))
    print(intersect([1, 2, 2, 3], [2, 3, 4, 2]))
