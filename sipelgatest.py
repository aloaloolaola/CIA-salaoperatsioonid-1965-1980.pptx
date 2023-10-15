import sipelgas
from random import randint

for _ in range(100):
    Xr, Yr, Zr = [randint(1, 1000) for _ in range(3)]

    ant_surface = randint(0, 5)
    if ant_surface == 0:
        Xs, Ys, Zs = 0, randint(0, Yr), randint(0, Zr)
    elif ant_surface == 1:
        Xs, Ys, Zs = Xr, randint(0, Yr), randint(0, Zr)
    elif ant_surface == 2:
        Xs, Ys, Zs = randint(0, Xr), 0, randint(0, Zr)
    elif ant_surface == 3:
        Xs, Ys, Zs = randint(0, Xr), Yr, randint(0, Zr)
    elif ant_surface == 4:
        Xs, Ys, Zs = randint(0, Xr), randint(0, Yr), 0
    elif ant_surface == 5:
        Xs, Ys, Zs = randint(0, Xr), randint(0, Yr), Zr
    
    
    honey_surface = randint(0, 5)
    if honey_surface == 0:
        Xm, Ym, Zm = 0, randint(0, Yr), randint(0, Zr)
    elif honey_surface == 1:
        Xm, Ym, Zm = Xr, randint(0, Yr), randint(0, Zr)
    elif honey_surface == 2:
        Xm, Ym, Zm = randint(0, Xr), 0, randint(0, Zr)
    elif honey_surface == 3:
        Xm, Ym, Zm = randint(0, Xr), Yr, randint(0, Zr)
    elif honey_surface == 4:
        Xm, Ym, Zm = randint(0, Xr), randint(0, Yr), 0
    elif honey_surface == 5:
        Xm, Ym, Zm = randint(0, Xr), randint(0, Yr), Zr
    
    
    cuboid = sipelgas.Cuboid(Xr, Yr, Zr, Xs, Ys, Zs, Xm, Ym, Zm).normalise_rotation()
    cuboid.measure_distance()