"""Ejercicio 4 de la guia 2: iteracion de Heron para raiz de 10."""

import math

from _metodos import error_porcentual


def heron(inicial, raiz, imprimir=False):
    actual = inicial
    anterior = None
    pasos = 0
    while True:
        actual = 0.5 * (actual + 10 / actual)
        pasos += 1
        error_aproximado = (
            abs((actual - anterior) / actual) * 100
            if anterior is not None
            else math.inf
        )
        if imprimir:
            error_verdadero = error_porcentual(actual, raiz)
            print(
                f"  paso {pasos}: x={actual:.12f}, "
                f"error verdadero={error_verdadero:.8g}%"
            )
        if error_aproximado < 0.5 * 10 ** (2 - 6):
            return actual, pasos
        anterior = actual


def main():
    raiz10 = math.sqrt(10)
    print("Ejercicio 4a: Heron desde x0=3, cuatro iteraciones")
    x_aprox = 3.0
    for paso in range(1, 5):
        x_aprox = 0.5 * (x_aprox + 10 / x_aprox)
        print(
            f"  paso {paso}: x={x_aprox:.12f}, "
            f"error verdadero={error_porcentual(x_aprox, raiz10):.8g}%"
        )
    _, pasos3 = heron(3, raiz10)
    _, pasos10 = heron(10, raiz10)
    print(
        "Ejercicio 4b-c: iteraciones para seis cifras correctas: "
        f"x0=3 -> {pasos3}; x0=10 -> {pasos10}"
    )


if __name__ == "__main__":
    main()
