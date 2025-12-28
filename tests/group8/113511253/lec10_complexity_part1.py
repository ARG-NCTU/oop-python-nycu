# -*- coding: utf-8 -*-
# from add_path import add_path
# add_path()

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:     # Important: list must be sorted for early stop
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

def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)

    res = []
    for e in tmp:
        if not (e in res):
            res.append(e)

    return res
