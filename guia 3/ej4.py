"""Ejercicio 4 de la guia 3: Newton para (x-1)^2 + cos(2x)."""

import math

from _metodos import graficar, imprimir_iteraciones, newton


def main():
    funcion = lambda x: (x - 1) ** 2 + math.cos(2 * x)
    derivada = lambda x: 2 * (x - 1) - 2 * math.sin(2 * x)
    filas = newton(funcion, derivada, 1, tolerancia=0.1)
    imprimir_iteraciones("Newton para (x-1)^2 + cos(2x)", filas, funcion)
    print(
        f"En [-1, 2], f(-1)={funcion(-1):.8f} y f(2)={funcion(2):.8f}. "
        "Biseccion no se puede aplicar con esos extremos porque no hay cambio de signo."
    )
    graficar("4. (x - 1)^2 + cos(2x)", funcion, (-1, 2), (-1, 2))


if __name__ == "__main__":
    main()
