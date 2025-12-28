# -*- coding: utf-8 -*-
"""
Lecture 11: Complexity Analysis - Part 2

Examples demonstrating:
- Binary search (bisection) with two approaches
- Generating all subsets (power set)
- Generating all permutations
- Time/space complexity analysis of recursive algorithms

Key concepts:
- Divide and conquer algorithms
- Exponential time complexity (2^n for subsets, n! for permutations)
- Recursive algorithm analysis

@author: ericgrimson
"""
from add_path import add_path
add_path()


def bisect_search1(L, e):
    """Binary search using list slicing (simpler but less efficient).
    
    Time complexity: O(log n) comparisons, but O(n log n) due to list slicing
    Space complexity: O(log n) for recursion stack + O(n log n) for slices
    
    IMPORTANT: List must be sorted!
    
    Args:
        L: Sorted list to search
        e: Element to find
    
    Returns:
        True if element found, False otherwise
    """
    print('low: ' + str(L[0]) + '; high: ' + str(L[-1]))
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)

def bisect_search2(L, e):
    """Binary search using indices (more efficient than list slicing).
    
    Time complexity: O(log n) - optimal for comparison-based search
    Space complexity: O(log n) for recursion stack only
    
    IMPORTANT: List must be sorted!
    
    Advantages over bisect_search1:
    - No list slicing overhead (O(n) per slice)
    - More efficient space usage
    
    Args:
        L: Sorted list to search
        e: Element to find
    
    Returns:
        True if element found, False otherwise
    """
    def bisect_search_helper(L, e, low, high):
        """Helper function using index-based recursion.
        
        Args:
            L: List to search
            e: Element to find
            low: Lower bound index
            high: Upper bound index
        
        Returns:
            True if element found in range [low, high], False otherwise
        """
        print('low: ' + str(low) + '; high: ' + str(high))  #added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

testList = []
for i in range(100):
    testList.append(i)

print(bisect_search1(testList, 76))
print(bisect_search2(testList, 76))


# ===== Test Functions =====

def test_binary_search():
    """Test both binary search implementations."""
    test_list = list(range(1000))
    
    # Test cases: element at start, middle, end, not found
    test_cases = [0, 500, 999, 1000]
    
    print("\n--- Binary Search Tests ---")
    for target in test_cases:
        result1 = bisect_search1(test_list, target)
        result2 = bisect_search2(test_list, target)
        expected = target in test_list
        assert result1 == result2 == expected, f"Mismatch for {target}"
    print("All binary search tests passed!")


def count_subsets(n):
    """Calculate number of subsets for a list of size n.
    
    Number of subsets = 2^n
    
    Args:
        n: Size of list
    
    Returns:
        Number of subsets
    """
    return 2 ** n


def count_perms(n):
    """Calculate number of permutations for a list of size n.
    
    Number of permutations = n!
    
    Args:
        n: Size of list
    
    Returns:
        Number of permutations (factorial)
    """
    if n <= 1:
        return 1
    return n * count_perms(n - 1)


# Demonstration of subset and permutation generation is performed
# after the function definitions below so the functions are defined
# before they are invoked (avoids NameError during import/test collection).



def genSubsets(L):
    """Generate all subsets (power set) of list L using recursion.
    
    Time complexity: O(2^n) - there are 2^n subsets
    Space complexity: O(n * 2^n) for storing all subsets
    
    Algorithm:
    1. Get all subsets of L without last element (recursive)
    2. Create new subsets by adding last element to each subset
    3. Return union of original subsets and new subsets with last element
    
    Example:
        genSubsets([1, 2]) -> [[], [1], [2], [1, 2]]
    
    Args:
        L: List to generate subsets from
    
    Returns:
        List of all subsets (each subset is also a list)
    """
    res = []
    if len(L) == 0:
        return [[]] #list of empty list
    
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element
    
    return smaller+new  # combine those with last element and those without
def genPerms(L):
    """Generate all permutations of list L using recursion.
    
    時間複雜度 (Time complexity): O(n!) - there are n! permutations
    空間複雜度 (Space complexity): O(n * n!) for storing all permutations
    
    Algorithm:
    1. For each element in L:
       - Extract it as 'first'
       - Recursively generate permutations of remaining elements
       - Prepend 'first' to each permutation
    2. Return all generated permutations
    
    Example:
        genPerms([1, 2]) -> [[1, 2], [2, 1]]
        genPerms([1, 2, 3]) -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
    Args:
        L: List to generate permutations from
    
    Returns:
        List of all permutations (each permutation is also a list)
    """
    if len(L) == 0:
        return [[]]
    if len(L) == 1:
        return [L[:]]  # Return a copy

    res = []
    for i in range(len(L)):
        first = L[i]
        rest = L[:i] + L[i+1:]
        for p in genPerms(rest):
            res.append([first] + p)
    return res


testSet = [1,2,3,4]
print(genSubsets(testSet))
