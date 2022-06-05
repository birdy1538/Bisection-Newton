from sympy import sympify

from newton import newton
from biseccion import biseccion


def choose_method(method, f, expr):
    if method == 1:
        return newton(f, expr)
    elif method == 2:
        return biseccion(f)
    else:
        print("Método no válido")
        return None


def main():
    print("Proyecto 2")
    print("----------\n")
    print("Inserte los datos para resolver una ecuación")

    expr = sympify(input("Ingrese la ecuación: "))

    print("\nQué método desea utilizar para resolver la ecuación?")
    print("1. Método de Newton Raphson")
    print("2. Método de Bisección")

    metodo = int(input("> "))

    def f(v): return expr.evalf(subs={"x": v})

    result, iteraciones = choose_method(metodo, f, expr)
    if result == None:
        return
    print(f"\nEl resultado es: {result} luego de {iteraciones} iteraciones")


if __name__ == "__main__":
    main()
