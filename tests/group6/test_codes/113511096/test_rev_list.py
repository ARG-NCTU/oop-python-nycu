def rev_list(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    # Iterate only over the first half to avoid reversing it back to original
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp

# --- Pytest Functions ---
# Note: Function name must start with 'test_'
def test_rev_list():
    # Test Case 1: Odd number of elements
    L1 = [11, 2, 35, 4, 5]
    rev_list(L1)
    assert L1 == [5, 4, 35, 2, 11]
    
    # Test Case 2: Strings
    L2 = ['p', 'b', 'c']
    rev_list(L2)
    assert L2 == ['c', 'b', 'p']
    
    # Test Case 3: Empty list
    L3 = []
    rev_list(L3)
    assert L3 == []

    # Test Case 4: Even number of elements (from your example)
    L4 = [6, 24, 3, 4]
    rev_list(L4)
    assert L4 == [4, 3, 24, 6]