# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:34 2016

@author: WELG
"""

def printMove(fr, to):
    """
    Print a move instruction for Towers of Hanoi.
    Args:
        fr (str): Source peg.
        to (str): Destination peg.
    """
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    """
    Solve Towers of Hanoi for n disks.
    Args:
        n (int): Number of disks.
        fr (str): Source peg.
        to (str): Destination peg.
        spare (str): Spare peg.
    """
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

def fib(x):
    """
    Assumes x an int >= 0
    Returns Fibonacci of x
    Args:
        x (int): Non-negative integer.
    Returns:
        int: Fibonacci number.
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def is_palindrome(s):
    """
    Check if a string is a palindrome, ignoring non-letters and case.
    Args:
        s (str): Input string.
    Returns:
        bool: True if palindrome, False otherwise.
    """
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))

def lyrics_to_frequencies(lyrics):
    """
    Count frequency of words in a list.
    Args:
        lyrics (list): List of words.
    Returns:
        dict: Word frequency dictionary.
    """
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):
    """
    Find words with the highest frequency.
    Args:
        freqs (dict): Word frequency dictionary.
    Returns:
        tuple: (list of most frequent words, frequency)
    """
    values = freqs.values()
    best = max(freqs.values()) if freqs else 0
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    """
    Find words appearing at least minTimes.
    Args:
        freqs (dict): Word frequency dictionary.
        minTimes (int): Minimum frequency threshold.
    Returns:
        list: List of (words, frequency) tuples.
    """
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

def fib_mem(n):
    """
    Compute the nth Fibonacci number using recursion.
    Args:
        n (int): Non-negative integer.
    Returns:
        int: nth Fibonacci number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib_mem(n-1) + fib_mem(n-2)

def fib_efficient(n, d=None):
    """
    Compute the nth Fibonacci number using memoization.
    Args:
        n (int): Non-negative integer.
        d (dict): Memoization dictionary (default None).
    Returns:
        int: nth Fibonacci number.
    """
    if d is None:
        d = {0: 1, 1: 1}
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
