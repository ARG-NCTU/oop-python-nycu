def is_even(i):
    return i % 2 == 0

def bisection_cuberoot_approx(x, epsilon=0.01):
    low, high = 0.0, x
    guess = (low + high) / 2
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess

def apply_func(f, value):
    return f(value)

def make_adder(a):
    def add(b):
        return a + b
    return add

def show_scope_demo():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()
 
# test start from here

def test_is_even():
    assert is_even(2)
    assert not is_even(3)

def test_bisection_cuberoot_approx():
    assert abs(bisection_cuberoot_approx(27) - 3) < 0.01
    assert abs(bisection_cuberoot_approx(8) - 2) < 0.01

def test_apply_func():
    assert apply_func(lambda x: x * 2, 5) == 10
    assert apply_func(is_even, 4)

def test_make_adder():
    add_3 = make_adder(3)
    assert add_3(4) == 7
    assert make_adder(10)(5) == 15

def test_show_scope_demo():
    assert show_scope_demo() == 11

def test_all():
    test_is_even()
    test_bisection_cuberoot_approx()
    test_apply_func()
    test_make_adder()
    test_show_scope_demo()
