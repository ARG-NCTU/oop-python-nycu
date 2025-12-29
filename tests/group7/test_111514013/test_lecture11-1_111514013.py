# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:13 2016

@author: ericgrimson
"""

def bisect_search1(L, e):
    complexity = 0  # 計算複雜度
    print('low: ' + str(L[0]) + '; high: ' + str(L[-1]))
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
        complexity = 0  # 計算複雜度
        print('low: ' + str(low) + '; high: ' + str(high))  # added to visualize
        if high == low:
            complexity += 1
            return L[low] == e, complexity
        mid = (low + high)//2
        complexity += 1
        if L[mid] == e:
            return True, complexity
        elif L[mid] > e:
            if low == mid:  # nothing left to search
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
    complexity = 0  # 計算複雜度
    if len(L) == 0:
        return [[]], complexity  # list of empty list
    smaller, sub_complexity = genSubsets(L[:-1])  # all subsets without last element
    complexity += sub_complexity
    extra = L[-1:]  # create a list of just last element
    new = []
    for small in smaller:
        complexity += 1
        new.append(small + extra)  # for all smaller solutions, add one with last element
    return smaller + new, complexity  # combine those with last element and those without

# 測試程式碼
testList = []
for i in range(100):
    testList.append(i)

result, complexity = bisect_search1(testList, 6)
print(result, "Complexity:", complexity)

result, complexity = bisect_search2(testList, 76)
print(result, "Complexity:", complexity)

testSet = [1, 2, 3, 4]
result, complexity = genSubsets(testSet)
print(result, "Complexity:", complexity)

#print(list(range(100)))
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
    assert result == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert complexity == 7
# -*- coding: utf-8 -*-