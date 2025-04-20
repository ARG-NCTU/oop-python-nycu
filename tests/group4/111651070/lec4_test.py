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

#####################################
print("=====================================")
print("**              Test1              **")
print("=====================================")
print(f"input: 20, output: {is_even_with_return(20)}")
print("-------------------------------------")
print(f"input: 21, output: {is_even_with_return(21)}")
print("=====================================")
print("**              Test2              **")
print("=====================================")
print(f"input: 20, output: {is_even_without_return(20)}")
print("-------------------------------------")
print(f"input: 21, output: {is_even_without_return(21)}")
print("=====================================")
print("**              Test3              **")
print("=====================================")
is_even_function_test(6)
print("=====================================")
print("**              Test4              **")
print("=====================================")
bisection_cuberoot_approx_test(1000)
print("=====================================")
print("**              Test5              **")
print("=====================================")
print(f"input: func_a, output: {func_a()}")
print("-------------------------------------")
print(f"input: 5+func_b(2), output: {5+func_b(2)}")
print("-------------------------------------")
print(f"input: func_c(func_a), output: {func_c(func_a)}")