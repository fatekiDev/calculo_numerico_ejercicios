"""Ejercicio 1 de la guia 2: suma de 1/n^4 en precision sencilla."""

import math

from _metodos import error_porcentual, precision_simple


def suma_potencia_cuarta(cantidad, inversa=False):
    suma = precision_simple(0.0)
    indices = range(cantidad, 0, -1) if inversa else range(1, cantidad + 1)
    for indice in indices:
        suma = precision_simple(suma + precision_simple(1.0 / indice**4))
    return suma


def main():
    verdadero = math.pi**4 / 90
    print("Suma de 1/n^4 en precision sencilla")
    for cantidad in (10_000, 100_000):
        for inversa in (False, True):
            aproximacion = suma_potencia_cuarta(cantidad, inversa)
            sentido = "de mayor a menor" if inversa else "de menor a mayor"
            error = error_porcentual(aproximacion, verdadero)
            print(
                f"N={cantidad:6d}, {sentido:17s}: "
                f"{aproximacion:.10f}, error={error:.8g}%"
            )


if __name__ == "__main__":
    main()
