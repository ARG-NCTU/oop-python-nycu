#########################
## EXAMPLE: combinations of print and return
#########################
def is_even_with_return(i):
    print('with return')
    remainder = i % 2
    return remainder == 0

is_even_with_return(3)
print(is_even_with_return(3))

def is_even_without_return(i):
    print('without return')
    remainder = i % 2

is_even_without_return(3)
print(is_even_without_return(3))

#########################
## Simple is_even
#########################
def is_even(i):
    return (i % 2) == 0

print("All numbers between 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")

#########################
## Bisection cube root
#########################
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

x = 1
while x <= 10000:
    approx = bisection_cuberoot_approx(x, 0.01)
    print(approx, "is close to cube root of", x)
    x *= 10

#########################
## Functions as arguments
#########################
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

#########################
## Returning function objects
#########################
def f():
    def x(a, b):
        return a + b
    return x

val = f()(3, 4)
print(val)

#########################
## Scope example
#########################
def f_scope(y):
    x = 1
    x += 1
    print(x)

x = 5
f_scope(x)
print(x)

def g_scope(y):
    print(x)
    print(x + 1)

x = 5
g_scope(x)
print(x)

#########################
## hader scope example
#########################
def g2(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g2(x)

#########################
## complicated scope
#########################
def f2(x):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f2(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

def g3(x):
    def h(x):
        x = x + 1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g3(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)
