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
