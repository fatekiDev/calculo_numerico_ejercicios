"""Utilidades compartidas por los ejercicios de la guia 2."""

import struct


def precision_simple(valor):
    """Redondeo a IEEE-754 de 32 bits para imitar precision sencilla."""
    return struct.unpack("f", struct.pack("f", valor))[0]


def error_porcentual(aproximacion, verdadero):
    return abs((verdadero - aproximacion) / verdadero) * 100
