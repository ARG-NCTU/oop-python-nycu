def bisect_search1(L, e):
    complexity = 0
    if L == []:
        return False, complexity
    elif len(L) == 1:
        complexity += 1
        return L[0] == e, complexity
    else:
        half = len(L)//2
        complexity += 1
        if L[half] > e:
            result, sub_complexity = bisect_search1(L[:half], e)
            complexity += sub_complexity
            return result, complexity
        else:
            result, sub_complexity = bisect_search1(L[half:], e)
            complexity += sub_complexity
            return result, complexity

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        complexity = 0
        if high == low:
            complexity += 1
            return L[low] == e, complexity
        mid = (low + high)//2
        complexity += 1
        if L[mid] == e:
            return True, complexity
        elif L[mid] > e:
            if low == mid:
                return False, complexity
            else:
                result, sub_complexity = bisect_search_helper(L, e, low, mid - 1)
                complexity += sub_complexity
                return result, complexity
        else:
            result, sub_complexity = bisect_search_helper(L, e, mid + 1, high)
            complexity += sub_complexity
            return result, complexity

    if len(L) == 0:
        return False, 0
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

def genSubsets(L):
    complexity = 0
    if len(L) == 0:
        return [[]], complexity
    smaller, sub_complexity = genSubsets(L[:-1])
    complexity += sub_complexity
    extra = L[-1:]
    new = []
    for small in smaller:
        complexity += 1
        new.append(small + extra)
    return smaller + new, complexity

# --- Pytest Functions ---

def test_bisect_search1():
    result, complexity = bisect_search1(list(range(100)), 6)
    assert result is True
    assert complexity == 7

def test_bisect_search2():
    result, complexity = bisect_search2(list(range(100)), 76)
    assert result is True
    assert complexity == 7  

def test_genSubsets():  
    result, complexity = genSubsets([1, 2, 3])
    # The order of subsets generated is specific to the recursion
    assert result == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert complexity == 7