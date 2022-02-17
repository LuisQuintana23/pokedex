from random import randint

class Pokemon():

    def __init__(self, nombre, tipo, hp,ataque, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.__ataque = ataque
        self.__defensa = defensa
        self.__nivel = 0
        self.__xp = 0
        self.__vida = hp

        self.__last_game = False
        
        print(self.__str__())
    
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        self.__vida = valor

    def pelear(self, tipo_ataque, vida_enemigo):#
        
        
        #--------subir estadisticas y cambiar valor de self.__last_game

        pass
    
    
    def subir_experiencia(self):
        #comprobar si gano la batalla con self.__last_game
        pass

    
    def evolucionar(self):
        pass

    def __str__(self):
        return "Pokemon {} creado".format(self.nombre)
    

