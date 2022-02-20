from random import randint, choice, random
import pandas as pd
import numpy as np
from funciones_generales.archivos import *
from time import sleep
from os import system
import json

from funciones_generales.archivos import guardarJson

class Pokemon():

    def __init__(self, nombre, tipo, hp,ataque, defensa, nivel = 0, xp = 0):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = int(hp)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.nivel = int(nivel)
        self.xp = int(xp)

        self.oponente = ""#nombre oponente
        self.op_vida = 0
        self.op_ataque = 0
        self.op_defensa = 0
    


    def almacenar_oponentes(self):
        datos_pokemones = cargarJsonTodos()#almacena nombre es una lista
        nombres = list(datos_pokemones.keys())
        ##----proceso para seleccion de oponente aleatoria
        self.oponente = choice(nombres)#da un nombre aleatorio
        self.op_vida = datos_pokemones[self.oponente]["HP"]
        self.op_ataque = datos_pokemones[self.oponente]["Attack"]
        self.op_defensa = datos_pokemones[self.oponente]["Defense"]
    
    #def pelear(self, tipo_ataque, vida_enemigo):#
    def pelear(self):

        print(f"Has seleccionado a {self.nombre}")
        self.almacenar_oponentes()
        print(f"Tu oponentes es {self.oponente}")
        batalla = True
        sleep(3)
        print("COMIENZA LA BATALLA")
        while batalla:
            print(f"\t{self.nombre}")
            print(f"Vida: {self.vida}\n")

            print(f"\t{self.oponente}")
            print(f"Vida: {self.op_vida}\n")
            t_ataque = int(input(f"\nSelecciona el tipo de ataque de {self.nombre}\n1.-Fuerte\n2.-Medio\n3.-Bajo\n>> "))
            dano = 0
            if t_ataque == 1:
                print("Ataque fuerte")
                #se tiene menos probabilidad de realizar un ataque fuerte o critico
                dano = randint(self.ataque-30, self.ataque)
            elif t_ataque == 2:
                print("Ataque medio")
                dano = randint(self.ataque-20, self.ataque-15)
            elif t_ataque == 3:#se hara un ataque bajo
                print("Ataque bajo")
                dano = randint(self.ataque-22, self.ataque-20)
            else:
                print("Opcion no valida")
            print(f"\nDaño ocasionado: {dano}")
            self.op_vida -= dano
            sleep(2)
            #se verificara que no se haya derrotado el pokemon
            if self.op_vida <= 0:
                print("Has derrotado a tu oponente")
                self.modificar_stats(True)#False es porque perdio
                batalla = False
            else:
                print(f"Turno de {self.oponente}")
                sleep(2)
                op_dano = randint(5, self.op_ataque)
                print(f"\n{self.oponente} te ha ocasionado {op_dano} de daño")
                self.vida -= op_dano
                if self.vida <= 0:
                    print("Han derrotado a tu pokemon\n")
                    self.modificar_stats(False)#False es porque perdio
                    batalla = False
        

        
    
    
    def modificar_stats(self, win):
        with open("./data/pokebolas.json") as file:
            contenido = json.load(file)

        if win == True:#en caso de que el pokemon gane
            contenido[self.nombre]["exp"] += 30#suma 30 de experiencia
            
        else:#en caso de que pierda
            contenido[self.nombre]["exp"] += 10#suma 10 de experiencia

        ##PROCESO DE SUBIR NIVEL
        if contenido[self.nombre]["exp"] >= 60*(contenido[self.nombre]["nivel"]+1):
            """""
            Supongamos que el nivel es 0, se suma uno y se multiplica por 60
            por lo tanto, se debera alcanzar una experiencia de 60 para subir al primer nivel,
            y un experiencia de 120 para subir al segundo
            """
            contenido[self.nombre]["nivel"] += 1
            contenido[self.nombre]["ataque"] += 5
            contenido[self.nombre]["defensa"] += 5
            contenido[self.nombre]["vida"] += 7
            print("\n\n")
            print("HAS SUBIDO DE NIVEL".center(50, "/"))
            print("\nNivel actual: {}\nAtaque: +5\nDefensa: +5\nVida: +7\n".format(contenido[self.nombre]["nivel"]))


        with open("./data/pokebolas.json", "w") as file:#guarda el archivo json con los cambios
            json.dump(contenido, file, indent=4, sort_keys=True)



    
    def evolucionar(self):
        pass

    def __str__(self):
        pass
    
    # Al finalizar el programa automaticamente se ejecuta este metodo
    """def __del__(self):
        datos = {
            'nombre':self.nombre,
            'tipo':self.tipo,
            'vida':int(self.vida),
            'ataque':int(self.ataque),
            'defensa':int(self.defensa),
            'nivel':int(self.nivel),
            'exp':int(self.xp)
        }
        # En un diccionario se guardan todos los datos del pokemon
        # los datos int no se pueden escribir en un json, por lo que son pasados
        # a str
        guardarJson(self.nombre, datos)
        # Se ejecuta la funcion para poder guardar todos los archivos a json
    """

    def guardarPokemon(self):
        pokemon_dict = {
            'nombre':self.nombre,
            'tipo':self.tipo,
            'vida':int(self.vida),
            'ataque':int(self.ataque),
            'defensa':int(self.defensa),
            'nivel':int(self.nivel),
            'exp':int(self.xp)
        }
        # En un diccionario se guardan todos los datos del pokemon
        # los datos int no se pueden escribir en un json, por lo que son pasados
        # a str
        guardarJson(self.nombre, pokemon_dict)

if "__main__" == __name__:
    batalla_pokemon = Pokemon("Bulbasaur", "Electric", 49, 45, 49, 0, 0)
    batalla_pokemon.pelear()