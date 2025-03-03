import numpy as np

# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Sigmoid Derivative Function
def derivative_sigmoid(x):
    return x * (1 - x)


