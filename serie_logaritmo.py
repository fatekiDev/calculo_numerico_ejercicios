import math

valor_real = 0.69314718056
suma = 0.0
termino = 1
n = 1

while True:
    termino = ((-1) ** (n + 1)) / n
    suma += termino
    error_absoluto = abs(valor_real - suma)
    if error_absoluto < 1e-6:
        break
    n += 1

print(f"Número de términos necesarios: {n}")
print(f"Suma final: {suma}")
print(f"Error absoluto: {error_absoluto}")
