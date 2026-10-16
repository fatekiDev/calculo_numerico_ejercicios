import math

valor_real = math.exp(-5)
valor_x = 5
terminos = 20
suma_1 = 0
suma_2 = 0

for i in range(terminos):
    termino_1 = ((-1) ** i) * (valor_x ** i) / math.factorial(i)
    suma_1 += termino_1

    termino_2 = (valor_x ** i) / math.factorial(i)
    suma_2 += termino_2
    resultado_2 = 1 / suma_2

    error_1 = abs((valor_real - suma_1) / valor_real) * 100
    error_2 = abs((valor_real - resultado_2) / valor_real) * 100

    print(f"Término {i + 1}:")
    print(f"  Método 1: {suma_1} | Error: {error_1}%")
    print(f"  Método 2: {resultado_2} | Error: {error_2}%")
