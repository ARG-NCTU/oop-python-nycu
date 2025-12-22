def bisect_search2(L, e):
    """
    Assumes L is a sorted list.
    Returns True if e is in L, otherwise False.
    Uses recursive bisection search.
    """
    if L == []:
        return False

    mid = len(L) // 2

    if L[mid] == e:
        return True
    elif e < L[mid]:
        return bisect_search2(L[:mid], e)
    else:
        return bisect_search2(L[mid+1:], e)
def genSubsets(L):
    """
    Returns a list of all subsets of list L.
    Order follows MIT OCW lecture example.
    """
    if len(L) == 0:
        return [[]]

    smaller = genSubsets(L[:-1])
    extra = L[-1:]

    new = []
    for subset in smaller:
        new.append(subset + extra)

    return smaller + new
