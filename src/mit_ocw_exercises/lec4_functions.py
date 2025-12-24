#########################
## EXAMPLE: combinations of print and return
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20is_even_with_return(%20i%20%29%3A%0A%20%20%20%20%22%22%22%20%0A%20%20%20%20Input%3A%20i,%20a%20positive%20int%0A%20%20%20%20Returns%20True%20if%20i%20is%20even,%20otherwise%20False%0A%20%20%20%20%22%22%22%0A%20%20%20%20print('with%20return'%29%0A%20%20%20%20remainder%20%3D%20i%20%25%202%0A%20%20%20%20return%20remainder%20%3D%3D%200%0A%0Ais_even_with_return(3%29%20%0Aprint(is_even_with_return(3%29%20%29%0A%0Adef%20is_even_without_return(%20i%20%29%3A%0A%20%20%20%20%22%22%22%20%0A%20%20%20%20Input%3A%20i,%20a%20positive%20int%0A%20%20%20%20Does%20not%20return%20anything%0A%20%20%20%20%22%22%22%0A%20%20%20%20print('without%20return'%29%0A%0Ais_even_without_return(3%29%0Aprint(is_even_without_return(3%29%20%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
def is_even_with_return( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

is_even_with_return(3) 
print(is_even_with_return(3) )

def is_even_without_return( i ):
    """ 
    Input: i, a positive int
    Does not return anything
    """
    print('without return')
    remainder = i % 2

is_even_without_return(3)
print(is_even_without_return(3) )
def is_even( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    Raises: ValueError if i is not a non-negative integer
    """
    if not isinstance(i, int) or i < 0:
        raise ValueError(f"Expected non-negative integer, got {type(i).__name__}: {i}")
    remainder = i % 2
    return remainder == 0

# Use the is_even function later on in the code with error handling
print("\n--- Testing is_even function ---")
test_numbers = [0, 1, 2, 5, 10, 15, 20]
for num in test_numbers:
    try:
        result = is_even(num)
        status = "even" if result else "odd"
        print(f"{num} is {status}")
    except ValueError as e:
        print(f"Error checking {num}: {e}")

#########################
## EXAMPLE: applying functions to repeat same task many times
#########################
def bisection_cuberoot_approx(x, epsilon):
    """
    Input: x, a non-negative number; epsilon, tolerance for accuracy
    Uses bisection to approximate the cube root of x to within epsilon
    Returns: a float approximating the cube root of x
    Raises: ValueError if epsilon is non-positive or x is negative
    """
    if epsilon <= 0:
        raise ValueError(f"epsilon must be positive, got {epsilon}")
    if x < 0:
        raise ValueError(f"Cannot compute cube root of negative number: {x}")
    low = 0.0
    high = max(x, 1.0)  # Handle case when x < 1
    guess = (high + low) / 2.0
    iteration_count = 0
    max_iterations = 10000  # Prevent infinite loops
    while abs(guess**3 - x) >= epsilon and iteration_count < max_iterations:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        iteration_count += 1
    return guess

# Demonstrate cube root approximation with error handling
print("\n--- Cube root approximations using bisection ---")
try:
    x = 1
    while x <= 10000:
        approx = bisection_cuberoot_approx(x, 0.01)
        print(f"{approx:.6f} is close to cube root of {x}")
        x *= 10
except ValueError as e:
    print(f"Error: {e}")


#########################
## EXAMPLE: functions as arguments
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20func_a(%29%3A%0A%20%20%20%20print('inside%20func_a'%29%0A%0Adef%20func_b(y%29%3A%0A%20%20%20%20print('inside%20func_b'%29%0A%20%20%20%20return%20y%0A%0Adef%20func_c(z%29%3A%0A%20%20%20%20print('inside%20func_c'%29%0A%20%20%20%20return%20z(%29%0A%0Aprint(func_a(%29%29%0Aprint(5%2Bfunc_b(2%29%29%0Aprint(func_c(func_a%29%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
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
print(5+func_b(2))
print(func_c(func_a))


#########################
## UTILITY HELPER: compute multiple cuberoot approximations efficiently
#########################
def compute_multiple_cuberoots(values, epsilon=0.01):
    """
    Compute cube roots for multiple values at once.
    Input: values (list of numbers), epsilon (tolerance, default 0.01)
    Returns: dictionary mapping input values to their approximate cube roots
    """
    results = {}
    for x in values:
        try:
            results[x] = bisection_cuberoot_approx(x, epsilon)
        except ValueError as e:
            results[x] = f"Error: {e}"
    return results


#########################
## EXAMPLE: returning function objects
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20f(%29%3A%0A%20%20%20%20def%20x(a,%20b%29%3A%0A%20%20%20%20%20%20%20%20return%20a%2Bb%0A%20%20%20%20return%20x%0A%20%20%20%20%0Aval%20%3D%20f(%29(3,4%29%0Aprint(val%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
def f():
    def x(a, b):
        return a+b
    return x
    
# the first part, f(), returns a function object
# then apply that function with parameters 3 and 4
val = f()(3,4)
print(val)



#########################
## EXAMPLE: shows accessing variables outside scope
#########################
def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

def h(y):
    pass
    #x += 1 #leads to an error without line `global x` inside h
x = 5
h(x)
print(x)


#########################
## EXAMPLE: hader scope example from slides
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20g(x%29%3A%0A%20%20%20%20def%20h(%29%3A%0A%20%20%20%20%20%20%20%20x%20%3D%20'abc'%0A%20%20%20%20x%20%3D%20x%20%2B%201%0A%20%20%20%20print('in%20g(x%29%3A%20x%20%3D',%20x%29%0A%20%20%20%20h(%29%0A%20%20%20%20return%20x%0A%0Ax%20%3D%203%0Az%20%3D%20g(x%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)


#########################
## EXAMPLE: complicated scope, test yourself!
## Python Tutor link: http://www.pythontutor.com/visualize.html#code=def%20f(x%29%3A%0A%20%20%20x%20%3D%20x%20%2B%201%0A%20%20%20print('in%20f(x%29%3A%20x%20%3D',%20x%29%0A%20%20%20return%20x%0A%0Ax%20%3D%203%0Az%20%3D%20f(x%29%0Aprint('in%20main%20program%20scope%3A%20z%20%3D',%20z%29%0Aprint('in%20main%20program%20scope%3A%20x%20%3D',%20x%29%0A%0Adef%20g(x%29%3A%0A%20%20%20%20def%20h(x%29%3A%0A%20%20%20%20%20%20%20%20x%20%3D%20x%2B1%0A%20%20%20%20%20%20%20%20print(%22in%20h(x%29%3A%20x%20%3D%20%22,%20x%29%0A%20%20%20%20x%20%3D%20x%20%2B%201%0A%20%20%20%20print('in%20g(x%29%3A%20x%20%3D%20',%20x%29%0A%20%20%20%20h(x%29%0A%20%20%20%20return%20x%0A%0Ax%20%3D%203%0Az%20%3D%20g(x%29%0Aprint('in%20main%20program%20scope%3A%20x%20%3D%20',%20x%29%0Aprint('in%20main%20program%20scope%3A%20z%20%3D%20',%20z%29%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
#########################
def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)
