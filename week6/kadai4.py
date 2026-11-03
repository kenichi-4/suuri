import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def lorenz( t, x ):
    fx = np.zeros_like(x)
    fx[0] = -10*x[0] + 10*x[1]
    fx[1] = 28*x[0] - x[1] - x[0]*x[2]
    fx[2] = -8/3*x[2] + x[0]*x[1]
    return fx

ts = 0
te = 50
n = 10000

x0 = np.zeros(3)
x0[0] = 1.0
x0[1] = 0.5
x0[2] = 0.5

t = np.linspace(ts, te, n)
for method in ['RK23', 'RK45', 'LSODA', 'BDF', 'Radau']:
    sol = integrate.solve_ivp(lorenz, [ts, te], x0, method=method, dense_output=True)
    z = sol.sol(t)
    plt.plot( t, z[0], label=method )
plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sol = integrate.solve_ivp(lorenz, [ts, te], x0, method='RK45', dense_output=True)
z = sol.sol(t)
ax.plot( z[0], z[1], z[2], linewidth=0.5 )
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
