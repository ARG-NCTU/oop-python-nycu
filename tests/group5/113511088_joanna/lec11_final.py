def bisect_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)

def bisect_search2(L, e):
    def bisect_helper(L, e, low, high):
        if high < low:
            return False
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            return bisect_helper(L, e, low, mid - 1)
        else:
            return bisect_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    return bisect_helper(L, e, 0, len(L) - 1)

def genSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for subset in smaller:
        new.append(subset + extra)
    return smaller + new
