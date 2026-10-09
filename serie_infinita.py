import math

n = int(input("Ingrese el número de términos: "))
resultado = 0
for i in range(1, n + 1):
    resultado += 1 / (i ** 4)

constante = (math.pi ** 4) / 90
error_absoluto = abs(constante - resultado)
error_relativo = error_absoluto / constante
error_porcentual = error_relativo * 100

print(f"Suma parcial: {resultado}")
print(f"Constante: {constante}")
print(f"Error absoluto: {error_absoluto}")
print(f"Error relativo: {error_relativo}")
print(f"Error porcentual: {error_porcentual}%")
