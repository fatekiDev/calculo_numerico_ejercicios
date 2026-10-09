def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True


valor = int(input("Ingrese un número: "))
if es_primo(valor):
    print("El número es primo")
else:
    print("El número no es primo")
