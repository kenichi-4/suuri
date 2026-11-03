import matplotlib.pyplot as plt

g = 9.8
h0 = 634.0
dt = 0.1

ts = []
hs = []
t = 0.0
while True:
    h = h0 - 0.5 * g * t ** 2
    ts.append(t)
    hs.append(h)
    if h < 0:
        break
    t += dt

plt.scatter(ts, hs)
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.show()
