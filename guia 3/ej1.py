"""Ejercicio 1 de la guia 3: Newton para la raiz cubica de 20."""

import math

from _metodos import cifras_significativas, imprimir_iteraciones, newton


def main():
    funcion = lambda x: x**3 - 20
    derivada = lambda x: 3 * x**2
    filas = newton(funcion, derivada, 3, tolerancia=0.005)
    imprimir_iteraciones("Raiz cubica de 20", filas, funcion)
    raiz = math.pow(20, 1 / 3)
    for numero, aproximacion, _ in filas:
        error_verdadero = abs((raiz - aproximacion) / raiz) * 100
        print(f"  iteracion {numero}: error relativo verdadero={error_verdadero:.8g}%")
    print(f"Cifras significativas garantizadas por el criterio: {cifras_significativas(0.005)}")


if __name__ == "__main__":
    main()
