import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


d=1
node = 51
n = node - 1
h = d/n


f = 20


A = np.zeros((node**2, node**2))
b = np.zeros((node**2,1))


X = np.zeros((node**2, 1))
Y = np.zeros((node**2, 1))


##################################################
# ここを書く
for i in range(n+1):
    for j in range(n+1):
        if i == 0 or i == n or j == 0 or j == n:
            A[i+node*j, i+node*j] = 1
            b[i+node*j] = 0
        else:
            A[i+node*j, i+node*j] = 4
            A[i+node*j, (i-1)+node*j] = -1
            A[i+node*j, (i+1)+node*j] = -1
            A[i+node*j, i+node*(j-1)] = -1
            A[i+node*j, i+node*(j+1)] = -1
            b[i+node*j] = f*h**2
##################################################
u = linalg.solve(A, b)


X = np.zeros((node**2, 1))
Y = np.zeros((node**2, 1))
for i in range(n+1):
    for j in range(n+1):
          X[ i+node*j ] = i*h
          Y[ i+node*j ] = j*h


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
cm = plt.get_cmap('coolwarm')
mappable = ax.scatter(X, Y, u, c=u[:,0], cmap=cm)
fig.colorbar(mappable, ax=ax)
plt.show()
