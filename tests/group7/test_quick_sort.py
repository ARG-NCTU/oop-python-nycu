from sorting_111511282 import quick_sort

def test_quick_sort():
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), 
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ]
    
    for i, (input_arr, expected_output) in enumerate(test_cases):
        sorted_arr = quick_sort(input_arr[:], 0, len(input_arr) - 1, list(range(len(input_arr))))
        if sorted_arr == expected_output:
            print(f"Test case {i + 1}: Passed")
        else:
            print(f"Test case {i + 1}: Failed. Expected {expected_output}, but got {sorted_arr}")

test_quick_sort()