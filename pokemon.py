from multiprocessing.sharedctypes import Value
from random import randint, choice, uniform
from matplotlib.pyplot import hist
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

    def barra_vida(self, vida, vida_maxima, divisiones):
        convertir_divisiones = int(vida_maxima/divisiones)
        divisones_actuales = int(vida/convertir_divisiones)
        vida_restante = divisiones - divisones_actuales

        vida_pantalla = "-" * divisones_actuales
        restante_pantalla = ' ' * vida_restante

        print("|" + vida_pantalla + restante_pantalla + "|")

    
    #def pelear(self, tipo_ataque, vida_enemigo):#
    def pelear(self):
        print(f"Has seleccionado a {self.nombre}")
        self.almacenar_oponentes()
        print(f"Tu oponentes es {self.oponente}\n")
        batalla = True
        #Almacenamiento de vida maxima de cada pokemon        
        vida_max = self.vida#se almacena ya que self.vida estará cambiando
        op_vida_max = self.op_vida

        sleep(3)
        print("COMIENZA LA BATALLA".center(50, "-"))#agrega giones al inicio y final de la cadena
        print("\n")
        while batalla:
            #MUESTRA LA VIDA DE AMBOS POKEMONES
            print(f"\t{self.nombre}")
            self.barra_vida(self.vida, vida_max, 20)
            print(f"Vida: {round(self.vida, 2)}\n")

            print(f"\t{self.oponente}")
            self.barra_vida(self.op_vida, op_vida_max, 15)#se coloca 15, ya que la barra de oponente se coloca mas grande
            print(f"Vida: {round(self.op_vida, 2)}\n")
            


            bucle_eleccion = True
            while bucle_eleccion:
                try:
                    t_ataque = int(input(f"\nSelecciona el tipo de ataque de {self.nombre}\n\n1.-Fuerte\n2.-Medio\n3.-Bajo\n>>> "))
                    dano = 0
                    #el usuario debera seleccionar entre realizar estos 3 ataques, entre mas fuerte sea
                    #menor posibilidad de ocasior buen daño
                    if t_ataque == 1:
                        print("Ataque fuerte")
                        #se tiene menos probabilidad de realizar un ataque fuerte o critico
                        dano = round(uniform(self.ataque*0.18, self.ataque), 1)#uniform permite obtener numero random de floats
                        #rounde redondea un numero a los decimales especificados en el segundo parametro
                        bucle_eleccion = False
                    elif t_ataque == 2:
                        print("Ataque medio")
                        dano = round(uniform(self.ataque*0.32, self.ataque*0.5), 1)#se multiplica por un decimal, para obtener un porcentaje del ataque
                        #la multiplicacion por decimal se hizo, porque no todos los pokemones tienen el mismo daño
                        bucle_eleccion = False
                    elif t_ataque == 3:#se hara un ataque bajo
                        print("Ataque bajo")
                        dano = round(self.ataque*0.34, 1)
                        bucle_eleccion = False
                    else:
                        raise ValueError
                except ValueError:
                    print("\nOpcion no valida\n")

            print(f"\nPotencia de ataque: {dano}")
            escudo = round(uniform(self.defensa*0.1, dano*0.8))#entre mayor sea el numero de la defensa, menor será el daño
            #se coloca como maximo self.dano, ya que esto signifiria que el escudo neutralizo el daño hasta un 80%
            dano = round(dano - escudo)#se actualiza el daño total hecho

            print(f"\nDaño ocasionado: {dano}")
            self.op_vida -= dano


            sleep(2)
            #se verificara que no se haya derrotado el pokemon
            if self.op_vida <= 0:
                print(f"\nHas derrotado a {self.oponente}")
                self.modificar_stats(True)#False es porque perdio
                batalla = False
            else:
                print(f"\nTurno de {self.oponente}")
                sleep(2)

                op_dano = round(uniform(5, self.op_ataque))

                print(f"\n{self.oponente} lanzo un golpe de {op_dano} de poder")
                sleep(2)

                escudo_poke = round(uniform(self.op_defensa*0.1, op_dano*0.8))#entre mayor sea el numero de la defensa, menor será el daño
                op_dano = (op_dano - escudo_poke)

                self.vida -= op_dano
                print(f"\nHas recibido {op_dano} de daño\n")

                if self.vida <= 0:
                    print("\nHan derrotado a tu pokemon\n")
                    self.modificar_stats(False)#False es porque perdio
                    batalla = False
        

        
    def guardar_historial(self, contenido):
        ruta = "./data/historial.json"
        #almacena todo los datos de la batalla actual
        stats = contenido[self.nombre]
        ataque = stats['ataque']
        vida = stats['vida']
        exp = stats['exp']
        defensa = stats['defensa']
        nivel = stats['nivel']

        #carga el archivo
        with open(ruta, 'r') as file:
            historial = json.load(file)

        #escribe el archivo
        with open(ruta, 'w') as file:
            historial[self.nombre]['ataque'].append(ataque)
            historial[self.nombre]['defensa'].append(defensa)
            historial[self.nombre]['vida'].append(vida)
            historial[self.nombre]['exp'].append(exp)
            historial[self.nombre]['nivel'].append(nivel)

            json.dump(historial, file, indent=4, sort_keys=True)
            print('\nDatos guardados con exito.\n')

    
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

        self.guardar_historial(contenido)

        with open("./data/pokebolas.json", "w") as file:#guarda el archivo json con los cambios
            json.dump(contenido, file, indent=4, sort_keys=True)


    # Al finalizar el programa automaticamente se ejecuta este metodo

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
        historial_poke = {
            'vida':[self.vida],
            'ataque':[self.ataque],
            'defensa':[self.defensa],
            'nivel':[self.nivel],
            'exp':[self.xp]
        }
        # En un diccionario se guardan todos los datos del pokemon
        # los datos int no se pueden escribir en un json, por lo que son pasados
        # a str
        #creara el historia con los valores iniciales

        guardarJson(self.nombre, pokemon_dict)
        crearHistoriaL(self.nombre, historial_poke)

if "__main__" == __name__:
    batalla_pokemon = Pokemon("Bulbasaur", "Electric", 49, 45, 49, 0, 0)
    batalla_pokemon.pelear()