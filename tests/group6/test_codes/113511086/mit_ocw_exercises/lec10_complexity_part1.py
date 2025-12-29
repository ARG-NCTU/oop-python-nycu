def linear_search(L, e):
    """
    Returns True if e is in list L, otherwise False.
    """
    for elem in L:
        if elem == e:
            return True
    return False

def intersect(L1, L2):
    """
    Returns a list of elements that appear in both L1 and L2.
    Each element appears only once in the result.
    Order follows L1.
    """
    result = []
    for elem in L1:
        if elem in L2 and elem not in result:
            result.append(elem)
    return result

def isSubset(L1, L2):
    """
    Returns True if every element in L1 is also in L2.
    """
    for elem in L1:
        if elem not in L2:
            return False
    return True

def search(L, e):
    """
    Assumes L is sorted.
    Returns True if e is in L, otherwise False.
    Uses linear search (not binary search) as in MIT lecture.
    """
    for elem in L:
        if elem == e:
            return True
        if elem > e:
            return False
    return False
