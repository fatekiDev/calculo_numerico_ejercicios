"""Ejercicio 2 de la guia 1: biseccion de un polinomio cubico."""

from _metodos import bisecar, graficar, mostrar_filas


def main():
    funcion = lambda x: 5 * x**3 - 5 * x**2 + 6 * x - 2
    filas = bisecar(funcion, 0, 1, tolerancia=10)
    mostrar_filas("Biseccion, error menor a 10%", filas, funcion)
    graficar("2. Polinomio cubico", funcion, (-0.5, 1.5))


if __name__ == "__main__":
    main()
