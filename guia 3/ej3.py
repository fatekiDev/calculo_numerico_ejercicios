"""Ejercicio 3 de la guia 3: cuatro iteraciones de Newton."""

import math

from _metodos import cifras_significativas, imprimir_iteraciones, newton


def main():
    funcion = lambda x: math.log(x) + x**2 - 1
    derivada = lambda x: 1 / x + 2 * x
    filas = newton(funcion, derivada, 1.4, iteraciones=4)
    imprimir_iteraciones("Cuatro iteraciones de Newton", filas, funcion)
    print(
        "Cifras significativas segun el error aproximado final: "
        f"{cifras_significativas(filas[-1][2])}"
    )


if __name__ == "__main__":
    main()
