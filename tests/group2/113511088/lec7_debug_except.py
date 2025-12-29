# -*- coding: utf-8 -*-
"""
Lab7: Debugging + Exceptions + Lists
"""

from math import nan


def rev_list(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing (None)
    """
    for i in range(len(L) // 2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp


def primes_list(n):
    """
    input: n an integer >= 2
    returns: list of all primes up to and including n
    """
    if not isinstance(n, int) or n < 2:
        raise ValueError("n must be an int >= 2")

    primes = [2]
    for j in range(3, n + 1):
        is_div = False
        for p in primes:
            if j % p == 0:
                is_div = True
                break
        if not is_div:
            primes.append(j)
    return primes


def get_ratios(L1, L2):
    """
    Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i]
    - if division by zero -> append nan
    - if bad args -> raise ValueError
    """
    if not isinstance(L1, list) or not isinstance(L2, list) or len(L1) != len(L2):
        raise ValueError("get_ratios called with bad arg")

    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i] / L2[i])
        except ZeroDivisionError:
            ratios.append(nan)
        except Exception:
            raise ValueError("get_ratios called with bad arg")
    return ratios


def avg(grades):
    """
    grades: list of numbers
    returns average; if empty list -> 0.0
    """
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return 0.0


def get_stats(class_list):
    """
    class_list: list of [name, grades]
      where name could be list like ['peter','parker'], grades is list of numbers
    returns: list of [name, grades, avg(grades)]
    """
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg(person[1])])
    return new_stats


if __name__ == "__main__":
    # Demo (手動跑才會執行，pytest import 不會跑)
    L = [1, 2, 3, 4]
    rev_list(L)
    print("reversed:", L)

    print("primes up to 15:", primes_list(15))
    print("ratios:", get_ratios([1, 4], [2, 0]))
