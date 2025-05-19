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
    Uses bisection to approximate cube root of x within epsilon
    """
    low, high = 0.0, x
    guess = (low + high)/2.0
    while abs(guess**3 - x) >= epsilon:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
    return guess

def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

def f():
    def x(a, b):
        return a + b
    return x

def f_scope(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

def g_scope(x):
    def h(x):
        x = x + 1
        print("in h(x): x =", x)
    x = x + 1
    print('in g(x): x =', x)
    h(x)
    return x

if __name__ == "__main__":
    # 範例執行
    print(is_even_with_return(3))
    print(is_even_without_return(3))
    print(is_even(4))
    print(bisection_cuberoot_approx(27, 0.01))
    print(func_b(5), func_c(func_a))
    print(f()(3,4))
    print(f_scope(3))
    print(g_scope(3))
