def test_get_ratios():
    assert get_ratios([1, 4], [2, 4]) == [0.5, 1.0], "Test case 1 failed"
    assert get_ratios([10, 20], [5, 4]) == [2.0, 5.0], "Test case 2 failed"
    assert get_ratios([3, 6], [0, 2]) == [float('nan'), 3.0], "Test case 3 failed"

    try:
        get_ratios([1, 2], [3])  # L1 和 L2 長度不一致，應該拋出錯誤
        print("Test case 4 failed")  # 如果沒有拋出錯誤，則測試失敗
    except ValueError:
        print("Test case 4 passed")

    print("get_ratios passed all test cases.")

test_get_ratios()

