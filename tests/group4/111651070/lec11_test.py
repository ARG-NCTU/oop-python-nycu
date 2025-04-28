# 從array L中分半找是否有e
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
    # 找Array L中index = low到index=high的範圍中是否有e
    def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  #added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

testList = []
for i in range(100):
    testList.append(i)

def test_bisect_search():
    assert bisect_search1(testList, 76) == True
    assert bisect_search1(testList, 101) == False
    assert bisect_search2(testList, 77) == True
    assert bisect_search2(testList, 102) == False

# 找出array L中的所有subsets組合
def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]] #list of empty list
    # 產生一個2維的list smaller包含L中除了最後一個element的所有subsets
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    # new用來存smaller+考慮extra的所有subsets，因此會與smaller的長度一樣
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element
    # 回傳smaller和new的所有subsets
    return smaller+new  # combine those with last element and those without


testSet = [1,2,3,4]
def test_genSubsets():
    assert genSubsets(testSet) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
    assert genSubsets([]) == [[]]
    assert genSubsets([5]) == [[], [5]]
    assert genSubsets([5,6]) == [[], [5], [6], [5,6]]
