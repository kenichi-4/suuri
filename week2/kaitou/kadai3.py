import numpy as np
from scipy import linalg


A = np.array([[2, 1, 3, 4,  5, -13],
              [1, 3, 4, 5,  6,   7],
              [1, 4, 5, 6,  7,   8],
              [4, 5, 6, 7,  9,  11],
              [1, 6, 7, 8, 10,  17],
              [1, 7, 8, 9, 11,  21]])
b = np.array([[1], [2], [3], [4], [5], [6]])

x = linalg.solve(A, b)

print("x = ")
print(x)
