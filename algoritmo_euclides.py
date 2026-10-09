print("=== ALGORITMO DE EUCLIDES ===")
print("Encuentra el MCD y MCM de dos números\n")

num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

residue_actual = mayor % menor
residue_anterior = menor
iterado = True

print(f"\nProceso:\n")

while iterado:
    if residue_actual == 0:
        mcd_resultado = residue_anterior
        iterado = False
        print(f"Residuo final: {residue_actual} → MCD = {mcd_resultado}")
    else:
        print(f"residue_anterior = {residue_anterior}, residue_actual = {residue_actual}")
        residue_anterior = residue_actual
        residue_actual = menor % residue_anterior
        menor = residue_anterior

mcm_resultado = (num1 * num2) // mcd_resultado

print(f"\n=== RESULTADOS ===")
print(f"MCD: {mcd_resultado}")
print(f"MCM: {mcm_resultado}")
