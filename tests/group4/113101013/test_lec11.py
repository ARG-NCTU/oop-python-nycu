# === 二分搜尋版本1：使用 slice ===
def bisect_search1(L, e):
    """
    使用 slicing 的遞迴二分搜尋
    """
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


# === 二分搜尋版本2：使用 low / high index ===
def bisect_search2(L, e):
    """
    使用 low/high index 的遞迴二分搜尋
    """
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)


# === 生成所有子集合 ===
def genSubsets(L):
    """
    回傳列表 L 的所有子集合
    """
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new
