#########################
## EXAMPLE: print vs return combinations
#########################

def is_even_with_return(num):
    """Check if the input number is even. Return True or False."""
    print('Checking with return')
    return num % 2 == 0

is_even_with_return(3)
print(is_even_with_return(3))

def is_even_without_return(num):
    """Check if the input number is even. Does not return anything."""
    print('Checking without return')
    result = num % 2  # Assigned but unused

is_even_without_return(3)
print(is_even_without_return(3))  # Will print None

# Define a reusable even check function
def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

print("Evenness of numbers from 0 to 19:")
for i in range(20):
    status = "even" if is_even(i) else "odd"
    print(i, status)


#########################
## EXAMPLE: bisection cube root approximation
#########################

def cube_root_bisection(n, tolerance):
    """
    Approximate the cube root of n using bisection within the given tolerance.
    """
    low = 0.0
    high = max(1.0, n)
    guess = (low + high) / 2.0
    while abs(guess**3 - n) >= tolerance:
        if guess**3 < n:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
    return guess

value = 1
while value <= 10000:
    approx_root = cube_root_bisection(value, 0.01)
    print(f"{approx_root} is approximately the cube root of {value}")
    value *= 10


#########################
## EXAMPLE: functions as inputs
#########################

def action_a():
    print('>> Inside action_a')

def action_b(data):
    print('>> Inside action_b')
    return data

def action_c(func):
    print('>> Inside action_c')
    return func()

print(action_a())
print(5 + action_b(2))
print(action_c(action_a))


#########################
## EXAMPLE: return a function from another function
#########################

def create_adder():
    def adder(a, b):
        return a + b
    return adder

result = create_adder()(3, 4)
print(result)


#########################
## EXAMPLE: scope and variable shadowing
#########################

def modify(x_val):
    temp = 1
    temp += 1
    print(temp)

x_global = 5
modify(x_global)
print(x_global)

def display(y_val):
    print(x_global)
    print(x_global + 1)

x_global = 5
display(x_global)
print(x_global)

def no_change(param):
    pass
    # To modify global x_global inside, use: global x_global

x_global = 5
no_change(x_global)
print(x_global)


#########################
## EXAMPLE: nested scope and shadowing
#########################

def outer(value):
    def inner():
        local_var = 'abc'
    value += 1
    print('inside outer(): value =', value)
    inner()
    return value

x_input = 3
result = outer(x_input)


#########################
## EXAMPLE: scope trickiness challenge
#########################

def increment(val):
    val += 1
    print('inside increment(): val =', val)
    return val

x_val = 3
z_val = increment(x_val)
print('main scope: z_val =', z_val)
print('main scope: x_val =', x_val)

def outer_function(val):
    def nested_function(val):
        val += 1
        print("inside nested_function(): val =", val)
    val += 1
    print('inside outer_function(): val =', val)
    nested_function(val)
    return val

x_val = 3
z_val = outer_function(x_val)
print('main scope: x_val =', x_val)
print('main scope: z_val =', z_val)

