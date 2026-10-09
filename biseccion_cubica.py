import matplotlib.pyplot as plt
import numpy as np

def funcion_polinomio(valor_x):
    return 5 * (valor_x**3) - 5 * (valor_x**2) + 6 * valor_x - 2

valores_x = np.linspace(-0.5, 1.5, 100)
valores_y = funcion_polinomio(valores_x)

plt.figure(figsize=(8, 5))
plt.plot(valores_x, valores_y, label="Función cúbica", color="blue", lw=2)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.title("Gráfica de la función cúbica")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.show()

print("=== BISECCIÓN - POLINOMIO CÚBICO ===")
limite_bajo = float(input("Ingrese límite inferior: "))
limite_alto = float(input("Ingrese límite superior: "))
error_objetivo = 10.0

aprox_anterior = None

if funcion_polinomio(limite_bajo) * funcion_polinomio(limite_alto) < 0:
    print(f"\nBuscando raíz con error menor al {error_objetivo}%\n")
    
    iteracion = 1
    while True:
        punto_central = (limite_bajo + limite_alto) / 2
        
        if aprox_anterior is not None:
            error_relativo = abs((punto_central - aprox_anterior) / punto_central) * 100
        else:
            error_relativo = float('inf')
        
        print(f"Iteración {iteracion}:")
        print(f"  Intervalo: [{limite_bajo:.6f}, {limite_alto:.6f}]")
        print(f"  Punto central: {punto_central:.6f}")
        print(f"  f(c): {funcion_polinomio(punto_central):.6f}")
        print(f"  Error relativo: {error_relativo:.6f}%\n")
        
        if error_relativo < error_objetivo:
            print(f"Raíz encontrada: {punto_central:.6f}")
            break
        
        if funcion_polinomio(limite_bajo) * funcion_polinomio(punto_central) < 0:
            limite_alto = punto_central
        else:
            limite_bajo = punto_central
        
        aprox_anterior = punto_central
        iteracion += 1
else:
    print("No hay cambio de signo en el intervalo.")
