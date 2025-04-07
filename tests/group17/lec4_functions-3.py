#########################
## EXAMPLE: using print vs return
#########################

def even_with_return(n):
    print("Function with return called")
    return n % 2 == 0

even_with_return(3)
print(even_with_return(3))

def even_no_return(n):
    print("Function without return called")
    remainder = n % 2  # value not used

even_no_return(3)
print(even_no_return(3))  # will print None

# Check even status from 0 to 19
def check_even(n):
    return n % 2 == 0

print("Check 0 to 19:")
for i in range(20):
    print(i, "is even" if check_even(i) else "is odd")


#########################
## EXAMPLE: approximate cube root with bisection
#########################

def cube_root(x, eps):
    low, high = 0.0, max(1.0, x)
    guess = (low + high) / 2
    while abs(guess**3 - x) >= eps:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess

x = 1
while x <= 10000:
    print(f"{cube_root(x, 0.01)} is close to cube root of {x}")
    x *= 10


#########################
## EXAMPLE: functions as arguments
#########################

def A():
    print(">> A")

def B(x):
    print(">> B")
    return x

def C(f):
    print(">> C")
    return f()

print(A())
print(5 + B(2))
print(C(A))


#########################
## EXAMPLE: return function
#########################

def outer():
    def inner(a, b):
        return a + b
    return inner

print(outer()(3, 4))


#########################
## EXAMPLE: scope test 1
#########################

def scope_demo(val):
    temp = 1
    temp +=

