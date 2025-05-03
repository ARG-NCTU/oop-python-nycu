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
for number in range(max(testList) + 1):
    if linear_search(testList, number):
        print(number, "is in the list")
    else:
        print(number, "is not in the list")

def search(L, e):   ##this search a sorted list, which means it may function out of expectation if user give an unsorted list
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

if isSubset(testSet1, testSet):
    print(testSet1, "is a subset of", testSet)
if isSubset(testSet2, testSet):
    print(testSet2, "is a subset of", testSet)
else:
    print(testSet2, "is not a subset of", testSet)

def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []    ##remove duplicates
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res

interTestSet1 = [1, 2, 3, 4, 5, 5]
interTestSet2 = [1, 5, 3, 3]
if intersect(interTestSet1, interTestSet2): ##if the intersection is not empty
    print("The intersection of", interTestSet1, "and", interTestSet2, "is", intersect(interTestSet1, interTestSet2))
if intersect(interTestSet2, interTestSet1):
    print("The intersection of", interTestSet2, "and", interTestSet1, "is", intersect(interTestSet2, interTestSet1))
print("The intersection of", interTestSet1, "and", interTestSet1, "is", intersect(interTestSet1, interTestSet1))
