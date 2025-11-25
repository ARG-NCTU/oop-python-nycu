# -*- coding: utf-8 -*-
"""
Examples:
- Reverse list
- Generate primes
- Exceptions
- Ratios with errors
- Stats with error handling
"""

########################################
# Reverse list
########################################

def rev_list(L):
    """
    Modifies L in-place so elements are reversed.
    """
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
    input: n > 1
    returns list of primes up to n
    """
    if n < 2:
        return []

    primes = [2]

    


########################################
# Ratios (Exceptions)
########################################

def get_ratios(L1, L2):
    """ L1 and L2 are lists of numbers, equal length """
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i] / L2[i])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except Exception:
            raise ValueError("get_ratios called with bad arg")
    return ratios


########################################
# Stats + avg (with assert)
########################################

def avg(grades):
    assert len(grades) != 0, "warning: no grades data"
    return sum(grades) / len(grades)


def get_stats(class_list):
    """
    class_list format:
    [
      [['first','last'], [grade list]],
      ...
    ]
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
            average = 0.0
        new_stats.append([name, grades, average])
    return new_stats
