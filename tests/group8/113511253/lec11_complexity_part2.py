# -*- coding: utf-8 -*-
# from add_path import add_path
# add_path()

def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: 
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1]) 
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new

def genPerms(L):
    if len(L) == 0:
        return [[]]
    if len(L) == 1:
        return [L[:]] 

    res = []
    for i in range(len(L)):
        first = L[i]
        rest = L[:i] + L[i+1:]
        for p in genPerms(rest):
            res.append([first] + p)
    return res
