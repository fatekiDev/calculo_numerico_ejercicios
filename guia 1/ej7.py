"""Ejercicio 7 de la guia 1: falsa posicion para una raiz analitica."""

from _metodos import falsa_posicion, graficar, mostrar_filas


def main():
    funcion = lambda x: (0.8 - 0.3 * x) / x
    raiz = 0.8 / 0.3
    print(f"Raiz analitica = {raiz:.10f}")
    mostrar_filas(
        "Tres iteraciones de falsa posicion desde [1, 3]",
        falsa_posicion(funcion, 1, 3, max_iter=3),
        funcion,
        raiz,
    )
    graficar("7. (0.8 - 0.3x) / x", funcion, (0.5, 4))


if __name__ == "__main__":
    main()
