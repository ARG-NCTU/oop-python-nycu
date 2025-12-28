def bisect_search2(L, e, start=0, end=None):
    """
    Assumes L is a sorted list.
    Returns True if e is in L, otherwise False.
    Uses recursive bisection search without slicing.
    """
    if end is None:
        end = len(L)
    if start >= end:
        return False

    mid = (start + end) // 2
    if L[mid] == e:
        return True
    elif e < L[mid]:
        return bisect_search2(L, e, start, mid)
    else:
        return bisect_search2(L, e, mid + 1, end)
def genSubsets(L):
    """
    Returns a list of all subsets of list L.
    Uses iterative bit manipulation for performance.
    """
    n = len(L)
    result = []
    for i in range(2 ** n):
        subset = [L[j] for j in range(n) if (i >> j) & 1]
        result.append(subset)
    return result
