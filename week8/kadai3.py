import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def sirv( t, x ):
    fx = np.zeros_like(x)
    N = 1000
    gamma = 0.5
    beta = 0.1
    delta = 0.01
    nu = 0.02
    fx[0] = -gamma/N*x[1]*x[0] - nu*x[0] + delta*x[2]
    fx[1] = gamma/N*x[1]*x[0] - beta*x[1]
    fx[2] = beta*x[1] + nu*x[0] - delta*x[2]
    return fx

ts = 0
te = 1000
n = 10000

x0 = np.zeros(3)
x0[0] = 999
x0[1] = 1
x0[2] = 0

sol = integrate.solve_ivp(sirv, [ts, te], x0, method='RK45', dense_output=True)

t = np.linspace(ts, te, n)
z = sol.sol(t)
print("S + I + R =", z[0][-1] + z[1][-1] + z[2][-1])
print("t = 1000 : S =", z[0][-1], " I =", z[1][-1], " R =", z[2][-1])
plt.plot( t, z.T )
plt.legend( ['S', 'I', 'R'] )
plt.xlabel('t')
plt.show()
