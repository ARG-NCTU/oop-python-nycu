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
    return x

def f(y):
    x = 1
    x += 1
    print(f"x = {x}")

def g(y):
    print(f"x = {x}")
    print(f"x+1 = {x+1}")

def h(y):
    pass

def i(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in i(x): x =', x)
    h()
    return x

def j(x):
   x = x + 1
   print('in j(x): x =', x)
   return x

def k(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in k(x): x = ', x)
    h(x)
    return x

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
print("=====================================")
print("**              Test6              **")
print("=====================================")
print(f"input: f()(3, 4), output: {ff()(3, 4)}")
print("-------------------------------------")
print(f"input: f()(2, 10), output: {ff()(2, 10)}")
print("=====================================")
print("**              Test7              **")
print("=====================================")
x = 7
print(f"x = 7")
print("input: 7")
f(x)
print("-------------------------------------")
g(x)
print("-------------------------------------")
h(x)
print("-------------------------------------")
i(x)
print("-------------------------------------")
z = j(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)
print("-------------------------------------")
z = k(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)