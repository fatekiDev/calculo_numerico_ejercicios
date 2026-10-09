import numpy as np
import matplotlib.pyplot as plt


def funcion(valor_x):
    return (0.8 - 0.3 * valor_x) / valor_x

valor_verdadero = 0.8 / 0.3
print(f"Valor real: {valor_verdadero}")

x_valores = np.linspace(0.5, 4.0, 200)
y_valores = funcion(x_valores)

plt.figure(figsize=(8, 5))
plt.plot(x_valores, y_valores, label="f(x) = (0.8 - 0.3x) / x", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Gráfica de la función")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()

limite_inferior = 1.0
limite_superior = 3.0
aprox_anterior = None

if funcion(limite_inferior) * funcion(limite_superior) < 0:
    for iteracion in range(1, 4):
        punto_corte = limite_superior - (funcion(limite_superior) * (limite_inferior - limite_superior)) / (funcion(limite_inferior) - funcion(limite_superior))

        if aprox_anterior is not None:
            error_aprox = abs((punto_corte - aprox_anterior) / punto_corte) * 100
        else:
            error_aprox = float('inf')

        error_verdadero = abs((valor_verdadero - punto_corte) / valor_verdadero) * 100

        print(f"Iteración {iteracion}: c = {punto_corte}")
        print(f"  Error aproximado: {error_aprox}%")
        print(f"  Error verdadero: {error_verdadero}%")

        if funcion(limite_inferior) * funcion(punto_corte) < 0:
            limite_superior = punto_corte
        else:
            limite_inferior = punto_corte

        aprox_anterior = punto_corte
else:
    print("No hay cambio de signo.")
