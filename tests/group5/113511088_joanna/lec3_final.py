# lec3_final_v3.py

from typing import List

def is_even(n: int) -> bool:
    """Return True if n is an even number."""
    return n % 2 == 0


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Cannot compute factorial of negative number.")
    return 1 if n == 0 else n * factorial(n - 1)


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    return s == s[::-1]


def find_max(numbers: List[int]) -> int:
    """Return the maximum value from a non-empty list of integers."""
    if not numbers:
        raise ValueError("Empty list provided.")
    return max(numbers)


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string, case-insensitive."""
    vowels = set("aeiou")
    return sum(1 for char in s.lower() if char in vowels)


# Optional: For quick manual test runs
if __name__ == "__main__":
    print("is_even(10):", is_even(10))
    print("factorial(4):", factorial(4))
    print("is_palindrome('madam'):", is_palindrome("madam"))
    print("find_max([1, 2, 9, 4]):", find_max([1, 2, 9, 4]))
    print("count_vowels('HELLO ai!'):", count_vowels("HELLO ai!"))
