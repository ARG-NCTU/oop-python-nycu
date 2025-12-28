import pytest
import random
from add_path import add_path
add_path()
from lec11_complexity_part2 import bisect_search1, bisect_search2, genSubsets, genPerms

def test_binary_search_found():
    L = list(range(100))
    assert bisect_search1(L, 42) == True

def test_binary_search_not_found():
    L = list(range(100))
    assert bisect_search1(L, 150) == False

def test_binary_search2_found():
    L = list(range(100))
    assert bisect_search2(L, 42) == True

def test_binary_search2_not_found():
    L = list(range(100))
    assert bisect_search2(L, 150) == False

def union(L1, L2):
    res = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            if L1[i] not in res: res.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            if L2[j] not in res: res.append(L2[j])
            j += 1
        else:
            if L1[i] not in res: res.append(L1[i])
            i += 1; j += 1
    while i < len(L1):
        if L1[i] not in res: res.append(L1[i])
        i += 1
    while j < len(L2):
        if L2[j] not in res: res.append(L2[j])
        j += 1
    return res

def difference(L1, L2):
    res = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            res.append(L1[i]); i += 1
        elif L1[i] > L2[j]:
            j += 1
        else:
            i += 1; j += 1
    while i < len(L1):
        res.append(L1[i]); i += 1
    return res

def test_union():
    assert union([1, 3, 5, 7], [2, 3, 6, 8]) == [1, 2, 3, 5, 6, 7, 8]

def test_difference():  
    assert difference([1, 2, 3, 4, 5], [2, 4]) == [1, 3, 5]

@pytest.mark.parametrize("n", [10, 50, 100])
def test_bisect_search1_random_sizes(n):
    random.seed(123)
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert bisect_search1(L, e)

