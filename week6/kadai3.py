import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def lotka_volterra( t, x ):
    fx = np.zeros_like(x)
    a = 1.0
    b = 0.1
    c = 0.075
    d = 1.5
    fx[0] = a*x[0] - b*x[0]*x[1]
    fx[1] = c*x[0]*x[1] - d*x[1]
    return fx

ts = 0
te = 50
n = 3000

x0 = np.zeros(2)
x0[0] = 10.0
x0[1] = 5.0

sol = integrate.solve_ivp(lotka_volterra, [ts, te], x0, method='RK45', dense_output=True)

t = np.linspace(ts, te, n)
z = sol.sol(t)
plt.plot( t, z.T )
plt.legend( ['x', 'y'] )
plt.xlabel('t')
plt.show()
