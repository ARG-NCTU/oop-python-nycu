import pytest
import random
import sys

# NOTE: Commented out local dependency to ensure script runs standalone.
# from add_path import add_path
# add_path()
# from lec11_complexity_part2 import bisect_search1, bisect_search2, genSubsets, genPerms

# ==============================================================================
# 1. Search Algorithms (Complexity Demo) 🔍
# ==============================================================================

def bisect_search1(L, e):
    """
    Binary search using List Slicing.
    Complexity: O(N) because slicing L[:half] copies the list.
    """
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)


def bisect_search2(L, e):
    """
    Binary search using Index Pointers.
    Complexity: O(log N) - No copying, just indices.
    """
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search
                return False
            return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    return bisect_search_helper(L, e, 0, len(L) - 1)

# ==============================================================================
# 2. Set Operations on Sorted Lists (Merge Logic) 🔗
# ==============================================================================

def union(L1, L2):
    """
    Returns a sorted list containing elements in either L1 or L2 (no duplicates).
    Assumes L1 and L2 are sorted.
    Complexity: O(len(L1) + len(L2))
    """
    res = []
    i, j = 0, 0
    
    # Helper to safely append unique elements
    def add_unique(val):
        if not res or res[-1] != val:
            res.append(val)

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            add_unique(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            add_unique(L2[j])
            j += 1
        else: # Equal: add one, advance both
            add_unique(L1[i])
            i += 1
            j += 1
            
    # Add remaining elements
    while i < len(L1):
        add_unique(L1[i])
        i += 1
    while j < len(L2):
        add_unique(L2[j])
        j += 1
        
    return res


def difference(L1, L2):
    """
    Returns a sorted list of elements in L1 but NOT in L2.
    Assumes L1 and L2 are sorted.
    Complexity: O(len(L1) + len(L2))
    """
    res = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            # Element is in L1 but not L2 (since L2[j] is already larger)
            res.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            # L2 is behind, catch up
            j += 1
        else: # Equal: element exists in both, so exclude it
            i += 1
            j += 1
            
    # Any remaining elements in L1 are definitely not in L2 (since L2 is exhausted)
    while i < len(L1):
        res.append(L1[i])
        i += 1
        
    return res

# ==============================================================================
# 3. Pytest Test Cases 🧪
# ==============================================================================

# --- Binary Search 1 Tests ---
def test_binary_search_found():
    L = list(range(100))
    e = 42
    assert bisect_search1(L, e) is True

def test_binary_search_not_found():
    L = list(range(100))
    e = 150
    assert bisect_search1(L, e) is False

@pytest.mark.parametrize("n", [10, 50, 100])
def test_bisect_search1_random_sizes(n):
    random.seed(123)
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert bisect_search1(L, e) is True

# --- Binary Search 2 Tests ---
def test_binary_search2_found():
    L = list(range(100))
    e = 42
    assert bisect_search2(L, e) is True

def test_binary_search2_not_found():
    L = list(range(100))
    e = 150
    assert bisect_search2(L, e) is False

@pytest.mark.parametrize("n", [10, 50, 100])
def test_bisect_search2_random_sizes(n):
    random.seed(123)
    L = sorted(random.sample(range(0, 1000), n))
    e = random.choice(L)
    assert bisect_search2(L, e) is True

# --- Set Operation Tests ---
def test_union():
    L1 = [1, 3, 5, 7]
    L2 = [2, 3, 6, 8]
    assert union(L1, L2) == [1, 2, 3, 5, 6, 7, 8]

def test_union_random():
    random.seed(42)
    L1 = sorted(random.sample(range(50), 10))
    L2 = sorted(random.sample(range(50), 10))
    result = union(L1, L2)
    # Check completeness and sorting using Python's set logic
    assert sorted(list(set(L1 + L2))) == result

def test_difference():  
    L1 = [1, 2, 3, 4, 5]
    L2 = [2, 4]
    assert difference(L1, L2) == [1, 3, 5]

def test_difference_random():
    random.seed(42)
    L1 = sorted(random.sample(range(50), 10))
    L2 = sorted(random.sample(range(50), 5))
    result = difference(L1, L2)
    expected = [x for x in L1 if x not in L2]
    assert expected == result

# ==============================================================================
# Main Execution
# ==============================================================================
if __name__ == "__main__":
    # Automatically run tests if script is executed directly
    sys.exit(pytest.main(["-v", __file__]))