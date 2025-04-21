def test_rev_list():
    L1 = [1, 2, 3, 4]
    rev_list(L1)
    assert L1 == [4, 3, 2, 1], "Test case 1 failed"

    L2 = [10]
    rev_list(L2)
    assert L2 == [10], "Test case 2 failed"

    L3 = []
    rev_list(L3)
    assert L3 == [], "Test case 3 failed"

    print("rev_list passed all test cases.")

test_rev_list()

