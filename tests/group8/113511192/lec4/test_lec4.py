import math

def is_even_with_return(i):
    print('with return')
    remainder = i % 2
    return remainder == 0

def is_even_without_return(i):
    print('without return')
    remainder = i % 2  # no return

def is_even(i):
    remainder = i % 2
    return remainder == 0

def bisection_cuberoot_approx(x, epsilon):
    low = 0.0
    high = x
    guess = (high + low)/2.0
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    return guess

def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

def f_return_function():
    def x(a, b):
        return a + b
    return x

def scope_f(y):
    x = 1
    x += 1
    print(x)

def scope_g(y):
    print(x)
    print(x + 1)

def scope_h(y):
    pass  # x += 1 would raise UnboundLocalError

def g_scope(x):
    def h():
        nonlocal x
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

def complicated_f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

def complicated_g(x):
    def h(x):
        x = x + 1
        print("in h(x): x =", x)
    x = x + 1
    print('in g(x): x =', x)
    h(x)
    return x


# Tests start here

def test_is_even_with_return(capfd):
    result = is_even_with_return(4)
    out, _ = capfd.readouterr()
    assert 'with return' in out
    assert result is True

    result = is_even_with_return(3)
    out, _ = capfd.readouterr()
    assert result is False

def test_is_even_without_return(capfd):
    result = is_even_without_return(4)
    out, _ = capfd.readouterr()
    assert 'without return' in out
    assert result is None  # since there's no return

def test_is_even():
    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(0) is True

def test_bisection_cuberoot_approx():
    x = 8
    epsilon = 0.01
    approx = bisection_cuberoot_approx(x, epsilon)
    assert abs(approx**3 - x) < epsilon

    x = 27
    approx = bisection_cuberoot_approx(x, epsilon)
    assert abs(approx**3 - x) < epsilon

def test_func_c_calls_func_a(capfd):
    result = func_c(func_a)
    out, _ = capfd.readouterr()
    assert 'inside func_c' in out
    assert 'inside func_a' in out
    assert result is None

def test_f_return_function():
    add = f_return_function()
    assert callable(add)
    assert add(3, 4) == 7

def test_scope_f(capfd):
    scope_f(5)
    out, _ = capfd.readouterr()
    assert '2' in out

def test_scope_g(capfd):
    global x
    x = 5
    scope_g(10)
    out, _ = capfd.readouterr()
    assert '5' in out
    assert '6' in out

def test_complicated_scope(capfd):
    global x
    x = 3
    z = complicated_f(x)
    out, _ = capfd.readouterr()
    assert 'in f(x): x = 4' in out
    assert z == 4

    z = complicated_g(x)
    out, _ = capfd.readouterr()
    assert 'in g(x): x = 4' in out
    assert 'in h(x): x = 5' in out
    assert z == 4
