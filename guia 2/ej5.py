"""Ejercicio 5 de la guia 2: serie alternada de ln(2)."""

import math


def main():
    ln2 = math.log(2)
    suma = 0.0
    terminos_objetivo = None
    print("Serie alternada de ln(2)")
    for n in range(1, 1_000_001):
        suma += (-1) ** (n + 1) / n
        error_absoluto = abs(ln2 - suma)
        if 4 <= n <= 8:
            error_relativo = error_absoluto / abs(ln2) * 100
            print(
                f"  S{n}={suma:.12f}, error absoluto={error_absoluto:.8g}, "
                f"error relativo={error_relativo:.8g}%"
            )
        if terminos_objetivo is None and 1 / (n + 1) < 1e-6:
            terminos_objetivo = n
            break
    print(
        f"  Terminos para garantizar error absoluto menor que 1e-6: "
        f"{terminos_objetivo} (cota 1/(n+1))"
    )


if __name__ == "__main__":
    main()
