"""Metodos numericos y utilidades compartidas por los ejercicios de la guia 1."""

import math

import matplotlib.pyplot as plt


def bisecar(funcion, inferior, superior, tolerancia=None, max_iter=100):
    """Devuelve una fila por iteracion: numero, punto medio, error aproximado."""
    filas = []
    anterior = None
    f_inferior = funcion(inferior)
    f_superior = funcion(superior)
    if f_inferior * f_superior > 0:
        raise ValueError("El intervalo no tiene cambio de signo.")

    for numero in range(1, max_iter + 1):
        medio = (inferior + superior) / 2
        error = (
            abs((medio - anterior) / medio) * 100
            if anterior is not None and medio != 0
            else math.inf
        )
        filas.append((numero, medio, error))
        f_medio = funcion(medio)
        if f_medio == 0 or (tolerancia is not None and error < tolerancia):
            break
        if f_inferior * f_medio < 0:
            superior = medio
            f_superior = f_medio
        else:
            inferior = medio
            f_inferior = f_medio
        anterior = medio
    return filas


def falsa_posicion(funcion, inferior, superior, tolerancia=None, max_iter=100):
    filas = []
    anterior = None
    f_inferior = funcion(inferior)
    f_superior = funcion(superior)
    if f_inferior * f_superior > 0:
        raise ValueError("El intervalo no tiene cambio de signo.")

    for numero in range(1, max_iter + 1):
        corte = superior - f_superior * (inferior - superior) / (
            f_inferior - f_superior
        )
        error = (
            abs((corte - anterior) / corte) * 100
            if anterior is not None and corte != 0
            else math.inf
        )
        filas.append((numero, corte, error))
        f_corte = funcion(corte)
        if f_corte == 0 or (tolerancia is not None and error < tolerancia):
            break
        if f_inferior * f_corte < 0:
            superior, f_superior = corte, f_corte
        else:
            inferior, f_inferior = corte, f_corte
        anterior = corte
    return filas


def mostrar_filas(titulo, filas, funcion, raiz_real=None):
    print(f"\n{titulo}")
    print("iteracion       aproximacion       f(x)        error aprox. (%)")
    for numero, aproximacion, error in filas:
        error_texto = "n/a" if math.isinf(error) else f"{error:.6f}"
        print(
            f"{numero:9d} {aproximacion:18.10f} "
            f"{funcion(aproximacion):12.5g} {error_texto:>18}"
        )
    if raiz_real is not None and filas:
        aproximacion = filas[-1][1]
        error_verdadero = abs((raiz_real - aproximacion) / raiz_real) * 100
        print(f"Error verdadero de la ultima aproximacion: {error_verdadero:.8f}%")


def graficar(titulo, funcion, limites):
    figura, eje = plt.subplots(figsize=(7, 5))
    xs = [limites[0] + i * (limites[1] - limites[0]) / 500 for i in range(501)]
    eje.plot(xs, [funcion(x) for x in xs], label="f(x)")
    eje.axhline(0, color="black", linewidth=0.8)
    eje.axvline(0, color="black", linewidth=0.6, linestyle=":")
    eje.set_title(titulo)
    eje.grid(True, linestyle=":", alpha=0.6)
    eje.legend()
    figura.tight_layout()
    plt.show()
