import pandas as pd
import json

diccionarioPokemon = {}
# Diccionario que guarda los datos de los pokemones ya creados y por crear
# y su contenido se lee y escribe en un json

# Cargar csv para tomar los datos del pokemon
def cargarPokedex():
    try:
        pokedex = pd.read_csv('data/_pokemones.csv') 
        pokedex.set_index('Name', inplace = True)
        # Coloca el indice por nombre
        return pokedex # Retorna todo el contenido del csv
    except FileNotFoundError: # Archivo no encontrado
        print('\n** Archivo no encontrado\n')

# Recibe el nombre del pokemon y sus datos
def guardarJson(pokemon, stats):
    global diccionarioPokemon
    diccionarioPokemon[pokemon] = stats
    # En el diccionario usamos la clave como el nombre del pokemon
    # y como valor los datos (stats) del pokemon
    with open('data/pokebolas.json','w') as f:
    # Abrimos el json en modo escritura
        json.dump(diccionarioPokemon,f, sort_keys=True, indent=4)
        #sort_keys acomoda las claves en orden alfabetico
        #intent agrega tabulaciones
        # Escribimos los datos del pokemon en el json

# Esta funcion carga los datos leidos en el json
def cargarJson():
    global diccionarioPokemon
    try: 
        with open('data/pokebolas.json') as f:
        # Abre el archivo json 
            diccionarioPokemon = json.load(f)
            # Lee el contenido y lo guarda en la variable diccionarioPokemon
            return diccionarioPokemon
            # retorna el diccionario
    except FileNotFoundError: # Si no existe el diccionario
        return diccionarioPokemon
        # regresa el diccionario vacio

# Para tener una mejor visualizacion del json en visual studio code
# shift + alt + f