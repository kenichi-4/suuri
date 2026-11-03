g = 9.8
h0 = 634.0
dt = 0.1

t = 0.0
while True:
    v = g * t
    h = h0 - 0.5 * g * t ** 2
    if h < 0:
        break
    print(f't = {t} [s], h = {h} [m], v = {v} [m/s]')
    t += dt
