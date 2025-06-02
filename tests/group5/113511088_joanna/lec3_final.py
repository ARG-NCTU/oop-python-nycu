# lec3_final.py

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_palindrome(s):
    return s == s[::-1]

def find_max(L):
    if not L:
        raise ValueError("Empty list has no maximum.")
    return max(L)

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
