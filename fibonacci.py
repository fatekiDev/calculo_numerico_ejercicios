def generar_fibonacci(cantidad):
    secuencia = [1, 1]
    while len(secuencia) < cantidad:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia


def calcular_limites(secuencia):
    limites = []
    for i in range(1, len(secuencia)):
        limites.append(secuencia[i] / secuencia[i - 1])
    return limites


cantidad = 10
serie = generar_fibonacci(cantidad)
limites = calcular_limites(serie)

print("Secuencia de Fibonacci:")
print(serie)
print("\nLímites:")
print(limites)
print(f"\nAproximación final: {limites[-1]}")
