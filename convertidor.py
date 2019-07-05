import math

def convertir_a_millas(kms):
    '''(number) -> number
    Devuelve el número de millas equivalente a los kms pasados.
    >>>convertir_a_millas(34)
    19
    >>>convertir_a_millas(234)
    146
    '''
    mil = kms * 0.62137
    return mil

def diagonal_rectangulo(ancho,alto):

    suma_cuadrados = (ancho**2) + (alto**2)
    diagonal = math.sqrt(suma_cuadrados)
    return diagonal
