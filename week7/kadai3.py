import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def logistic( t, x ):
    fx = np.zeros_like(x)
    gamma = -0.02
    Ninf = 13000
    fx[0] = gamma*(1 - x[0]/Ninf)*x[0]
    return fx

ts = 2008
te = 2200
n = 2000

x0 = np.zeros(1)
x0[0] = 12800

sol = integrate.solve_ivp(logistic, [ts, te], x0, method='RK45', dense_output=True)

t = np.linspace(ts, te, n)
z = sol.sol(t)
i = np.argmax(z[0] < 10000)
print("1億人を下回る年:", t[i])

plt.plot( t, z.T )
plt.axhline(10000, color='gray', linestyle='--')
plt.xlabel('year')
plt.ylabel('population [10^4]')
plt.show()
