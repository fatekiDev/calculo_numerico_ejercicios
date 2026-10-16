"""Ejercicio 3 de la guia 1: comparar biseccion y falsa posicion."""

from _metodos import bisecar, falsa_posicion, graficar, mostrar_filas


def main():
    funcion = lambda x: -25 + 82 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5
    filas_biseccion = bisecar(funcion, 0, 1, tolerancia=10)
    filas_falsa_posicion = falsa_posicion(funcion, 0, 1, tolerancia=0.2)
    mostrar_filas("Biseccion, error menor a 10%", filas_biseccion, funcion)
    mostrar_filas("Falsa posicion, error menor a 0.2%", filas_falsa_posicion, funcion)
    graficar("3. Polinomio de grado cinco", funcion, (0, 1))


if __name__ == "__main__":
    main()
