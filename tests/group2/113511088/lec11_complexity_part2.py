# -*- coding: utf-8 -*-
"""
lec11_bisect_subsets_113511088.py
Binary search (recursive) + generating subsets (recursion)
"""

def bisect_search1(L, e, verbose=False):
    """
    Binary search by slicing (recursive).
    Assumes L is sorted.
    """
    if L == []:
        return False

    if verbose:
        print('low: ' + str(L[0]) + '; high: ' + str(L[-1]))

    if len(L) == 1:
        return L[0] == e

    half = len(L) // 2
    if L[half] > e:
        return bisect_search1(L[:half], e, verbose)
    else:
        return bisect_search1(L[half:], e, verbose)


def bisect_search2(L, e, verbose=False):
    """
    Binary search using helper with indices.
    Assumes L is sorted.
    """
    def bisect_search_helper(L, e, low, high):
        if verbose:
            print('low: ' + str(low) + '; high: ' + str(high))

        if high < low:
            return False

        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    return bisect_search_helper(L, e, 0, len(L) - 1)


def genSubsets(L):
    """
    Returns a list of all subsets of L.
    Example: [1,2] -> [[], [1], [2], [1,2]] (order may vary)
    """
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new


if __name__ == "__main__":
    testList = list(range(100))
    print(bisect_search1(testList, 76, verbose=True))
    print(bisect_search2(testList, 76, verbose=True))

    testSet = [1, 2, 3, 4]
    print(genSubsets(testSet))
