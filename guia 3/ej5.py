"""Ejercicio 5 de la guia 3: comportamiento de Newton para arctan(x)."""

import math

from _metodos import biseccion, graficar, imprimir_iteraciones, newton


def main():
    funcion = math.atan
    derivada = lambda x: 1 / (1 + x**2)
    filas_newton = newton(funcion, derivada, 1.5, iteraciones=6)
    imprimir_iteraciones("Newton para arctan(x), seis pasos", filas_newton, funcion)
    print(
        "La iteracion se aleja de la raiz 0. En [-1, 2], biseccion si queda "
        "acotada por el cambio de signo y converge sin depender de x0."
    )
    graficar("5. arctan(x)", funcion, (-2, 2), (-1, 2))


if __name__ == "__main__":
    main()
