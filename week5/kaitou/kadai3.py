import numpy as np
import matplotlib.pyplot as plt


def forward_euler(x0, tau, tf, f):
    ti = 0
    xi = x0
    tlist = [ ti ]
    xlist = [ x0 ]
    while ti < tf:
        tip1 = ti + tau
        xip1 = xi + tau * f(ti, xi)
        tlist.append(tip1)
        xlist.append(xip1)
        ti, xi = tip1, xip1
    return (tlist, xlist)


K = 100


def logistic( t, x ):
    fx = np.zeros_like(x)
    fx[0] = r * x[0] * (1 - x[0] / K)
    return fx


plt.figure()
for r in [0.5, 1.0, 2.0]:
    x0 = np.zeros(1)
    x0[0] = 5
    t, x = forward_euler(x0, 0.01, 20, logistic)
    plt.plot(t, x, label="r = " + str(r))
plt.xlabel("t")
plt.ylabel("N(t)")
plt.legend()
plt.savefig("kadai3_r.png")
plt.show()

r = 1.0
plt.figure()
for n0 in [5, 50, 150]:
    x0 = np.zeros(1)
    x0[0] = n0
    t, x = forward_euler(x0, 0.01, 20, logistic)
    plt.plot(t, x, label="N(0) = " + str(n0))
plt.xlabel("t")
plt.ylabel("N(t)")
plt.legend()
plt.savefig("kadai3_N0.png")
plt.show()
