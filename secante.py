def secante(f):

    x0 = float(input('Ingrese el limite X0: '))
    x1 = float(input('Ingrese el limite X-1: '))

    f0 = f(x0)
    f1 = f(x1)

    xr = x0 - (f0 * (x0-x1)) / (f1-f0)
    xa = xr
    if xr > x0:
        x0 = xr
    else:
        x1 = xr
    while True:
        f0 = f(x0)
        f1 = f(x1)
        xr = x0 - (f0 * (x0-x1)) / (f1-f0)
        if xr > x0:
            x0 = xr
        else:
            x1 = xr
        xr = x0 - (f0 * (x0-x1)) / (f1-f0)
        E = abs(xr-xa) / xr * 100
        xa = xr
        if E <= 1:
            break

    return xr
