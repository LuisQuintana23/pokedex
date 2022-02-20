from funciones_generales.archivos import *
from funciones_generales.funciones import *
from funciones_generales.excepciones import *
from pokemon import *
import os

global pokemones, pokebolas
pokedex = cargarPokedex() # Carga los datos generales de los pokemones
pokebolas = cargarJson() # Carga los pokemones y datos que el usuario tiene
# si el usuario no tiene pokemones registrados, pokebolas estará vacio

pokemones = {}
# En este diccionario se guarda los 'objetos' de los pokemones ya creados y por crear
# tiene como clave el nombre del pokemon
if pokebolas: # Si hay pokemones previamente creados y cargados en el json
    for pokemon,stats in pokebolas.items(): # Itera sobre los pokemones en el json
        pkm = Pokemon(stats['nombre'],stats['tipo'],int(stats['vida']),int(stats['ataque']),int(stats['defensa']),int(stats['nivel']),int(stats['exp']))
        # Crea cada uno de los pokemones como un objeto
        # Como el json solo guarda cadenas, transformamos a int los atributos correspondientes
        pokemones[pokemon] = pkm
        # Los añade a un diccionario para despues acceder a ellos por medio de su nombre

# Visualizar pokemones creados 
#for pokemon in pokemones:
#    print('Tienes a {} atrapado'.format(pokemon))

print("""
\t*********  POKEDEX  **********
\t***     PROYECTO FINAL     ***
\t FUNDAMENTOS DE PROGRAMACIÓN 
""")

while True:
    pokebolas = cargarJson()
    menu_principal()
    try:
        entrada_Main = int(input('>> '))
        Excepciones.validar_Main(entrada_Main)

        if entrada_Main == 1: # Imprimir pokedex
            print(pokedex)
        elif entrada_Main == 2: # Atrapar pokemon
            pokemones = atraparPokemon(pokemones, pokedex)
        elif entrada_Main == 3: # Estadisticas del pokemon
            estadisticas(pokebolas)
        elif entrada_Main == 4:
            duelo(pokebolas)
        else: # entrada_Main == 5 -> Salir
            print("\n ¡Adios!\n")
            break

    except ValueError:
        print("\n** Ingresa un valor válido\n")
    except Excepciones:
        print('\n** Ingresa un valor válido\n')

    os.system("pause")
