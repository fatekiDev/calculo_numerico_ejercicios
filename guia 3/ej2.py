"""Ejercicio 2 de la guia 3: comparar Newton y biseccion."""

import math

from _metodos import biseccion, graficar, imprimir_iteraciones, newton


def main():
    funcion = lambda x: math.exp(-x) - 3 * x
    derivada = lambda x: -math.exp(-x) - 3
    filas_newton = newton(funcion, derivada, 0, tolerancia=0.05)
    filas_biseccion = biseccion(funcion, 0, 1, tolerancia=0.05)
    imprimir_iteraciones("Newton-Raphson desde x0=0", filas_newton, funcion)
    imprimir_iteraciones("Biseccion en [0, 1]", filas_biseccion, funcion)
    print(
        f"Iteraciones: Newton {len(filas_newton)}, biseccion {len(filas_biseccion)} "
        "(con el mismo criterio de error aproximado)."
    )
    graficar("2. exp(-x) - 3x", funcion, (-0.2, 1.2), (0, 1))


if __name__ == "__main__":
    main()
