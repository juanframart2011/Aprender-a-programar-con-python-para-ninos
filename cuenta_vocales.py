def cuenta_vocales(text):

    contador = 0
    for letra in text:
        if letra in "aeiou":
            contador = contador + 1

    return contador            

def vocales_return(text):

    contador = ""
    for letra in text:
        if letra in "aeiou":
            contador = contador + " " + letra

    return contador

def vocal_para( txt ):

    i = 0
    while i < len( txt ) and not (txt[i] in "aeiouAEIOU"):

        print( txt[i] )
        i = i + 1

    return "termino"

def letras_sin_vocal( txt ):

    letras = ""
    i = 0
    while i < len( txt ) and not (txt[i] in "aeiouAEIOU"):

        letras = txt[i] + " " + letras
        i = i + 1

    return letras

def obtener_respuesta( pregunta ):
    
    respuesta = input(pregunta)
    while not(respuesta == "si" or respuesta == "no" or respuesta == "sí"):
        respuesta = input(pregunta)
    return respuesta
