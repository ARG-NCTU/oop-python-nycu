def linear_search(L, e):
    found = False
    complexity = 0 #time complexity  
    for i in range(len(L)):
        complexity += 1
        if e == L[i]:
            found = True
    return found, complexity
def search(L, e):
    complexity = 0
    for i in range(len(L)):
        complexity += 1
        if L[i] == e:
            return True, complexity
        if L[i] > e:
            return False, complexity
    return False, complexity
def isSubset(L1, L2):
    complexity = 0 #time complexity
    for e1 in L1:
        matched = False
        for e2 in L2:
            complexity ++
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False, complexity
    return True, complexity
def intersect(L1, L2):
    tmp = []
    complexity = 0
    for e1 in L1:
        for e2 in L2:
            complexity += 1
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        # complexity += 1
        if not(e in res):
            res.append(e)
    return res, complexity
def test_linear_search():
    found, complexity = linear_search([1, 3, 4, 5, 9, 18, 27], 5)
    assert found is True
    assert complexity == 7
def test_search():
    found, complexity = search([1, 3, 4, 5, 9, 18, 27], 6)
    assert found is False
    assert complexity == 5
def test_isSubset():
    is_subset, complexity = isSubset([1, 3, 5], [1, 2, 3, 4, 5])
    assert is_subset is True
    assert complexity ==9
def test_intersect():
    result, complexity = intersect([1, 2, 3], [2, 3, 4])
    assert result == [2, 3]
    assert complexity == 9