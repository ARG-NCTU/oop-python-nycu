def run_tests():
    print("Testing bisect_search1...")
    sorted_list = list(range(0, 100))
    assert bisect_search1(sorted_list, 50) == True
    assert bisect_search1(sorted_list, 0) == True
    assert bisect_search1(sorted_list, 99) == True
    assert bisect_search1(sorted_list, 100) == False
    assert bisect_search1([], 5) == False
    print("bisect_search1 passed.")

    print("Testing bisect_search2...")
    assert bisect_search2(sorted_list, 50) == True
    assert bisect_search2(sorted_list, 0) == True
    assert bisect_search2(sorted_list, 99) == True
    assert bisect_search2(sorted_list, -1) == False
    assert bisect_search2([], 5) == False
    print("bisect_search2 passed.")

    print("Testing genSubsets...")
    assert genSubsets([]) == [[]]
    assert sorted(genSubsets([1])) == sorted([[], [1]])
    assert sorted(genSubsets([1, 2])) == sorted([[], [2], [1], [1, 2]])
    assert sorted(genSubsets([1, 2, 3])) == sorted([
        [],
        [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]
    ])
    print("genSubsets passed.")

    print("\nAll tests passed!")

# 呼叫測試函式
run_tests()

