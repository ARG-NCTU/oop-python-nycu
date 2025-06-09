import pytest

def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element
    return smaller+new  # combine those with last element and those without

def test_genSubsets():
    assert genSubsets([]) == [[]]
    assert genSubsets([1]) == [[], [1]]
    assert genSubsets([1, 2]) == [[], [1], [2], [1, 2]]
    assert genSubsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert genSubsets([1, 2, 3, 4]) == [
        [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
        [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
        [2, 3, 4], [1, 2, 3, 4]
    ]