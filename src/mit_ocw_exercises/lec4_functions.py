# src/mit_ocw_exercises/lec4_functions.py

from typing import Callable, Iterable, List

def iter_power(base: float, exp: int) -> float:
    """Compute base**exp using iteration; exp >= 0 integer."""
    if exp < 0:
        raise ValueError("exp must be non-negative")
    result = 1.0
    for _ in range(exp):
        result *= base
    return result

def recur_power(base: float, exp: int) -> float:
    """Compute base**exp using recursion; exp >= 0 integer."""
    if exp < 0:
        raise ValueError("exp must be non-negative")
    if exp == 0:
        return 1.0
    return base * recur_power(base, exp - 1)

def gcd_iter(a: int, b: int) -> int:
    """Greatest common divisor using Euclid's algorithm (iterative)."""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recur(a: int, b: int) -> int:
    """Greatest common divisor using recursion."""
    a, b = abs(a), abs(b)
    return a if b == 0 else gcd_recur(b, a % b)

def is_in(char: str, a_str: str) -> bool:
    """
    Return True iff single-character `char` is in sorted string `a_str`,
    using a recursive binary-search style (no `in` operator for the search).
    """
    if not a_str:
        return False
    mid = len(a_str) // 2
    if char == a_str[mid]:
        return True
    if char < a_str[mid]:
        return is_in(char, a_str[:mid])
    return is_in(char, a_str[mid+1:])

def apply_to_each(L: Iterable, f: Callable) -> List:
    """Return a new list where function `f` is applied to each element of `L`."""
    return [f(e) for e in L]

def eval_poly(coeffs: List[float], x: float) -> float:
    """
    Evaluate polynomial with coefficients [a0, a1, ..., an] meaning
    a0 + a1*x + ... + an*x^n using Horner's method.
    """
    result = 0.0
    for c in reversed(coeffs):
        result = result * x + c
    return result

def bisection_cuberoot_approx(x: float, epsilon: float) -> float:
    """
    Approximate cube root of nonnegative x within epsilon using bisection.
    Returns a float.
    """
    if x < 0:
        raise ValueError("x must be non-negative for this simple version")
    if x == 0:
        return 0.0
    low, high = (0.0, max(1.0, x))
    guess = (low + high) / 2.0
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
    return guess

# Optional tiny helpers that some test sets use (no side effects, safe to include):

def is_even(i: int) -> bool:
    """Return True if i is even, otherwise False."""
    return (i % 2) == 0

