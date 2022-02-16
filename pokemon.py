from random import randint
class Pokemon():
    def __init__(self):
        self.nombre = ""
        self.tipo = ""
        self.__ataque = 0
        self.__defensa = 0
        self.__nivel = 0
        self.__xp = 0
        self.__vida = 0

        self.__last_game = False

    
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

