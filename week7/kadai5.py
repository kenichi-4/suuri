import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

gamma = 0.03
Ninf = 13000
p = 0.16
q = 0.32

def f( u ):
    return u**p

def g( v ):
    return v**q

def logistic( t, x ):
    fx = np.zeros_like(x)
    fx[0] = gamma*(1 - x[0]/Ninf)*x[0]
    return fx

def modified_logistic( t, x ):
    fx = np.zeros_like(x)
    fx[0] = gamma*g(max(1 - f(x[0]/Ninf), 0))*x[0]
    return fx

year = [1920, 1925, 1930, 1935, 1940, 1945, 1950, 1955, 1960, 1965,
        1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2008]
data = [5596, 5974, 6445, 6925, 7193, 7215, 8412, 9008, 9430, 9921,
        10467, 11194, 11706, 12105, 12361, 12557, 12693, 12777, 12808]

ts = 1920
te = 2008
n = 1000

x0 = np.zeros(1)
x0[0] = 5500

t = np.linspace(ts, te, n)
sol1 = integrate.solve_ivp(logistic, [ts, te], x0, method='RK45', dense_output=True)
sol2 = integrate.solve_ivp(modified_logistic, [ts, te], x0, method='RK45', dense_output=True, max_step=0.5)

e1 = np.sqrt(np.mean((sol1.sol(year)[0] - data)**2))
e2 = np.sqrt(np.mean((sol2.sol(year)[0] - data)**2))
print("ロジスティック方程式の誤差:", e1)
print("改造したモデルの誤差:", e2)

plt.plot( year, data, 'ko', label='data' )
plt.plot( t, sol1.sol(t)[0], label='logistic' )
plt.plot( t, sol2.sol(t)[0], label='modified' )
plt.legend()
plt.xlabel('year')
plt.ylabel('population [10^4]')
plt.show()
