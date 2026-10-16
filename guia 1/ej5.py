"""Ejercicio 5 de la guia 1: resolver sin(x) = x^2."""

import math

from _metodos import bisecar, graficar, mostrar_filas


def main():
    funcion = lambda x: math.sin(x) - x**2
    filas = bisecar(funcion, 0.5, 1, tolerancia=2)
    mostrar_filas("sin(x) = x^2", filas, funcion)
    print(f"Comprobacion final sin(x) - x^2 = {funcion(filas[-1][1]):.10g}")
    graficar("5. sin(x) - x^2", funcion, (0, 1.2))


if __name__ == "__main__":
    main()
