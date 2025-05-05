import add_path
import lec10_complexity_part1 as lec10
import pytest
# testSet = [1, 2, 3, 4, 5]
# testSet1 = [1, 5, 3]
# testSet2 = [1, 6]

result = lec10.linear_search(lec10.testList, 5)
print(result)  # 應該輸出 True，因為 5 在 testList 中
 
result2 = lec10.search(lec10.testList,5)
print(result2)
 
result3 = lec10.isSubset(lec10.testSet1,lec10.testSet2)
print(result2)
def test_isSubset():
    # 測試真正的子集
    assert lec10.isSubset(lec10.testSet, lec10.testSet1) == False
    
    # 測試非子集
    assert lec10.isSubset(lec10.testSet2, lec10.testSet) == False
    
    # 測試空集合
    assert lec10.isSubset([], lec10.testSet) == True
    
    # 測試相同集合
    assert lec10.isSubset(lec10.testSet, lec10.testSet) == True
    
    # 測試其他情況
    assert lec10.isSubset([1, 2], [1, 2, 3]) == True
    assert lec10.isSubset([1, 4], [1, 2, 3]) == False

def test_intersect():
    result = lec10.intersect(lec10.testSet, lec10.testSet1)
    
    # 檢查結果是否包含正確的元素
    # 注意：集合的交集應該是 [1, 3, 5] 或順序的變體
    expected = [1, 3, 5]  # 或者 [1, 5, 3] 等，取決於函數的實現
    
    # 由於順序可能不同，我們先排序再比較，或者轉換為集合再比較
    assert sorted(result) == sorted(expected)