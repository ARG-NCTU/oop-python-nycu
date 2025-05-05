import lec11_complexity_part2 as lec11
import pytest
# testSet = [1, 2, 3, 4, 5]
# testSet1 = [1, 5, 3]
# testSet2 = [1, 6]

def test_linear_search():
    """
    Test the linear_search function in the lec10 module
    """
    print("\n===== TESTING LINEAR SEARCH FUNCTION =====")
    
    # Test case 1: Element in list
    result = lec11.linear_search(lec11.testList, 5)
    print(f"Searching for 5 in testList: {result}") # 應該輸出 True，因為 5 在 testList 中
    assert result == True, "linear_search failed to find element in list"
    
    # Test case 2: Element not in list
    result = lec11.linear_search(lec11.testList, 200)
    print(f"Searching for 200 in testList: {result}") # 應該輸出 False，因為 200 不在 testList 中
    assert result == False, "linear_search incorrectly found element not in list"
    
    # Test case 3: Empty list
    result = lec11.linear_search([], 5)
    print(f"Searching for 5 in empty list: {result}") # 應該輸出 False
    assert result == False, "linear_search should return False for empty list"
    
    # Test case 4: List with only one element that matches
    result = lec11.linear_search([5], 5)
    print(f"Searching for 5 in [5]: {result}") # 應該輸出 True
    assert result == True, "linear_search failed to find element in single element list"
    
    print("All linear_search tests passed!")

def test_search():
    """
    Test the search function in the lec10 module
    """
    print("\n===== TESTING SEARCH FUNCTION =====")
    
    # Test case 1: Element in list
    result = lec11.search(lec11.testList, 5)
    print(f"Searching for 5 in testList: {result}") # 應該輸出 True
    assert result == True, "search failed to find element in list"
    
    # Test case 2: Element not in list
    result = lec11.search(lec11.testList, 200)
    print(f"Searching for 200 in testList: {result}") # 應該輸出 False
    assert result == False, "search incorrectly found element not in list"
    
    # Test case 3: Empty list
    result = lec11.search([], 5)
    print(f"Searching for 5 in empty list: {result}") # 應該輸出 False
    assert result == False, "search should return False for empty list"
    
    # Test case 4: List with only one element that matches
    result = lec11.search([5], 5)
    print(f"Searching for 5 in [5]: {result}") # 應該輸出 True
    assert result == True, "search failed to find element in single element list"
    
    print("All search tests passed!")

def test_isSubset():
    """
    Test the isSubset function in the lec10 module
    """
    print("\n===== TESTING ISSUBSET FUNCTION =====")
    
    # 測試真正的子集
    result = lec11.isSubset(lec11.testSet, lec11.testSet1)
    print(f"Is testSet a subset of testSet1: {result}") # 應該是 False
    assert result == False, "testSet should not be a subset of testSet1"
    
    # 測試非子集
    result = lec11.isSubset(lec11.testSet2, lec11.testSet)
    print(f"Is testSet2 a subset of testSet: {result}") # 應該是 False
    assert result == False, "testSet2 should not be a subset of testSet"
    
    # 測試空集合
    result = lec11.isSubset([], lec11.testSet)
    print(f"Is empty set a subset of testSet: {result}") # 應該是 True
    assert result == True, "Empty set should be a subset of any set"
    
    # 測試相同集合
    result = lec11.isSubset(lec11.testSet, lec11.testSet)
    print(f"Is testSet a subset of itself: {result}") # 應該是 True
    assert result == True, "A set should be a subset of itself"
    
    # 測試其他情況
    result = lec11.isSubset([1, 2], [1, 2, 3])
    print(f"Is [1, 2] a subset of [1, 2, 3]: {result}") # 應該是 True
    assert result == True, "[1, 2] should be a subset of [1, 2, 3]"
    
    result = lec11.isSubset([1, 4], [1, 2, 3])
    print(f"Is [1, 4] a subset of [1, 2, 3]: {result}") # 應該是 False
    assert result == False, "[1, 4] should not be a subset of [1, 2, 3]"
    
    print("All isSubset tests passed!")

def test_intersect():
    """
    Test the intersect function in the lec10 module
    """
    print("\n===== TESTING INTERSECT FUNCTION =====")
    
    # 測試兩個集合的交集
    result = lec11.intersect(lec11.testSet, lec11.testSet1)
    expected = [1, 3, 5]  # 或者順序可能不同，取決於函數的實現
    print(f"Intersection of testSet and testSet1: {result}")
    print(f"Expected result: {expected}")
    assert sorted(result) == sorted(expected), f"Intersection should be {sorted(expected)}, got {sorted(result)}"
    
    # 測試沒有交集的情況
    result = lec11.intersect([2, 4, 6], [1, 3, 5])
    print(f"Intersection of [2, 4, 6] and [1, 3, 5]: {result}")
    assert result == [], "Intersection of disjoint sets should be empty"
    
    # 測試空集合
    result = lec11.intersect([], lec11.testSet)
    print(f"Intersection of empty set and testSet: {result}")
    assert result == [], "Intersection with empty set should be empty"
    
    # 測試完