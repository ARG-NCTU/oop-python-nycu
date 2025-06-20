def is_even(number):
    """
    Check if a number is even.
    Args:
        number (int): A positive integer.
    Returns:
        bool: True if even, False otherwise.
    """
    return number % 2 == 0

def check_even_with_message(number):
    """
    Check if a number is even, print a message, and return result.
    Args:
        number (int): A positive integer.
    Returns:
        bool: True if even, False otherwise.
    """
    print(f"Checking if {number} is even")
    return number % 2 == 0

def print_even_status(number):
    """
    Print whether a number is even without returning a value.
    Args:
        number (int): A positive integer.
    Returns:
        None
    """
    print(f"Processing {number} for evenness")
    _ = number % 2  # Compute but don't return

def approximate_cube_root(number, epsilon=0.01):
    """
    Approximate the cube root of a number using bisection search.
    Args:
        number (float): A positive number.
        epsilon (float): Tolerance for approximation.
    Returns:
        dict: {'success': bool, 'guess': float, 'iterations': int}
    """
    if number <= 0:
        return {"success": False, "guess": None, "iterations": 0}
    low = 0.0
    high = max(1, number)
    guess = (low + high) / 2.0
    iterations = 0
    while abs(guess ** 3 - number) >= epsilon and iterations < 10000:
        if guess ** 3 < number:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        iterations += 1
    return {
        "success": abs(guess ** 3 - number) < epsilon,
        "guess": guess,
        "iterations": iterations
    }

def execute_function(func):
    """
    Execute a function and return its result.
    Args:
        func (callable): A function to execute.
    Returns:
        Any: The function's return value.
    """
    print(f"Executing function {func.__name__}")
    return func()

def create_adder():
    """
    Return a function that adds two numbers.
    Returns:
        callable: A function that takes two numbers and returns their sum.
    """
    def adder(a, b):
        return a + b
    return adder

def modify_local_variable(value):
    """
    Modify a local variable and print it.
    Args:
        value (int): Input value.
    Returns:
        int: Modified value.
    """
    x = 1
    x += value
    print(f"Local x: {x}")
    return x

def read_global_variable(value):
    """
    Read and print a global variable plus an offset.
    Args:
        value (int): Input value (unused).
    Returns:
        None
    """
    global_x = 5  # Simulate accessing a global variable
    print(f"Global x: {global_x}")
    print(f"Global x + 1: {global_x + 1}")

def nested_scope_example(input_value):
    """
    Demonstrate nested scope with an inner function.
    Args:
        input_value (int): Input value.
    Returns:
        int: Modified outer value.
    """
    def inner_function():
        local_x = 'abc'
        print(f"In inner_function: x = {local_x}")
    x = input_value + 1
    print(f"In outer function: x = {x}")
    inner_function()
    return x

def complex_scope(input_value):
    """
    Demonstrate complex scope with nested function modifying input.
    Args:
        input_value (int): Input value.
    Returns:
        dict: {'outer': int, 'inner': int}
    """
    def inner_modify(x):
        x = x + 1
        print(f"In inner_modify: x = {x}")
        return x
    outer_x = input_value + 1
    print(f"In outer function: x = {outer_x}")
    inner_x = inner_modify(outer_x)
    return {"outer": outer_x, "inner": inner_x}
