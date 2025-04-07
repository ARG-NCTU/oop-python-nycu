#########################
## EXAMPLE: print vs return behaviors
#########################

def check_even_with_return(num):
    print("Doing check with return!")
    return num % 2 == 0

check_even_with_return(3)
print(check_even_with_return(3))

def check_even_no_return(num):
    print("Doing check without return.")
    remainder = num % 2

check_even_no_return(3)
print(check_even_no_return(3))

def is_number_even(value):
    return value % 2 == 0

print("0 to 19 even check:")
for number in range(20):
    if is_number_even(number):
        print(f"{number} => even")
    else:
        print(f"{number} => odd")


#########################
## EXAMPLE: bisection method for cube root
#########################

def approx_cube_root(target, tol):
    low = 0.0
    high = max(1.0, target)
    mid = (low + high) / 2
    while abs(mid**3 - target) >= tol:
        if mid**3 < target:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
    return mid

val = 1
while val <= 10000:
    result = approx_cube_root(val, 0.01)
    print(f"{result} is close to ∛{val}")
    val *= 10


#########################
## EXAMPLE: passing and calling functions
#########################

def say_hello():
    print("Inside say_hello")

def echo(value):
    print("Inside echo")
    return value

def call_func(f):
    print("Inside call_func")
    return f()

print(say_hello())
print(5 + echo(2))
print(call_func(say_hello))


#########################
## EXAMPLE: return a function object
#########################

def generator():
    def add(x, y):
        return x + y
    return add

print(generator()(3, 4))


#########################
## EXAMPLE: global and local scope
#########################

def play_with_scope(n):
    temp = 1
    temp += 1
    print(temp)

main_val = 5
play_with_scope(main_val)
print(main_val)

def read_scope(n):
    print(main_val)
    print(main_val + 1)

main_val = 5
read_scope(main_val)
print(main_val)

def dummy(n):
    pass
    # If you want to change global main_val here, use global keyword

main_val = 5
dummy(main_val)
print(main_val)


#########################
## EXAMPLE: changing scope inside nested function
#########################

def outer_test(a):
    def inner_test():
        a = "abc"
    a += 1
    print("a in outer_test =", a)
    inner_test()
    return a

some_num = 3
new_val = outer_test(some_num)


#########################
## EXAMPLE: final tricky scope challenge
#########################

def f(n):
    n += 1
    print("in f(): n =", n)
    return n

var = 3
ret = f(var)
print("main: ret =", ret)
print("main: var =", var)

def g(n):
    def h(n):
        n += 1
        print("in h(): n =", n)
    n += 1
    print("in g(): n =", n)
    h(n)
    return n

var = 3
ret = g(var)
print("main: var =", var)
print("main: ret =", ret)

