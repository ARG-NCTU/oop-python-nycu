# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:52:34 2016
@author: WELG
"""

def printMove(fr, to):
    """Return a formatted move string"""
    return f'move from {fr} to {to}'


def Towers(n, fr, to, spare):
    """Return list of moves to solve Towers of Hanoi for n disks"""
    moves = []
    if n == 1:
        moves.append(printMove(fr, to))
    else:
        moves += Towers(n-1, fr, spare, to)
        moves += Towers(1, fr, to, spare)
        moves += Towers(n-1, spare, to, fr)
    return moves


def fib(x):
    """Assumes x is an int >= 0; returns Fibonacci number F(x) with F(0)=F(1)=1"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def is_palindrome(s):
    """Returns True if s is a palindrome (ignoring non-letters and case)"""
    def to_chars(s):
        s = s.lower()
        return ''.join(c for c in s if c.isalpha())
    def is_pal(st):
        if len(st) <= 1:
            return True
        return st[0] == st[-1] and is_pal(st[1:-1])
    return is_pal(to_chars(s))


def lyrics_to_frequencies(lyrics):
    """Count frequencies of words in a sequence of lyrics"""
    freqs = {}
    for word in lyrics:
        freqs[word] = freqs.get(word, 0) + 1
    return freqs


def most_common_words(freqs):
    """Return (list_of_words_with_max_freq, max_freq)"""
    best = max(freqs.values())
    words = [k for k, v in freqs.items() if v == best]
    return (words, best)


def words_often(freqs, minTimes):
    """Return list of (words, count) pairs for frequencies >= minTimes, in descending order"""
    result = []
    freqs = freqs.copy()
    while True:
        words, count = most_common_words(freqs)
        if count >= minTimes:
            result.append((words, count))
            for w in words:
                del freqs[w]
        else:
            break
    return result


def fib_efficient(n, d=None):
    """Efficient Fibonacci using memoization with F(0)=F(1)=1"""
    if d is None:
        d = {0: 1, 1: 1}
    if n in d:
        return d[n]
    d[n] = fib_efficient(n-1, d) + fib_efficient(n-2, d)
    return d[n]