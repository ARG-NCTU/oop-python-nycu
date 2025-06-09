import pytest

def bisect_search1(L, e):
    print('low: ' + str(L[0]) + '; high: ' + str(L[-1]))
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
        print('low: ' + str(low) + '; high: ' + str(high))  # added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

def test_bisect_search():
    L = [1, 3, 5, 7, 9, 11, 13, 15]
    assert bisect_search1(L, 5) == True
    assert bisect_search1(L, 6) == False
    assert bisect_search2(L, 5) == True
    assert bisect_search2(L, 6) == False
    assert bisect_search1([], 5) == False
    assert bisect_search2([], 5) == False
    assert bisect_search1([5], 5) == True
    assert bisect_search1([5], 6) == False
    assert bisect_search2([5], 5) == True
    assert bisect_search2([5], 6) == False
    assert bisect_search1([1, 2, 3], 2) == True
    assert bisect_search2([1, 2, 3], 2) == True
    assert bisect_search1([1, 2, 3], 4) == False
    assert bisect_search2([1, 2, 3], 4) == False


