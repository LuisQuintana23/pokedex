import pandas as pd # lectura de archivos csv
import json # lectura y escritura de archivos json
import os # creacion y verificacion de carpetas
import ssl # verificacion de certificados de url

ssl._create_default_https_context = ssl._create_unverified_context
# Esta instrucciona ayuda a validar los certificados para poder usar 
# el url de _pokemones.csv 

diccionarioPokemon = {}
# Diccionario que guarda los datos de los pokemones ya creados y por crear
# y su contenido se lee y escribe en un json

# Comprueba si la carpeta data existe
def verificarCarpeta():
    if not os.path.exists('data'): # Si la carpeta data no existe
        os.mkdir('data') # La crea

# Cargar csv para tomar los datos del pokemon
def cargarPokedex():
    verificarCarpeta()
    try:
        pokedex = pd.read_csv('data/_pokemones.csv') 
        pokedex.set_index('Name', inplace = True)
        # Coloca el indice por nombre
        return pokedex # Retorna todo el contenido del csv
    except FileNotFoundError: # Archivo no encontrado
        url = 'https://raw.githubusercontent.com/LuisQuintana23/pokedex/main/data/_pokemones.csv'
        # Toma el csv de un repositorio en github
        pokedex = pd.read_csv(url) # lee el csv
        pokedex.set_index('Name', inplace = True) # Pone como indice el nombre de los pokemons
        pokedex.to_csv('data/_pokemones.csv') # Crea el archivo en la carpeta data
        return pokedex # Devuelve el dataframe

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