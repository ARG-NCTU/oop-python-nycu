import numpy as np
import time

# Using Python loop to compute element-wise product of two arrays
def compute_product_with_loop(a, b):
    result = np.zeros_like(a)
    for i in range(len(a)):
        result[i] = a[i] * b[i]
    return result

# Using NumPy to compute element-wise product of two arrays
def compute_product_with_numpy(a, b):
    return a * b

# Generate two arrays of size 10 million
a = np.random.rand(10000000)
b = np.random.rand(10000000)

# Compute element-wise product using Python loop and time it
start = time.time()
result_loop = compute_product_with_loop(a, b)
end = time.time()
print("Time taken with Python loop: ", end - start, "seconds")

# Compute element-wise product using NumPy and time it
start = time.time()
result_numpy = compute_product_with_numpy(a, b)
end = time.time()
print("Time taken with NumPy: ", end - start, "seconds")

