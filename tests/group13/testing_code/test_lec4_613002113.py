def check_divisible_by_two_with_output(num):
    """ 
    Input: num, a positive int
    Returns True if num is even, otherwise False
    """
    print('checking with output')
    mod_result = num % 2
    return mod_result == 0

check_divisible_by_two_with_output(3) 
print(check_divisible_by_two_with_output(3))

def check_divisible_by_two_no_output(num):
    """ 
    Input: num, a positive int
    Does not return anything
    """
    print('checking without output')
    mod_result = num % 2

check_divisible_by_two_no_output(3)
print(check_divisible_by_two_no_output(3))

def check_divisible_by_two(num):
    """ 
    Input: num, a positive int
    Returns True if num is even, otherwise False
    """
    mod_result = num % 2
    return mod_result == 0

print("All numbers between 0 and 20: even or not")
for num in range(20):
    if check_divisible_by_two(num):
        print(num, "even")
    else:
        print(num, "odd")

def binary_search_cube_root(value, precision):
    """
    Input: value, an integer
    Uses bisection to approximate the cube root of value to within precision
    Returns: a float approximating the cube root of value
    """
    min_bound = 0.0
    max_bound = value
    estimate = (max_bound + min_bound)/2.0
    while abs(estimate**3 - value) >= precision:
        if estimate**3 < value:
            min_bound = estimate
        else:
            max_bound = estimate
        estimate = (max_bound + min_bound)/2.0
    return estimate

value = 1
while value <= 10000:
    result = binary_search_cube_root(value, 0.01)
    print(result, "is close to cube root of", value)
    value *= 10

def operation_a():
    print('inside operation_a')

def operation_b(param):
    print('inside operation_b')
    return param

def operation_c(func_param):
    print('inside operation_c')
    return func_param()

print(operation_a())
print(5+operation_b(2))
print(operation_c(operation_a))

def create_function():
    def add_numbers(first, second):
        return first+second
    return add_numbers
    
result = create_function()(3,4)
print(result)

def test_function_a(param):
    local_var = 1
    local_var += 1
    print(local_var)
local_var = 5
test_function_a(local_var)
print(local_var)

def test_function_b(param):
    print(local_var)
    print(local_var+1)
local_var = 5
test_function_b(local_var)
print(local_var)

def test_function_c(param):
    pass
local_var = 5
test_function_c(local_var)
print(local_var)

def outer_function(param):
    def inner_function():
        param = 'abc'
    param = param + 1
    print('in outer_function(param): param =', param)
    inner_function()
    return param

param = 3
result_var = outer_function(param)

def process_data(input_val):
   input_val = input_val + 1
   print('in process_data(input_val): input_val =', input_val)
   return input_val

input_val = 3
output_val = process_data(input_val)
print('in main program scope: output_val =', output_val)
print('in main program scope: input_val =', input_val)

def wrapper_function(input_val):
    def nested_function(input_val):
        input_val = input_val+1
        print("in nested_function(input_val): input_val = ", input_val)
    input_val = input_val + 1
    print('in wrapper_function(input_val): input_val = ', input_val)
    nested_function(input_val)
    return input_val

input_val = 3
output_val = wrapper_function(input_val)
print('in main program scope: input_val = ', input_val)
print('in main program scope: output_val = ', output_val)