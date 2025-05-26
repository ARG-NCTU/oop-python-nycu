def is_even_with_return(i):
    print('with return')
    return i % 2 == 0

def is_even_without_return(i):
    print('without return')
    remainder = i % 2
    # Does not return anything

def is_even(i):
    return i % 2 == 0

def bisection_cuberoot_approx(x, epsilon):
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

def func_a():
    return "inside func_a"

def func_b(y):
    return y

def func_c(z):
    return z()

def f_returning_function():
    def x(a, b):
        return a + b
    return x

def scope_demo_f(y):
    x = 1
    x += 1
    return x

def scope_demo_g(y, x):
    return (x, x + 1)

def scope_demo_h(y, x):
    # This simulates what would raise an error without `global`
    return "no operation"

def nested_scope_g(x):
    def h():
        nonlocal_x = 'abc'
        return nonlocal_x
    x = x + 1
    h()
    return x

def complicated_scope_f(x):
    x = x + 1
    return x

def complicated_scope_g(x):
    def h(x):
        return x + 1
    x = x + 1
    return h(x)
