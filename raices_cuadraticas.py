import math


def formula_general(a, b, c):
    discriminante = b**2 - 4 * a * c
    if discriminante >= 0:
        raiz_1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz_2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return raiz_1, raiz_2
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * a)
        return complex(parte_real, parte_imaginaria), complex(parte_real, -parte_imaginaria)


print("=== Resolución de ecuación de segundo grado ===")
a = float(input("Ingrese A: "))
b = float(input("Ingrese B: "))
c = float(input("Ingrese C: "))

raices = formula_general(a, b, c)
print("Raíces:", raices)
