# lec3_final.py

def is_even(n):
    return not n % 2  # True if n is divisible by 2

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0:
        return 1  # 0! is defined as 1
    return n * factorial(n - 1)

def is_palindrome(s):
    return s == s[::-1]

def find_max(L):
    if not L:
        raise ValueError("Cannot find max of empty list.")
    return max(L)

def count_vowels(s):
    # Count number of vowels in the string (case-insensitive)
    return sum(1 for c in s.lower() if c in "aeiou")
