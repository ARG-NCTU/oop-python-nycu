def run_tests():
    # 測試 linear_search
    print("Testing linear_search...")
    assert linear_search([1, 2, 3], 2) == True
    assert linear_search([1, 2, 3], 4) == False
    assert linear_search([], 1) == False
    print("linear_search passed.")

    # 測試 search（假設 L 是排序過的 list）
    print("Testing search...")
    assert search([1, 3, 5, 7, 9], 5) == True
    assert search([1, 3, 5, 7, 9], 6) == False
    assert search([1, 2, 4], 3) == False  # 提早結束測試
    assert search([], 3) == False
    print("search passed.")

    # 測試 isSubset
    print("Testing isSubset...")
    assert isSubset([1, 2], [1, 2, 3]) == True
    assert isSubset([1, 4], [1, 2, 3]) == False
    assert isSubset([], [1, 2]) == True
    assert isSubset([1, 2], []) == False
    print("isSubset passed.")

    # 測試 intersect
    print("Testing intersect...")
    assert intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersect([1, 2, 2, 3], [2, 2, 3]) == [2, 3]
    assert intersect([], [1, 2]) == []
    assert intersect([1, 2], []) == []
    assert intersect([], []) == []
    print("intersect passed.")

    print("\nAll tests passed!")

# 呼叫測試函式
run_tests()

