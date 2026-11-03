import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


def heun_adaptive(x0, tf, f, tol):
    ti = 0
    xi = x0
    tau = 0.1
    tlist = [ ti ]
    xlist = [ x0 ]
    while ti < tf:
        if ti + tau > tf:
            tau = tf - ti
        tip1 = ti + tau
        x_euler = xi + tau * f(ti, xi)
        x_heun = xi + tau / 2 * (f(ti, xi) + f(tip1, x_euler))
        err = np.max(np.abs(x_heun - x_euler))
        if err > tol:
            tau = tau / 4
            continue
        tlist.append(tip1)
        xlist.append(x_heun)
        ti, xi = tip1, x_heun
        tau = tau * 2
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
t, x = heun_adaptive(x0, 10, strogatz, 10**(-3))
print(len(t) - 1, "steps")
plt.plot(t, x, marker=".")
plt.show()
