# -*- coding: utf-8 -*-
"""
Lecture 10: Complexity Analysis - Part 1

Examples demonstrating:
- Linear search vs optimized search
- Subset checking algorithms
- Set intersection operations
- Time complexity analysis (O(n), O(n^2), etc.)

@author: ericgrimson
"""
from add_path import add_path
add_path()


def linear_search(L, e):
    """Simple linear search - checks entire list regardless of found element.
    
    Time complexity: O(n) - always checks all elements
    Space complexity: O(1)
    
    Args:
        L: List to search
        e: Element to find
    
    Returns:
        True if element found, False otherwise
    """
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


testList = [1, 3, 4, 5, 9, 18, 27]


def search(L, e):
    """Optimized search for sorted list - returns early when possible.
    
    Time complexity: O(n) worst case, O(1) best case
    Space complexity: O(1)
    
    IMPORTANT: List must be sorted for early termination to work correctly!
    
    Args:
        L: Sorted list to search
        e: Element to find
    
    Returns:
        True if element found, False otherwise
    
    Raises:
        TypeError: If L is not a list
    """
    if not isinstance(L, list):
        raise TypeError(f"Expected list, got {type(L).__name__}")
    
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:     # Important: list must be sorted for early stop
            return False
    return False


def isSubset(L1, L2):
    """Check if all elements of L1 are contained in L2.
    
    Time complexity: O(n*m) where n=len(L1), m=len(L2)
    Space complexity: O(1)
    
    Algorithm:
    - For each element in L1, search L2 for a match
    - If any element of L1 not found in L2, return False
    - If all elements found, return True
    
    Args:
        L1: First list (potential subset)
        L2: Second list (potential superset)
    
    Returns:
        True if L1 is a subset of L2, False otherwise
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


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]


# ===== Optimized Versions =====

def isSubset_optimized(L1, L2):
    """Optimized subset check using set conversion.
    
    Time complexity: O(n + m) average case
    Space complexity: O(m) for the set
    
    Much faster for large lists!
    
    Args:
        L1: First list
        L2: Second list
    
    Returns:
        True if L1 is a subset of L2, False otherwise
    """
    return set(L1).issubset(set(L2))


def intersect_optimized(L1, L2):
    """Optimized intersection using set operations.
    
    Time complexity: O(n + m) average case
    Space complexity: O(min(n, m)) for result
    
    Much faster than nested loop approach!
    
    Args:
        L1: First list
        L2: Second list
    
    Returns:
        List of common elements (without duplicates)
    """
    return list(set(L1).intersection(set(L2)))


def intersect(L1, L2):
    """Find the intersection of two lists (elements present in both).
    
    Time complexity: O(n*m + k*len(res)) where n=len(L1), m=len(L2), k=len(intersection)
    Space complexity: O(min(n, m)) for result list
    
    Algorithm:
    1. Find all matching pairs between L1 and L2 (O(n*m))
    2. Remove duplicates from result (O(k^2) in worst case)
    
    Args:
        L1: First list
        L2: Second list
    
    Returns:
        List of elements present in both L1 and L2 (without duplicates)
    """
    tmp = []
    # Find all matches (including duplicates)
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)

    # Remove duplicates
    res = []
    for e in tmp:
        if e not in res:
            res.append(e)

    return res
