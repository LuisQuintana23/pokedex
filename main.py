from archivos import *
from pokemon import *

pokedex = cargarPokedex()

# Instanciar pokemon 
name = input('¿Qué pokémon quieres atrapar?\n>> ').capitalize().replace(' ','')
# capitalize -> Primera letra en mayuscula
# replace -> Elimina los espacios
try: # Si el pokemon existe en el csv
    datos = pokedex.loc[name] # toma los datos del pokemon
    tipo = datos['Type 1']
    hp = datos['HP']
    ataque = datos['Attack']
    defensa = datos['Defense']
    pokemon = Pokemon(name, tipo, hp, ataque, defensa)
    # Usando los datos crea el objeto pokemon
except:
    print('No existe el pokémon')


