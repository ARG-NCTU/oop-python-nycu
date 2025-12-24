# -*- coding: utf-8 -*-
"""
Examples:
- Reverse list
- Generate primes
- Exceptions
- Ratios with errors
- Stats with error handling
"""
from add_path import add_path
add_path()


########################################
# Reverse list
########################################

def rev_list(L):
    """
    Reverse a list in-place by swapping elements from both ends.
    
    Args:
        L: List to reverse (must be mutable)
    
    Returns:
        The reversed list (same object)
    
    Raises:
        TypeError: If L is not a list
    """
    if not isinstance(L, list):
        raise TypeError(f"Expected list, got {type(L).__name__}")
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
    return L


########################################
# Prime list
########################################

def primes_list(n):
    """
    Generate all prime numbers up to and including n using trial division.
    
    Args:
        n: Upper bound (int >= 0)
    
    Returns:
        List of all primes <= n (empty list if n < 2)
    
    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    if n < 2:
        return []

    primes = [2]

    for j in range(3, n + 1):
        is_divisible = False
        for p in primes:
            if j % p == 0:
                is_divisible = True
                break   # MUST break once divisible
        if not is_divisible:
            primes.append(j)

    return primes


########################################
# Ratios (Exceptions)
########################################

def get_ratios(L1, L2):
    """
    Calculate element-wise ratios of two equal-length lists.
    
    Args:
        L1: List of numbers (numerators)
        L2: List of numbers (denominators)
    
    Returns:
        List of ratios L1[i]/L2[i], with float('nan') for division by zero
    
    Raises:
        ValueError: If lists have unequal length or contain non-numeric types
    """
    if len(L1) != len(L2):
        raise ValueError(f"Lists must have equal length: {len(L1)} != {len(L2)}")
    
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i] / L2[i])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except TypeError as e:
            raise ValueError(f"get_ratios: non-numeric value at index {i}: {e}")
        except Exception as e:
            raise ValueError(f"get_ratios called with bad arg at index {i}: {e}")
    return ratios


########################################
# Stats + avg (with assert)
########################################

def avg(grades):
    """
    Calculate average of a list of grades.
    
    Args:
        grades: List of numeric grades
    
    Returns:
        Average (sum/count) as float
    
    Raises:
        AssertionError: If grades list is empty
    """
    assert len(grades) != 0, "warning: no grades data"
    return sum(grades) / len(grades)


def get_stats(class_list):
    """
    Generate statistics for a class list including student names, grades, and averages.
    
    Args:
        class_list: List in format [['first', 'last'], [grade1, grade2, ...]], ...
    
    Returns:
        List of [['first', 'last'], [grades], average] for each person
        (average is 0.0 if grade list is empty)
    
    Raises:
        ValueError: If class_list format is invalid
    """
    if not isinstance(class_list, list):
        raise ValueError(f"class_list must be a list, got {type(class_list).__name__}")
    
    new_stats = []
    for idx, person in enumerate(class_list):
        try:
            if not isinstance(person, list) or len(person) != 2:
                raise ValueError(f"Person entry at index {idx} must be [name_list, grade_list]")
            name = person[0]
            grades = person[1]
            if not isinstance(grades, (list, tuple)):
                raise ValueError(f"Grades at index {idx} must be a list or tuple")
            
            average = avg(grades) if grades else 0.0
        except AssertionError:
            # Handle empty grades
            average = 0.0
        except ValueError as e:
            # Re-raise ValueError with context
            raise ValueError(f"Error processing person {idx}: {e}")
        
        new_stats.append([name, grades, average])
    return new_stats


########################################
# Utility: Safe prime calculation
########################################

def safe_primes_list(n):
    """
    Safe wrapper around primes_list that handles invalid input gracefully.
    
    Args:
        n: Upper bound for prime calculation
    
    Returns:
        Tuple (success: bool, result: list or error message)
    """
    try:
        result = primes_list(n)
        return (True, result)
    except (TypeError, ValueError) as e:
        return (False, str(e))


########################################
# Utility: Safe statistics calculation
########################################

def safe_get_stats(class_list):
    """
    Safe wrapper around get_stats that handles errors gracefully.
    
    Args:
        class_list: Student data in required format
    
    Returns:
        Tuple (success: bool, result: stats list or error message)
    """
    try:
        result = get_stats(class_list)
        return (True, result)
    except (ValueError, TypeError) as e:
        return (False, str(e))