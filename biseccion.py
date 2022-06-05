
def biseccion(f):
    x0 = float('inf')
    x1 = float('-inf')

    while (abs(x0 - x1) > 0.00001):
        x2 = (x0 + x1) / 2
        if f(49) == 0:
            return x2

    return x0, x1
