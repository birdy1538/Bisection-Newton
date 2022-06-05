from sympy import *


def newton(f, expr):
    x = symbols('x')
    r = int(input('Valor inicial: '))

    y_diff = Derivative(expr, x)
    def g(v): return y_diff.doit().evalf(subs={x: v})

    while(abs(f(r)) > 0.0000000001):
        fa = f(r)
        fb = g(r)
        r -= fa/fb
    return r
