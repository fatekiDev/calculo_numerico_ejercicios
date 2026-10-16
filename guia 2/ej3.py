"""Ejercicio 3 de la guia 2: serie de Maclaurin para cos(0.3*pi)."""

import math

from _metodos import error_porcentual


def main():
    x = 0.3 * math.pi
    verdadero = math.cos(x)
    tolerancia_porcentual = 0.5 * 10 ** (2 - 8)
    suma = 0.0
    termino = 1.0
    numero = 0
    while True:
        suma += termino
        numero += 1
        error = error_porcentual(suma, verdadero)
        print(
            f"Termino {numero:2d}, cos({x:.8f}) ~= "
            f"{suma:.12f}, error verdadero={error:.8g}%"
        )
        if error < tolerancia_porcentual:
            break
        termino *= -(x**2) / ((2 * numero - 1) * (2 * numero))
    print(f"Terminos para ocho cifras significativas: {numero}")


if __name__ == "__main__":
    main()
