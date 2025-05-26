#!/usr/bin/env python3
# 範例程式集合：講解 print vs return、重複任務函式、高階函式、作用域

def is_even_with_return(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

print("=== Example: print vs return ===")
is_even_with_return(3)
print(is_even_with_return(3))

def is_even_without_return(i):
    """
    Input: i, a positive int
    Does not return anything
    """
    print('without return')
    remainder = i % 2

is_even_without_return(3)
print(is_even_without_return(3))

def is_even(i):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0

print("All numbers between 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")

print("\n=== Example: bisection cube root approximation ===")
def bisection_cuberoot_approx(x, epsilon):
    """
    Input: x, an integer
    Uses bisection to approximate the cube root of x to within epsilon
    Returns: a float approximating the cube root of x
    """
    low = 0.0
    high = x
    guess = (high + low) / 2.0
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
    return guess

x = 1
while x <= 10000:
    approx = bisection_cuberoot_approx(x, 0.01)
    print(f"{approx} is close to cube root of {x}")
    x *= 10

print("\n=== Example: functions as arguments ===")
def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5 + func_b(2))
print(func_c(func_a))

print("\n=== Example: returning function objects ===")
def f():
    def x(a, b):
        return a + b
    return x

val = f()(3, 4)
print(val)

print("\n=== Example: accessing variables outside scope ===")
def f1(y):
    x = 1
    x += 1
    print(x)
x = 5
f1(x)
print(x)

def g1(y):
    print(x)
    print(x + 1)
x = 5
g1(x)
print(x)

def h1(y):
    pass
    # x += 1  # would raise UnboundLocalError without global declaration
x = 5
h1(x)
print(x)

print("\n=== Example: nested scope from slides ===")
def g2(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g2(x): x =', x)
    h()
    return x

x = 3
z = g2(x)
print(z)

print("\n=== Example: complicated scope ===")
def f2(x):
    x = x + 1
    print('in f2(x): x =', x)
    return x

x = 3
z = f2(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

def g3(x):
    def h(x):
        x = x + 1
        print("in h(x): x =", x)
    x = x + 1
    print('in g3(x): x =', x)
    h(x)
    return x

x = 3
z = g3(x)
print('in main program scope: x =', x)
print('in main program scope: z =', z)

