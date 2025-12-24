import pytest
import random

# NOTE: Commented out local dependency to ensure script runs standalone.
# from add_path import add_path
# add_path()
# from lec10_complexity_part1 import linear_search, search, isSubset, intersect

# ==============================================================================
# 1. Algorithm Implementations (Complexity Demo) 🧠
# ==============================================================================

def linear_search(L, e):
    """
    Returns True if e is in L, False otherwise.
    Complexity: O(N) - Linear time
    """
    for i in L:
        if i == e:
            return True
    return False


def search(L, e):
    """
    Assumes L is a list sorted in ascending order.
    Returns True if e is in L, False otherwise.
    Complexity: O(log N) - Logarithmic time (Binary Search)
    """
    def bsearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            return bsearch(L, e, low, mid - 1)
        else:
            return bsearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    return bsearch(L, e, 0, len(L) - 1)


def isSubset(L1, L2):
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


def intersect(L1, L2):
    """
    Returns a list without duplicates that are in both L1 and L2.
    Complexity: O(N^2) due to "e in result" check inside loop
    """
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                if e1 not in tmp:  # Avoid duplicates
                    tmp.append(e1)
                break
    return sorted(tmp) # Sorting to ensure consistent test results


# ==============================================================================
# 2. Pytest Test Cases 🧪
# ==============================================================================

def test_linear_search_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    e = 5
    assert linear_search(L, e) is True

def test_linear_search_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    e = 7
    assert linear_search(L, e) is False

def test_search_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    e = 9
    assert search(L, e) is True
 
def test_search_not_found():
    L = [1, 3, 4, 5, 9, 18, 27]
    e = 10
    assert search(L, e) is False

def test_isSubset_true():
    L1 = [1, 3, 5]
    L2 = [1, 2, 3, 4, 5]
    assert isSubset(L1, L2) is True 

def test_isSubset_false():
    L1 = [1, 6]
    L2 = [1, 2, 3, 4, 5]
    assert isSubset(L1, L2) is False

def test_intersect():
    L1 = [1, 2, 3, 4, 5]
    L2 = [4, 5, 6, 7, 8]
    # intersect returns sorted list of common elements
    assert intersect(L1, L2) == [4, 5]

def test_intersect_no_common():
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    assert intersect(L1, L2) == []

def test_intersect_with_duplicates():
    L1 = [1, 2, 2, 3, 4]
    L2 = [2, 2, 4, 4, 5]
    # Should return unique common elements
    assert intersect(L1, L2) == [2, 4]
    
    
# Parametrized test to run same test logic with different inputs
@pytest.mark.parametrize("n", [10, 50, 100])
def test_search_random_sizes(n):
    random.seed(123)
    # Generate a sorted list of unique random numbers
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert search(L, e) is True

# ==============================================================================
# Main Execution
# ==============================================================================
if __name__ == "__main__":
    # This allows running the script directly: `python script_name.py`
    # It will invoke pytest to run the tests defined above.
    import sys
    sys.exit(pytest.main(["-v", __file__]))