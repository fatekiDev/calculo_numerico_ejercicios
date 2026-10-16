import numpy as np
import matplotlib.pyplot as plt


def funcion(valor_x):
    return np.sin(valor_x) - valor_x**2

x_valores = np.linspace(0, 1.2, 200)
y_valores = funcion(x_valores)

plt.figure(figsize=(8, 5))
plt.plot(x_valores, y_valores, label=r"f(x) = sin(x) - x^2", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Gráfica de la función")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()

limite_inferior = 0.5
limite_superior = 1.0
error_objetivo = 2.0
aprox_anterior = None
iteracion = 1

if funcion(limite_inferior) * funcion(limite_superior) < 0:
    while True:
        punto_medio = (limite_inferior + limite_superior) / 2

        if aprox_anterior is not None:
            error_aprox = abs((punto_medio - aprox_anterior) / punto_medio) * 100
        else:
            error_aprox = float('inf')

        print(f"Iteración {iteracion}: c = {punto_medio}, error = {error_aprox}%")

        if error_aprox < error_objetivo:
            print(f"Raíz obtenida: {punto_medio}")
            break

        if funcion(limite_inferior) * funcion(punto_medio) < 0:
            limite_superior = punto_medio
        else:
            limite_inferior = punto_medio

        aprox_anterior = punto_medio
        iteracion += 1
else:
    print("No hay cambio de signo en el intervalo.")
