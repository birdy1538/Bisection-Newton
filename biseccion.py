def biseccion(f):
    a = int(input("Inserte el limite izquierdo: "))
    b = int(input("Inserte el limite derecho: "))

    c = (a + b) / 2
    iteraciones = 0
    while (abs(f(c)) > 1e-5):
        c = (a + b) / 2
        if f(c)*f(a) > 0:
            a = c
        else:
            b = c
        iteraciones += 1

    return c, iteraciones
