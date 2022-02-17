import pandas as pd

# Cargar csv para tomar los datos del pokemon
def cargarPokedex():
    try:
        pokedex = pd.read_csv('_pokemones.csv')
        pokedex.set_index('Name', inplace = True)
        return pokedex
    except FileNotFoundError: # Archivo no encontrado
        print('\n** Archivo no encontrado\n')

def guardarJson():
    pass

def cargarJson():
    pass