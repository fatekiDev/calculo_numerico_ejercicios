"""Ejercicio 4 de la guia 1: falsa posicion para hallar la raiz menor."""

from _metodos import falsa_posicion, graficar, mostrar_filas


def main():
    funcion = lambda x: -12 - 21 * x + 18 * x**2 - 2.75 * x**3
    filas = falsa_posicion(funcion, -1, 0, tolerancia=0.05)
    mostrar_filas("Falsa posicion, raiz menor", filas, funcion)
    graficar("4. Cubica", funcion, (-1.5, 2.5))


if __name__ == "__main__":
    main()
