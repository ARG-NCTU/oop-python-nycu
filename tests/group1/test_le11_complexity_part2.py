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

def test_difference():
    L1 = [1, 2, 3, 4]
    L2 = [3, 4, 5]
    assert difference(L1, L2) == [1, 2]

@pytest.mark.parametrize("n", [10, 50, 100])
def test_binary_search_random_sizes(n):
    random.seed(123)
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert binary_search(L, e) == True

def test_difference_random_sizes():
    random.seed(123)
    L1 = sorted(random.sample(range(0, 1000), 50))
    L2 = sorted(random.sample(range(0, 1000), 30))
    result = difference(L1, L2)
    for item in result:
        assert item in L1 and item not in L2
    expected = [item for item in L1 if item not in L2]
    assert sorted(result) == sorted(expected)

def test_union_random_sizes():
    random.seed(123)
    L1 = sorted(random.sample(range(0, 1000), 50))
    L2 = sorted(random.sample(range(0, 1000), 30))
    result = union(L1, L2)
    expected = sorted(set(L1).union(set(L2)))
    assert result == expected

@pytest.mark.parametrize("n", [10, 50, 100])
def test_union_random_sizes(n):
    random.seed(123)
    L1 = sorted(random.sample(range(0, 1000), n))
    L2 = sorted(random.sample(range(0, 1000), n))
    result = union(L1, L2)
    expected = sorted(set(L1).union(set(L2)))
    assert result == expected