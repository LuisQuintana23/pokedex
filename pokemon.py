from random import randint

from archivos import guardarJson

class Pokemon():

    def __init__(self, nombre, tipo, hp,ataque, defensa, nivel = 0, xp = 0):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = hp
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.xp = xp

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

    def __str__(self):
        pass
    
    # Al finalizar el programa automaticamente se ejecuta este metodo
    def __del__(self):
        datos = {
            'nombre':self.nombre,
            'tipo':self.tipo,
            'vida':str(self.vida),
            'ataque':str(self.ataque),
            'defensa':str(self.defensa),
            'nivel':str(self.nivel),
            'exp':str(self.xp)
        }
        # En un diccionario se guardan todos los datos del pokemon
        # los datos int no se pueden escribir en un json, por lo que son pasados
        # a str
        guardarJson(self.nombre, datos)
        # Se ejecuta la funcion para poder guardar todos los archivos a json

