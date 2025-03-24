from test_lec7 import Mat
import numpy as np

m1 = Mat([[1, 2, 3],
          [4, 5, 6]])

m2 = Mat([[1, 2],
          [3, 4],
          [5, 6]])

m3 = m1 * m2
m3.transpose().print()
print(m3.transpose())
# [[22, 49]
#  [28, 64]]

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[1, 2],
              [3, 4],
              [5, 6]])

def matmul(A, B):
    return np.array([np.dot(a, B) for a in A])

print(matmul(A, B))
# [[22, 28]
#  [49, 64]]