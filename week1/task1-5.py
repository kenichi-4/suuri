g = 9.8
y0 = 634.0
vx = 30
dt = 0.1

t = 0.0
while True:
    x = vx * t
    y = y0 - 0.5 * g * t ** 2
    if y < 0:
        break
    print(f't = {t} , ( {x:g} , {y} )')
    t += dt
