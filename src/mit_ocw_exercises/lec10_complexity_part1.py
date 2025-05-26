# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:27:54 2016

@author: ericgrimson
"""

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

testList = [1, 3, 4, 5, 9, 18, 27]

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


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


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

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

def test_linear_search():
    print("--- Testing linear_search ---")
    assert linear_search([1, 2, 3], 2) == True
    assert linear_search([1, 2, 3], 4) == False
    assert linear_search([], 0) == False
    assert linear_search([10, 20, 30], 30) == True
    assert linear_search([5, 6, 7], 1) == False
    print("linear_search tests passed.")

def test_search():
    print("\n--- Testing search ---")
    assert search([1, 3, 5, 7], 5) == True
    assert search([1, 3, 5, 7], 6) == False
    assert search([], 3) == False
    assert search([2, 4, 6], 1) == False
    assert search([1, 3, 5, 7, 9], 9) == True
    assert search([1, 3, 5, 7, 9], 10) == False
    print("search tests passed.")

def test_isSubset():
    print("\n--- Testing isSubset ---")
    assert isSubset([1, 3], [1, 2, 3, 4]) == True
    assert isSubset([], [1, 2, 3]) == True
    assert isSubset([1, 5], [2, 3, 4]) == False
    assert isSubset([1, 2], [1, 2]) == True
    assert isSubset([5], [5, 6, 7]) == True
    assert isSubset([8], [1, 2, 3]) == False
    print("isSubset tests passed.")

def test_intersect():
    print("\n--- Testing intersect ---")
    assert intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersect([], [1, 2]) == []
    assert intersect([1, 1, 2], [1]) == [1]
    assert intersect([1, 2, 2], [2, 2, 3]) == [2]
    assert intersect([1, 2, 3], [4, 5, 6]) == []
    assert intersect([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert intersect([7, 8], [8, 9]) == [8]
    print("intersect tests passed.")

# Run all tests
test_linear_search()
test_search()
test_isSubset()
test_intersect()

