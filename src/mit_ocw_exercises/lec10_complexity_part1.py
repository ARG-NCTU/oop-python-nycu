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

print("--- Testing linear_search ---")
print(linear_search([1, 2, 3], 2) == True)
print(linear_search([1, 2, 3], 4) == False)
print(linear_search([], 0) == False)

print("\n--- Testing search ---")
print(search([1, 3, 5, 7], 5) == True)
print(search([1, 3, 5, 7], 6) == False)
print(search([], 3) == False)
print(search([2, 4, 6], 1) == False)

print("\n--- Testing isSubset ---")
print(isSubset([1, 3], [1, 2, 3, 4]) == True)
print(isSubset([], [1, 2, 3]) == True)
print(isSubset([1, 5], [2, 3, 4]) == False)
print(isSubset([1, 2], [1, 2]) == True)

print("\n--- Testing intersect ---")
print(intersect([1, 2, 3], [2, 3, 4]) == [2, 3])
print(intersect([], [1, 2]) == [])
print(intersect([1, 1, 2], [1]) == [1])
print(intersect([1, 2, 2], [2, 2, 3]) == [2])
print(intersect([1, 2, 3], [4, 5, 6]) == [])

