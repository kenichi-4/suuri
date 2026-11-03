import matplotlib.pyplot as plt

g = 9.8
y0 = 634.0
vx = 30
dt = 0.1

xs = []
ys = []
t = 0.0
while True:
    x = vx * t
    y = y0 - 0.5 * g * t ** 2
    if y < 0:
        break
    xs.append(x)
    ys.append(y)
    t += dt

plt.scatter(xs, ys)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.show()
