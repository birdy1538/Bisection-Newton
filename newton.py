from sympy import *


def newton(f, expr):
    x = symbols('x')
    r = int(input('Valor inicial: '))

    y_diff = Derivative(expr, x)
    def g(v): return y_diff.doit().evalf(subs={x: v})

    iteraciones = 0
    while(abs(f(r)) > 1e-5):
        fa = f(r)
        fb = g(r)
        r -= fa/fb
        iteraciones += 1

    return r, iteraciones
