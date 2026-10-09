import math

valor_x = 0.3 * math.pi
terminos = 0
suma = 0
suma_anterior = 0
error_actual = 100
cifras = 8
error_objetivo = 0.5 * (10 ** (2 - cifras))

print(f"Meta de error: {error_objetivo}%")

while error_actual > error_objetivo:
    termino = ((-1) ** terminos) * (valor_x ** (2 * terminos)) / math.factorial(2 * terminos)
    suma_anterior = suma
    suma += termino

    if terminos > 0:
        error_actual = abs((suma - suma_anterior) / suma) * 100

    terminos += 1

print(f"Número de términos: {terminos}")
print(f"Aproximación: {suma}")
print(f"Valor real: {math.cos(valor_x)}")
print(f"Error final: {error_actual}%")
