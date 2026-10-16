"""Ejercicio 1 de la guia 1: raices de una cuadratica y biseccion."""

import math

from _metodos import bisecar, graficar, mostrar_filas


def main():
    funcion = lambda x: -0.5 * x**2 + 2.5 * x + 4.5
    raices = (
        (-2.5 + math.sqrt(2.5**2 - 4 * -0.5 * 4.5)) / (2 * -0.5),
        (-2.5 - math.sqrt(2.5**2 - 4 * -0.5 * 4.5)) / (2 * -0.5),
    )
    raiz_mayor = max(raices)
    print("Raices de la cuadratica:", raices)
    filas = bisecar(funcion, 5, 10, max_iter=3)
    mostrar_filas("Biseccion desde [5, 10], tres iteraciones", filas, funcion, raiz_mayor)
    graficar("1. Cuadratica", funcion, (-2, 8))


if __name__ == "__main__":
    main()
