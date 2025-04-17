def test_get_stats():
    test_grades = [
        [['peter', 'parker'], [80.0, 70.0, 85.0]],
        [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
        [['captain', 'america'], [80.0, 70.0, 96.0]],
        [['deadpool'], []]
    ]

    expected_output = [
        ['peter', [80.0, 70.0, 85.0], 78.33333333333333],
        ['bruce', [100.0, 80.0, 74.0], 84.66666666666667],
        ['captain', [80.0, 70.0, 96.0], 82.0],
        ['deadpool', [], 0.0]
    ]

    assert get_stats(test_grades) == expected_output, "Test case failed"

    print("get_stats passed all test cases.")

test_get_stats()

