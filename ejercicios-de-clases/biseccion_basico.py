import matplotlib.pyplot as plt
import numpy as np

def funcion_ejemplo(valor_x):
    return -0.5 * (valor_x**2) + 2.5 * valor_x + 4.5

valores_x = np.linspace(-2, 7, 100)
valores_y = funcion_ejemplo(valores_x)

plt.figure(figsize=(8, 5))
plt.plot(valores_x, valores_y, label="Función cuadrática", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Gráfica de la función")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()

print("=== MÉTODO DE BISECCIÓN ===")
limite_bajo = float(input("Ingrese límite inferior: "))
limite_alto = float(input("Ingrese límite superior: "))

if funcion_ejemplo(limite_bajo) * funcion_ejemplo(limite_alto) < 0:
    print("\nCondición cumplida: hay cambio de signo.\n")
    
    for iteracion in range(10):
        punto_central = (limite_bajo + limite_alto) / 2
        valor_central = funcion_ejemplo(punto_central)
        error_calc = abs((limite_bajo - limite_alto) / (limite_bajo + limite_alto)) if (limite_bajo + limite_alto) != 0 else float('inf')
        
        print(f"Iteración {iteracion + 1}:")
        print(f"  Intervalo: [{limite_bajo:.6f}, {limite_alto:.6f}]")
        print(f"  Punto medio: {punto_central:.6f}")
        print(f"  f(punto_medio): {valor_central:.6f}")
        print(f"  Error: {error_calc:.6f}\n")
        
        if valor_central == 0:
            print(f"Raíz exacta encontrada: {punto_central}")
            break
        elif funcion_ejemplo(limite_bajo) * valor_central < 0:
            limite_alto = punto_central
        else:
            limite_bajo = punto_central
else:
    print("No hay cambio de signo. Intenta con otros valores.")
