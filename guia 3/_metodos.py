"""Metodos numericos y utilidades compartidas por los ejercicios de la guia 3."""

import math

import matplotlib.pyplot as plt


def error_aproximado(actual, anterior):
    if anterior is None or actual == 0:
        return math.inf
    return abs((actual - anterior) / actual) * 100


def newton(funcion, derivada, inicial, tolerancia=None, iteraciones=100):
    filas = []
    actual = inicial
    anterior = None
    for numero in range(1, iteraciones + 1):
        valor_derivada = derivada(actual)
        if abs(valor_derivada) < 1e-14:
            raise ZeroDivisionError(f"Derivada demasiado cercana a cero en x={actual}.")
        siguiente = actual - funcion(actual) / valor_derivada
        error = error_aproximado(siguiente, actual)
        filas.append((numero, siguiente, error))
        if tolerancia is not None and error < tolerancia:
            break
        anterior, actual = actual, siguiente
    return filas


def biseccion(funcion, inferior, superior, tolerancia=0.05, max_iter=500):
    f_inferior = funcion(inferior)
    if f_inferior * funcion(superior) > 0:
        raise ValueError("El intervalo no tiene cambio de signo.")
    filas = []
    anterior = None
    for numero in range(1, max_iter + 1):
        medio = (inferior + superior) / 2
        error = error_aproximado(medio, anterior)
        filas.append((numero, medio, error))
        f_medio = funcion(medio)
        if f_medio == 0 or error < tolerancia:
            break
        if f_inferior * f_medio < 0:
            superior = medio
        else:
            inferior, f_inferior = medio, f_medio
        anterior = medio
    return filas


def imprimir_iteraciones(titulo, filas, funcion=None):
    print(f"\n{titulo}")
    print("iteracion       aproximacion       f(x)        error aprox. (%)")
    for numero, aproximacion, error in filas:
        valor = funcion(aproximacion) if funcion else float("nan")
        texto_error = "n/a" if math.isinf(error) else f"{error:.8g}"
        print(
            f"{numero:9d} {aproximacion:18.10f} "
            f"{valor:12.5g} {texto_error:>18}"
        )


def cifras_significativas(error_porcentual):
    cifras = 0
    for cantidad in range(1, 16):
        limite = 0.5 * 10 ** (2 - cantidad)
        if error_porcentual <= limite:
            cifras = cantidad
        else:
            break
    return cifras


def resolver_sistema(matriz, terminos):
    a = [fila[:] + [termino] for fila, termino in zip(matriz, terminos)]
    n = len(a)
    for columna in range(n):
        fila_pivote = max(range(columna, n), key=lambda fila: abs(a[fila][columna]))
        if abs(a[fila_pivote][columna]) < 1e-14:
            raise ValueError("El sistema no tiene una solucion unica.")
        a[columna], a[fila_pivote] = a[fila_pivote], a[columna]
        for fila in range(columna + 1, n):
            multiplicador = a[fila][columna] / a[columna][columna]
            for j in range(columna, n + 1):
                a[fila][j] -= multiplicador * a[columna][j]

    solucion = [0.0] * n
    for i in range(n - 1, -1, -1):
        restante = a[i][n] - sum(a[i][j] * solucion[j] for j in range(i + 1, n))
        solucion[i] = restante / a[i][i]
    return solucion


def graficar(titulo, funcion, limites, intervalo=None):
    figura, eje = plt.subplots(figsize=(7, 4.5))
    xs = [limites[0] + i * (limites[1] - limites[0]) / 600 for i in range(601)]
    eje.plot(xs, [funcion(x) for x in xs], label="f(x)")
    eje.axhline(0, color="black", linewidth=0.8)
    if intervalo is not None:
        eje.axvline(intervalo[0], color="gray", linestyle=":")
        eje.axvline(intervalo[1], color="gray", linestyle=":")
    eje.set_title(titulo)
    eje.grid(True, linestyle=":", alpha=0.6)
    eje.legend()
    figura.tight_layout()
    plt.show()
