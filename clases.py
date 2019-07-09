class Objetos:
    pass

class Inanimados(Objetos):
    pass

class Animados(Objetos):
    pass

class Edificios(Inanimados):
    pass

class Casas(Edificios):
    pass

class Animales():

    def respirar(self):
        print("respirando")

    def mover(self):
        print("moviendose")
    
    def comer(self):
        print("comiendose")
    
class Mamiferos(Animales):
    def alimentan_crias_con_leche(self):
        pass
    
class Primates(Mamiferos):
    def tienen_manos_prensiles(self):
        pass

class Humanos(Primates):
    pass

class Reptiles(Animales):
    def tienen_sangre_fria(self):
        print("sangre fria")

class Tortugas(Reptiles):

    def __init__(self, edad):
        self.tortuga_edad = edad
    
    def ponen_huevos(self):
        print("pone huevos")

    def encontrar_comida( self ):
        self.mover()
        print( "¡he encontrado comida!" )
        self.comer()

    def reproducir( self ):
        self.mover()
        print( "¡Se esta moviendo!" )

        self.ponen_huevos()
        print( "¡Puso unos huevos!" )

    def bailar( self ):
        self.mover()
        print( "¡Baila!" )

        self.mover()
        print( "¡Sigue Bailando!" )

        self.mover()
        print( "¡No para de Bailar!" )


