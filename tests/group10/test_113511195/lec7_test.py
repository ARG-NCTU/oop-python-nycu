import add_path
import lec7_debug_except as lec7 # type: ignore
import pytest
import random
import math

def rev_list(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp

def test_rev_list():
    L = [1, 2, 3]
    rev_list(L)
    assert L == [3, 2, 1]


    L = ['q', 'w', 'e', 'r', 't', 'y']
    rev_list(L)
    assert L == ['y', 't', 'r', 'e', 'w', 'q']

    L = []
    rev_list(L)
    assert L == []

    L = [1]
    rev_list(L)
    assert L == [1]


def test_rev_list_generalize():
    for _ in range(100):
        length = random.randint(0, 100)
        tar = [random.randint(0, 1000) for _ in range(length)]
        expected = tar[::-1]
        rev_list(tar)
        assert tar == expected

    
def test_primes_list():
    assert lec7.primes_list(5) == [2, 3, 5]
    assert lec7.primes_list(10) == [2, 3, 5, 7]
    assert lec7.primes_list(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert lec7.primes_list(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def test_primes_list_generalize():
    known_primes_up_to_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for n in range(2, 101):
        expected = [p for p in known_primes_up_to_100 if p <= n]
        assert lec7.primes_list(n) == expected
    
def test_get_ratios():
    assert lec7.get_ratios([0, 0], [1, 2]) == [0, 0]
    assert lec7.get_ratios([1, 3, 5, 7], [1, 3, 5, 7]) == [1, 1, 1, 1]
    assert lec7.get_ratios([8, 8, 8, 8, 8], [2, 4, 8, 16, 32]) == [4, 2, 1, 0.5, 0.25]
    assert lec7.get_ratios([], []) == []
    assert lec7.get_ratios([-1, -2, -3], [1, 2, 3]) == [-1.0, -1.0, -1.0]
    result = lec7.get_ratios([1, 2, 3], [0, 0, 0])
    assert all(math.isnan(x) for x in result)

def rev_list(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    returns: nothing
    """
    for i in range(len(L)//2):
        j = len(L) - i - 1
        temp = L[i]
        L[i] = L[j]
        L[j] = temp

def test_avg():
    assert lec7.avg([1, 2, 3]) == 2

def test_get_status():
    stats = lec7.get_stats([[['s1'], [1, 2, 3]], [['s2'], [0]]])
    assert stats == [[['s1'], [1, 2, 3], 2.0], [['s2'], [0], 0.0]]