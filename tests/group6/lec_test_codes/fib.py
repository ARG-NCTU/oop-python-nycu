import sys
import pytest

def fib (n):

    if n == 0 or n ==1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fast_fib (n, memo = {}):
    if n == 0 or n ==1 :
        return 1     
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
        return memo[n]
    
def test_fib():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8
    assert fib(6) == 13
    assert fib(7) == 21

def test_fast_fib():
    assert fast_fib(0) == 1
    assert fast_fib(1) == 1
    assert fast_fib(3) == 3
    assert fast_fib(4) == 5
    assert fast_fib(5) == 8
    assert fast_fib(6) == 13
    assert fast_fib(7) == 21

def main ():
    for i in range(36):
        print("fib(" + str(i) + ") =" + str(fib(i)))
    for i in range(36):
        print("fib(" + str(i) + ") =" + str(fast_fib(i)))

if __name__ == "__main__":
    main()