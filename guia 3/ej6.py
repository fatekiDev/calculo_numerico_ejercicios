"""Ejercicio 6 de la guia 3: eliminacion gaussiana."""

from _metodos import resolver_sistema


def main():
    print("Eliminacion gaussiana")
    print("m21=a21/a11, m31=a31/a11; se restan esos multiplos de la primera fila.")
    print("Luego m32=a'32/a'22 y se elimina x2 de la tercera fila.")
    print(
        "x3=b''3/a''33, x2=(b'2-a'23*x3)/a'22, "
        "x1=(b1-a12*x2-a13*x3)/a11."
    )
    print(
        "Se requieren pivotes no nulos (a11, a'22 y a''33). "
        "Si a11=0 se intercambian filas; si el pivote sigue siendo cero, "
        "el sistema no tiene solucion unica."
    )
    matriz = [[2, 1, -1], [-3, -1, 2], [-2, 2, 2]]
    terminos = [8, -11, -3]
    solucion = resolver_sistema(matriz, terminos)
    print(
        f"Para el sistema dado: x1={solucion[0]:.8g}, "
        f"x2={solucion[1]:.8g}, x3={solucion[2]:.8g}"
    )


if __name__ == "__main__":
    main()
