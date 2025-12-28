# -*- coding: utf-8 -*-
"""
Modified on Thu Dec 25 2025
Original examples: Reverse list, Generate primes, Exceptions, Stats
"""

import math

# NOTE: Commented out local dependency to ensure script runs standalone.
# from add_path import add_path
# add_path()

# ==============================================================================
# 1. Reverse List (In-Place) 🔄
# ==============================================================================

def rev_list(L: list) -> list:
    """
    Modifies L in-place so elements are reversed.
    Complexity: O(N)
    """
    # Iterate only up to the middle point
    for i in range(len(L) // 2):
        j = len(L) - i - 1
        # Pythonic swap using tuple unpacking
        L[i], L[j] = L[j], L[i]
        
    return L


# ==============================================================================
# 2. Prime Generation (Optimized) 🔢
# ==============================================================================

def primes_list(n: int) -> list:
    """
    Returns list of primes up to n.
    Optimization: Checks divisibility only up to sqrt(number).
    """
    if n < 2:
        return []

    primes = [2]

    # Check only odd numbers starting from 3
    for j in range(3, n + 1, 2):
        is_divisible = False
        # Optimization: We only need to check factors up to sqrt(j)
        limit = int(math.isqrt(j))
        
        for p in primes:
            if p > limit:
                break
            if j % p == 0:
                is_divisible = True
                break
                
        if not is_divisible:
            primes.append(j)

    return primes


# ==============================================================================
# 3. Ratios with Exception Handling ⚠️
# ==============================================================================

def get_ratios(L1: list, L2: list) -> list:
    """
    Calculates L1[i] / L2[i]. 
    Returns a list of ratios, using NaN for division by zero.
    """
    ratios = []
    if len(L1) != len(L2):
        raise ValueError("Lists must be of equal length")

    for i in range(len(L1)):
        try:
            ratios.append(L1[i] / L2[i])
        except ZeroDivisionError:
            # Handle division by zero gracefully
            ratios.append(float('nan'))
        except TypeError:
            # Handle non-numeric types
            raise ValueError(f"get_ratios called with bad arg at index {i}")
            
    return ratios


# ==============================================================================
# 4. Statistics with Assertions 📊
# ==============================================================================

def avg(grades: list) -> float:
    """Returns the average of a list of grades."""
    # assert raises an AssertionError if the condition is False
    assert len(grades) != 0, "warning: no grades data"
    return sum(grades) / len(grades)


def get_stats(class_list: list) -> list:
    """
    Computes average grades for a list of students.
    
    Args:
        class_list: [ [['first','last'], [grade list]], ... ]
    
    Returns:
        [ ['first','last'], [grades], avg ]
    """
    new_stats = []
    
    for person in class_list:
        name = person[0]
        grades = person[1]
        
        try:
            average = avg(grades)
        except AssertionError:
            # Default to 0.0 if no grades exist
            average = 0.0
            print(f"  Warning: No grades for {name[0]} {name[1]}")
            
        new_stats.append([name, grades, average])
        
    return new_stats


# ==============================================================================
# Main Execution
# ==============================================================================

def main():
    print("=" * 60)
    print(f"{'💻 ALGORITHMS & EXCEPTIONS DEMO 📈':^60}")
    print("=" * 60)

    # --- 1. Reverse List ---
    print("\n## 1. Reverse List")
    print("-" * 40)
    
    my_list = [1, 2, 3, 4, 5]
    print(f"Original: {my_list}")
    rev_list(my_list)
    print(f"Reversed: {my_list}")
    
    # --- 2. Primes ---
    print("\n## 2. Generate Primes")
    print("-" * 40)
    
    limit = 50
    p_list = primes_list(limit)
    print(f"Primes up to {limit}:")
    print(f"{p_list}")

    # --- 3. Ratios (Error Handling) ---
    print("\n## 3. Ratios and Exceptions")
    print("-" * 40)
    
    numerators   = [10, 20, 30, 40]
    denominators = [ 2,  0,  5,  4]
    
    print(f"L1: {numerators}")
    print(f"L2: {denominators}")
    
    try:
        results = get_ratios(numerators, denominators)
        print(f"Ratios: {results}")
    except ValueError as e:
        print(f"Error: {e}")

    # --- 4. Statistics ---
    print("\n## 4. Student Stats (Assertions)")
    print("-" * 40)
    
    test_grades = [
        [['Peter', 'Parker'], [82, 77, 86]],
        [['Bruce', 'Wayne'],  [102, 92, 99]],  # Invalid grade to test robustness
        [['Clark', 'Kent'],   []],  # Empty list to trigger assertion
        [['Tony', 'Stark'],   [95, 100, 100, 90]]
    ]

    stats = get_stats(test_grades)
    
    print("\nFinal Report:")
    for student in stats:
        full_name = f"{student[0][0]} {student[0][1]}"
        avg_score = student[2]
        print(f"  {full_name:<15} | Avg: {avg_score:.2f}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()