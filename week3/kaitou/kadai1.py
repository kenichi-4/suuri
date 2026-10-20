import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

n = 100
b = np.zeros((n, 1))
b[0] = 10

A = -2.0*np.eye(n)
## Aを完成させる:
A[0,0] = A[-1, -1] = 1
for i in range(1, n-1):
    A[i, i-1] = 1
    A[i, i+1] = 1
###################
ux = linalg.solve(A, b)
x = [i/n*10 for i in range(n)]
plt.plot(x, ux)
plt.xlabel("$x$")
plt.ylabel("$u(x)$")
plt.show()
