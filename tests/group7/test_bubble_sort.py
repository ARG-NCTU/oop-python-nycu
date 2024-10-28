from sorting_111511282 import bubble_sort

def test_bubble_sort():
    test_cases = [
        ([], []),
        ([7], [7]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), 
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ]
    
    for i, (input_arr, expected_output) in enumerate(test_cases):
        sorted_arr = bubble_sort(input_arr[:])
        if sorted_arr == expected_output:
            print(f"Test case {i + 1}: Passed")
        else:
            print(f"Test case {i + 1}: Failed. Correct Ans = {expected_output}, Your Ans = {sorted_arr}")

test_bubble_sort()