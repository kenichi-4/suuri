import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def sir( t, x ):
    fx = np.zeros_like(x)
    N = 1000
    gamma = 0.5
    beta = 0.1
    fx[0] = -gamma/N*x[1]*x[0]
    fx[1] = gamma/N*x[1]*x[0] - beta*x[1]
    fx[2] = beta*x[1]
    return fx

ts = 0
te = 100
n = 3000

x0 = np.zeros(3)
x0[0] = 999
x0[1] = 1
x0[2] = 0

sol = integrate.solve_ivp(sir, [ts, te], x0, method='RK45', dense_output=True)

t = np.linspace(ts, te, n)
z = sol.sol(t)
plt.plot( t, z.T )
plt.legend( ['S', 'I', 'R'] )
plt.xlabel('t')
plt.show()
