# === 線性搜尋 ===
def linear_search(L, e):
    """
    線性搜尋
    回傳 True 如果 e 在 L 裡面，否則 False
    """
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


# === 有序列表中的搜尋 ===
def search(L, e):
    """
    有序列表中的搜尋（假設 L 已經遞增排序）
    遇到大於 e 的元素可以提前停止
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


# === 判斷是否為子集合 ===
def isSubset(L1, L2):
    """
    判斷 L1 是否是 L2 的子集合
    """
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


# === 求兩個列表的交集 ===
def intersect(L1, L2):
    """
    傳回 L1 和 L2 的交集（無重複元素）
    """
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if e not in res:
            res.append(e)
    return res

# === 求兩個列表的聯集 ===
def union(L1, L2):
    """
    傳回 L1 和 L2 的聯集（無重複元素）
    """
    res = []
    for e in L1 + L2:
        if e not in res:
            res.append(e)
    return
    res
# === 求兩個列表的差集 ===
def difference(L1, L2):
    """
    傳回 L1 和 L2 的差集（L1 中有而 L2 中沒有的元素）
    """
    res = []
    for e in L1:
        if e not in L2:
            res.append(e)
    return res

def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 3) == True
    assert linear_search([1, 2, 3, 4, 5], 6) == False
    assert linear_search([], 1) == False
def test_search():
    assert search([1, 2, 3, 4, 5], 3) == True
    assert search([1, 2, 3, 4, 5], 6) == False
    assert search([], 1) == False

def test_isSubset():
    assert isSubset([1, 2], [1, 2, 3]) == True
    assert isSubset([1, 4], [1, 2, 3]) == False
    assert isSubset([], [1, 2, 3]) == True
    assert isSubset([], []) == True
def test_intersect():
    assert intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersect([1, 2], [3, 4]) == []
    assert intersect([], [1, 2]) == []
    assert intersect([], []) == []


def test_difference():
    assert difference([1, 2, 3], [2, 3, 4]) == [1]
    assert difference([1, 2], [3, 4]) == [1, 2]
    assert difference([], [1, 2]) == []
    assert difference([], []) == []

def test_all():
    test_linear_search()
    test_search()
    test_isSubset()
    test_intersect()
    test_difference()
    # Add more tests as needed
