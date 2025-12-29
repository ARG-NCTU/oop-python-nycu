def selection_sort(L):
    suffixSt = 0
    complexity = 0  # To track the number of comparisons
    while suffixSt != len(L):
        # The inner loop finds the minimum and swaps it to the current suffixSt position
        for i in range(suffixSt, len(L)):
            complexity += 1
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

    return L, complexity

# --- Pytest Functions ---

def test_selection_sort():
    """Validates sorting logic and O(n^2) complexity"""
    lst = [4, 2, 2, 22, 61]
    # Complexity for n=5: 5+4+3+2+1 = 15
    sorted_lst, complexity = selection_sort(lst)
    
    assert sorted_lst == [2, 2, 4, 22, 61]
    assert complexity == 15

def test_selection_sort_empty():
    """Validates behavior with an empty list"""
    sorted_lst, complexity = selection_sort([])
    assert sorted_lst == []
    assert complexity == 0