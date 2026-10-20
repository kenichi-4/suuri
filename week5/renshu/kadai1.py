import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt


def forward_euler(x0, tau, tf, f):
    ti = 0
    xi = x0
    tlist = [ ti ]
    xlist = [ x0 ]
    while ti < tf:
        tip1 = ti + tau
        xip1 =
        tlist.append(tip1)
        xlist.append(xip1)
        ti, xi = tip1, xip1
    return (tlist, xlist)


def strogatz( t, x ):
    a =
    b =
    c =
    d =
    fx = np.zeros_like(x)
    fx[0] =
    fx[1] =
    return fx


x0 = np.zeros(2)
x0[0] =
x0[1] =
t, x = forward_euler(x0, 0.1, 10, strogatz)
plt.plot(t, x)
plt.show()
