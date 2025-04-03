# Part 1: Fibonacci
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def test_fib_basic():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(5) == 8
