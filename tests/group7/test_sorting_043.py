import pytest
from sorting_111701043 import bubble_sort, insertion_sort, merge_sort
import numpy as np
import time

# Parametrize to test multiple algorithms
@pytest.mark.parametrize("algorithm", [bubble_sort, insertion_sort, merge_sort])
def test_sorting_algorithm(algorithm):
    # Dictionary of test cases
    test_cases = {
        "empty_list": [],
        "sorted_list": [3, 5, 6, 7, 22],
        "reverse_sorted_list": [45, 40, 33, 21, 10],
        "unsorted_list": [4, 2, 1, 8, 7, 6],
        "list_with_duplicates": [4, 7, 7, 8, 7, 6],
        "list_with_negatives": [4, -10, 1, -9, 7, 2],
        "single_element_list": [1],
        "all_same_elements": [5, 5, 5, 5, 5],
        "random_input": np.random.randint(0, 1000, size=500).tolist()
    }
    
    for name, data in test_cases.items():
        if name == "random_input":
            start_time = time.time()
            sorted_output = algorithm(data.copy())
            end_time = time.time()
            assert sorted_output == sorted(data)
            print(f"Execution time for {algorithm.__name__} with {name}: {end_time - start_time} seconds")
        else:
            assert algorithm(data.copy()) == sorted(data)
            print(f"Test passed for {algorithm.__name__} with {name}")

if __name__ == "__main__":
    pytest.main()
