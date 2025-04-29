def is_even_with_return( i ):
    print('with return')
    remainder = i % 2
    return remainder == 0

def is_even_without_return( i ):
    print('without return')
    remainder = i % 2

def is_even( i ):
    remainder = i % 2
    return remainder == 0
def is_even_function_test(d):
    print(f"All numbers between 0 and {d}: even or not")
    for i in range(d):
        if is_even(i):
            print(i, "even")
        else:
            print(i, "odd")

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
def bisection_cuberoot_approx_test(num):
    x = 1
    while x < num:
        approx = bisection_cuberoot_approx(x, 0.01)
        print(approx, "is close to cube root of", x)
        x *= 10

def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z()

def ff():
    def x(a, b):
        return a+b
