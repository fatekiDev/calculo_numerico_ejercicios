"""Ejercicio 6 de la guia 1: comparar dos metodos para ln(x^2) = 0.7."""

import math

from _metodos import bisecar, falsa_posicion, graficar, mostrar_filas


def main():
    funcion = lambda x: math.log(x**2) - 0.7
    raiz = math.exp(0.7 / 2)
    mostrar_filas(
        "Tres iteraciones de biseccion",
        bisecar(funcion, 0.5, 2, max_iter=3),
        funcion,
        raiz,
    )
    mostrar_filas(
        "Tres iteraciones de falsa posicion",
        falsa_posicion(funcion, 0.5, 2, max_iter=3),
        funcion,
        raiz,
    )
    graficar("6. ln(x^2) - 0.7", funcion, (0.2, 2.5))


if __name__ == "__main__":
    main()
