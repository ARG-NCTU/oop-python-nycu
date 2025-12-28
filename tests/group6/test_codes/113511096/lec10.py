import pytest
import random
from typing import List, Any

# ==============================================================================
# 1. Algorithm Implementations (Complexity Demo) 🧠
# ==============================================================================

def linear_search(L: List[Any], e: Any) -> bool:
    """
    Returns True if e is in L, False otherwise.
    Complexity: O(N) - Linear time
    """
    for i in L:
        if i == e:
            return True
    return False


def search(L: List[int], e: int) -> bool:
    """
    Assumes L is a list sorted in ascending order.
    Returns True if e is in L, False otherwise.
    Complexity: O(log N) - Logarithmic time (Binary Search)
    """
    

    def bsearch(L, e, low, high):
        # Base case: search space is exhausted
        if low > high:
            return False
        
        mid = (low + high) // 2
        
        if L[mid] == e:
            return True
        elif L[mid] > e:
            # Search lower half
            return bsearch(L, e, low, mid - 1)
        else:
            # Search upper half
            return bsearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
        
    return bsearch(L, e, 0, len(L) - 1)


def isSubset(L1: List[Any], L2: List[Any]) -> bool:
    """
    Returns True if every element in L1 is also in L2.
    Complexity: O(len(L1) * len(L2)) -> O(N^2) worst case
    """
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


def intersect(L1: List[Any], L2: List[Any]) -> List[Any]:
    """
    Returns a list of elements common to both L1 and L2 without duplicates.
    
    Complexity Analysis:
    - Outer loops: O(len(L1) * len(L2))
    - 'not in tmp' check: O(len(tmp))
    - Total Worst Case: O(N^3) (though typically faster in practice)
    """
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                if e1 not in tmp:  # Avoid duplicates
                    tmp.append(e1)
                break
    return sorted(tmp) 


# ==============================================================================
# 2. Pytest Test Cases 🧪
# ==============================================================================

# --- Linear Search Tests ---
def test_linear_search_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert linear_search(L, 5) is True

def test_linear_search_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert linear_search(L, 7) is False

# --- Binary Search Tests ---
def test_search_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert search(L, 9) is True
 
def test_search_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    assert search(L, 10) is False

def test_search_empty():
    """Test searching in an empty list."""
    L = []
    assert search(L, 1) is False

def test_search_boundaries():
    """Test searching for the first and last elements."""
    L = [1, 2, 3, 4, 5]
    assert search(L, 1) is True
    assert search(L, 5) is True

# --- Subset Tests ---
def test_isSubset_true():
    L1 = [1, 3, 5]
    L2 = [1, 2, 3, 4, 5]
    assert isSubset(L1, L2) is True 

def test_isSubset_false():
    L1 = [1, 6]
    L2 = [1, 2, 3, 4, 5]
    assert isSubset(L1, L2) is False

# --- Intersect Tests ---
def test_intersect():
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 5, 6, 7, 8]
    assert intersect(L1, L2) == [4, 5]

def test_intersect_no_common():
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    assert intersect(L1, L2) == []

def test_intersect_with_duplicates():
    L1 = [1, 2, 2, 3, 4]
    L2 = [2, 2, 4, 4, 5]
    assert intersect(L1, L2) == [2, 4]
    
# --- Parametrized Random Tests ---
@pytest.mark.parametrize("n", [10, 50, 100])
def test_search_random_sizes(n):
    """Test binary search with random sorted lists of various sizes."""
    random.seed(123)
    # Generate a sorted list of unique random numbers
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert search(L, e) is True

    # Test for an element NOT in the list
    non_existent = 1001
    assert search(L, non_existent) is False

# ==============================================================================
# Main Execution
# ==============================================================================
if __name__ == "__main__":
    import sys
    sys.exit(pytest.main(["-v", __file__]))