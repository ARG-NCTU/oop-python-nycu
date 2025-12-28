# -*- coding: utf-8 -*-
"""
lec6_recursion_dicts_113511088.py
Recursion + Dictionaries examples
"""

#####################################
# EXAMPLE: Towers of Hanoi
#####################################

def printMove(fr, to):
    """Print one move (used by Towers)."""
    print('move from ' + str(fr) + ' to ' + str(to))


def Towers(n, fr, to, spare):
    """Move n disks from fr to to using spare."""
    if n <= 0:
        raise ValueError("n must be >= 1")
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)


#####################################
# EXAMPLE: Fibonacci (0-based)
# fib(0)=1, fib(1)=1
#####################################

def fib(x):
    """assumes x an int >= 0; returns Fibonacci of x (0-based)."""
    if x < 0:
        raise ValueError("x must be >= 0")
    if x == 0 or x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)


#####################################
# EXAMPLE: Palindrome
#####################################

def is_palindrome(s):
    """Return True if s is a palindrome (ignoring case/non-letters)."""

    def to_chars(t):
        t = t.lower()
        ans = ''
        for c in t:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def is_pal(t):
        if len(t) <= 1:
            return True
        return (t[0] == t[-1]) and is_pal(t[1:-1])

    return is_pal(to_chars(s))


#####################################
# EXAMPLE: Dictionaries - word frequencies
#####################################

def lyrics_to_frequencies(lyrics):
    """lyrics: list[str] -> dict[str,int]"""
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


def most_common_words(freqs):
    """Return (list_of_words_with_max_freq, max_freq)."""
    if not freqs:
        raise ValueError("freqs cannot be empty")
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def words_often(freqs, minTimes):
    """
    Return list of tuples: [([most_common_words], freq), ...]
    This version does NOT mutate the original freqs.
    """
    if minTimes < 1:
        raise ValueError("minTimes must be >= 1")

    freqs_copy = freqs.copy()
    result = []

    while freqs_copy:
        words, best = most_common_words(freqs_copy)
        if best < minTimes:
            break
        result.append((words, best))
        for w in words:
            del freqs_copy[w]

    return result


#####################################
# EXAMPLE: Fibonacci with memoization
#####################################

def fib_efficient(n, d):
    """Memoized Fibonacci (0-based). d maps int->fib(int)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in d:
        return d[n]
    ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
    d[n] = ans
    return ans


def fib_mem(n):
    """Wrapper: memoized Fibonacci (0-based)."""
    d = {0: 1, 1: 1}
    return fib_efficient(n, d)


if __name__ == "__main__":
    # quick demo (optional)
    print("fib(10) =", fib(10))
    print("fib_mem(34) =", fib_mem(34))
    print(is_palindrome("Able was I, ere I saw Elba"))
    # Towers(3, "P1", "P2", "P3")
