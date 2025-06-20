# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:34 2016

@author: WELG
"""

def rev_list(L):
    """
    Input: L, a list
    Modifies L such that its elements are in reverse order
    Returns: nothing
    """
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp

def primes_list(n):
    """
    Input: n an integer > 1
    Returns: list of all the primes up to and including n
    """
    primes = [2]
    for j in range(3, n+1):
        is_div = False
        for p in primes:
            if j % p == 0:
                is_div = True
        if not is_div:
            primes.append(j)
    return primes

def get_ratios(L1, L2):
    """
    Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i]
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index] / L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios

def get_stats(class_list):
    """
    Input: class_list, a list of lists [[name, grades], ...]
    Returns: a list of [name, grades, average]
    """
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg(person[1])])
    return new_stats

def avg(grades):
    """
    Input: grades, a list of numbers
    Returns: average of grades
    Raises: AssertionError if grades is empty
    """
    assert len(grades) != 0, 'warning: no grades data'
    return sum(grades) / len(grades)
