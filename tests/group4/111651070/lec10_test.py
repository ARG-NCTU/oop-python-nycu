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
def test_linear_search():
    assert linear_search(testList, 1) == True
    assert linear_search(testList, 2) == False
    assert linear_search(testList, 3) == True
    assert linear_search(testList, 4) == True
    assert linear_search(testList, 5) == True
    assert linear_search(testList, 6) == False
    assert linear_search(testList, 7) == False
    assert linear_search(testList, 8) == False
    assert linear_search(testList, 9) == True
    assert linear_search(testList, 10) == False

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def test_search():
    assert search(testList, 1) == True
    assert search(testList, 2) == False
    assert search(testList, 3) == True
    assert search(testList, 4) == True
    assert search(testList, 5) == True
    assert search(testList, 6) == False
    assert search(testList, 7) == False
    assert search(testList, 8) == False
    assert search(testList, 9) == True
    assert search(testList, 10) == False

# L1是L2的Subset
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

def test_isSubset():
    assert isSubset(testSet1, testSet) == True
    assert isSubset(testSet2, testSet) == False
    assert isSubset(testSet, testSet1) == False
    assert isSubset(testSet, testSet2) == False

def intersect(L1, L2):
    tmp = [] # 共有的element
    # 重複元素的順序與L1的順序相同
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = [] # 去重重複的共同元素
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res

def test_intersect():
    assert intersect(testSet1, testSet) == [1, 5, 3] # 和testSet1的順序相同
    assert intersect(testSet2, testSet) == [1]
    assert intersect(testSet, testSet1) == [1, 3, 5] # 和testSet的順序相同
    assert intersect(testSet, testSet2) == [1]