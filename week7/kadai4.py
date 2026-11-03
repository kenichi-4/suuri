import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

Ninf = 10000

def rumor( t, x ):
    fx = np.zeros_like(x)
    fx[0] = gamma*(1 - x[0]/Ninf)*x[0]
    return fx

ts = 0
te = 48
n = 1000

x0 = np.zeros(1)
x0[0] = 1

t = np.linspace(ts, te, n)
for gamma in [0.25, 0.5, 1.0]:
    sol = integrate.solve_ivp(rumor, [ts, te], x0, method='RK45', dense_output=True)
    z = sol.sol(t)
    plt.plot( t, z[0], label='gamma = ' + str(gamma) )
plt.legend()
plt.xlabel('t [hour]')
plt.ylabel('number of people who know')
plt.show()
