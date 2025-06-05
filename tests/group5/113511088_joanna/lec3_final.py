# lec3_final_v2.py

def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0  # 也可以用 not n % 2 寫法


def factorial(n):
    """Compute factorial recursively. Raises error for negative input."""
    if n < 0:
        raise ValueError("Cannot compute factorial of negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_palindrome(s):
    """Check if string s is a palindrome."""
    reversed_s = s[::-1]
    return s == reversed_s


def find_max(L):
    """Return the maximum element in list L. Raise error if list is empty."""
    if len(L) == 0:
        raise ValueError("Empty list: no maximum exists.")
    return max(L)


def count_vowels(s):
    """Count number of vowels (a, e, i, o, u) in the string s (case-insensitive)."""
    vowels = "aeiou"
    return sum(1 for c in s.lower() if c in vowels)
