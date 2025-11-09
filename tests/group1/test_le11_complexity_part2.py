from lec11_complexity_part2 import bisect_search1, bisect_search2, genSubsets, genPerms
import pytest
import add_path
import random
def test_binary_search_found():
    L = list(range(100))
    e = 42
    assert bisect_search1(L, e) == True

def test_binary_search_not_found():
    L = list(range(100))
    e = 150
    assert bisect_search1(L, e) == False

def test_binary_search2_found():
    L = list(range(100))
    e = 42
    assert bisect_search2(L, e) == True

def test_binary_search2_not_found():
    L = list(range(100))
    e = 150
    assert bisect_search2(L, e) == False

def union(L1, L2):
    res = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            if L1[i] not in res:
                res.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            if L2[j] not in res:
                res.append(L2[j])
            j += 1
        else:
            if L1[i] not in res:
                res.append(L1[i])
            i += 1
            j += 1
    while i < len(L1):
        if L1[i] not in res:
            res.append(L1[i])
        i += 1
    while j < len(L2):
        if L2[j] not in res:
            res.append(L2[j])
        j += 1
    return res

def difference(L1, L2):
    res = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            res.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            j += 1
        else:
            i += 1
            j += 1
    while i < len(L1):
        res.append(L1[i])
        i += 1
    return res

def test_union():
    L1 = [1, 3, 5, 7]
    L2 = [2, 3, 6, 8]
    assert union(L1, L2) == [1, 2, 3, 5, 6, 7, 8]

def test_union_random():
    random.seed(42)
    L1 = sorted(random.sample(range(50), 10))
    L2 = sorted(random.sample(range(50), 10))
    result = union(L1, L2)
    # 檢查是否包含所有元素且不重複
    assert sorted(set(L1 + L2)) == result

def test_difference():  
    L1 = [1, 2, 3, 4, 5]
    L2 = [2, 4]
    assert difference(L1, L2) == [1, 3, 5]