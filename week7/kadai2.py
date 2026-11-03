import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def logistic( t, x ):
    fx = np.zeros_like(x)
    gamma = 0.03
    Ninf = 13000
    fx[0] = gamma*(1 - x[0]/Ninf)*x[0]
    return fx

ts = 1920
te = 2008
n = 1000

x0 = np.zeros(1)
x0[0] = 5500

sol = integrate.solve_ivp(logistic, [ts, te], x0, method='RK45', dense_output=True)

t = np.linspace(ts, te, n)
z = sol.sol(t)
plt.plot( t, z.T )
plt.xlabel('year')
plt.ylabel('population [10^4]')
plt.show()
