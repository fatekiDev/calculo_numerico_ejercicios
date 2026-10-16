"""Ejercicio 2 de la guia 2: aproximaciones de exp(-5)."""

import math

from _metodos import error_porcentual


def main():
    valor_real = math.exp(-5)
    suma_directa = 0.0
    suma_exponencial = 0.0
    print("Aproximaciones de exp(-5), usando 20 terminos")
    print(" n       serie directa       error (%)       reciproco       error (%)")
    for i in range(20):
        suma_directa += (-5) ** i / math.factorial(i)
        suma_exponencial += 5**i / math.factorial(i)
        reciproco = 1 / suma_exponencial
        print(
            f"{i + 1:2d} {suma_directa:19.10g} "
            f"{error_porcentual(suma_directa, valor_real):13.6g} "
            f"{reciproco:17.10g} "
            f"{error_porcentual(reciproco, valor_real):13.6g}"
        )
    print(f"Valor de referencia exp(-5) = {valor_real:.12g}")


if __name__ == "__main__":
    main()
