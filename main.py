from sympy import sympify

from newton import newton
from biseccion import biseccion

metodos = {
    1: newton,
    2: biseccion
}


def main():
    print("Proyecto 2")
    print("----------\n")
    print("Inserte los datos para resolver una ecuación")

    expr = sympify(input("Ingrese la ecuación: "))

    print("\nQué método desea utilizar para resolver la ecuación?")
    print("1. Método de Newton Raphson")
    print("2. Método de Bisección")

    metodo = int(input("> "))

    if metodo not in metodos.keys():
        print("Método no válido")
        return

    def f(v): return expr.evalf(subs={"x": v})

    print("\nEl resultado es:", metodos[metodo](f, expr))


if __name__ == "__main__":
    main()
