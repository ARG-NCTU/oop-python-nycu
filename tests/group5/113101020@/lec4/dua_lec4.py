#!/usr/bin/env python3

"""
核心程式：定義各範例函式，不包含測試
"""

def is_even_with_return(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    return i % 2 == 0

def is_even_without_return(i):
    """
    Input: i, a positive int
    Does not return anything
    """
    print('without return')
    _ = i % 2

def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    return i % 2 == 0

def bisection_cuberoot_approx(x, epsilon):
    """
    Input: x, an integer
    Uses bisection to approximate the cube root of x to within epsilon
    Returns: a float approximating the cube root of x
    """
    low, high = 0.0, x
    guess = (low + high) / 2.0
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
    return guess

def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

def f_factory():
    def x(a, b):
        return a + b
    return x

