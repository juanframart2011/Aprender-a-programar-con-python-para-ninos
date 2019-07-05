'''verde = True
if verde:
    print("¡Puedes pasar!")
else:
    print("¡Espera!")

semaforo_verde = False
semaforo_naranja = True

if semaforo_verde:
    print("¡Puedes pasar!")
else:
    if semaforo_verde:
        print("¡Pasa con precaución!")
    else:
        print("Debes Espera")

color = "verde"

if color == "rojo":
    
    print("¡Espera!")
elif color == "naranja":

    print("¡Pasa con precaución!")
else:

    print("Adelante")'''

def estado_agua( temperatura ):
    '''(num) -> string
    función que determina el estado del agua en base a la temperatura
    en la que se encuentra:
    (-12) -> "estado del agua: solido"
    (95) -> "estado del agua: liquido"
    (129) -> "estado del agua: gaseoso"
    (hola pepe) -> "estado indeterminado, temperatura no válida"
    '''

    if(type(temperatura) == int or type(temperatura) == float):
        if temperatura <= 0:
            return "estado del agua: solido"
        elif(temperatura > 0) and (temperatura <= 100):
            return "estado del agua: gaseoso"
        elif temperatura > 100:
            return "estado del agua:gaseoso"
    else:
        return "estado indeterminado"
            
    
