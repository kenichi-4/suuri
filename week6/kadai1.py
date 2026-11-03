import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


def heun(x0, tau, tf, f):
    ti = 0
    xi = x0
    tlist = [ ti ]
    xlist = [ x0 ]
    while ti < tf:
        tip1 = ti + tau
        x_euler = xi + tau * f(ti, xi)
        xip1 = xi + tau / 2 * (f(ti, xi) + f(tip1, x_euler))
        tlist.append(tip1)
        xlist.append(xip1)
        ti, xi = tip1, xip1
    return (tlist, xlist)


def strogatz( t, x ):
    a = 0
    b = 1
    c = -1
    d = 0
    fx = np.zeros_like(x)
    fx[0] = a*x[0] + b*x[1]
    fx[1] = c*x[0] + d*x[1]
    return fx


x0 = np.zeros(2)
x0[0] = 1
x0[1] = 0
t, x = heun(x0, 0.1, 10, strogatz)
plt.plot(t, x)
plt.show()
