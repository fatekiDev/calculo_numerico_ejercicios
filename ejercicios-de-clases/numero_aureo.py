import math

numero_aureo = (1 + math.sqrt(5)) / 2

serie = [1, 1]
while (serie[-1] / serie[-2]) != numero_aureo:
    siguiente = serie[-1] + serie[-2]
    serie.append(siguiente)

limites = []
for i in range(1, len(serie)):
    limites.append(serie[i] / serie[i - 1])

print("Número áureo:", numero_aureo)
print("Secuencia:", serie)
print("Límites:", limites)
print("Aproximación final:", limites[-1])
