from funciones_generales.archivos import *
from pokemon import *

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


# Instanciar pokemon 
name = input('¿Qué pokémon quieres atrapar?\n>> ').capitalize().replace(' ','')
# capitalize -> Primera letra en mayuscula
# replace -> Elimina los espacios
try: # Si el pokemon existe en el csv
    # Para evitar que sobreescriba los datos de un pokemon, revisa si este ya existe
    # Si no existe, crea al pokemon
    if not name in pokemones.keys(): 
        datos = pokedex.loc[name] # toma los datos del pokemon
        tipo = datos['Type 1']
        hp = datos['HP']
        ataque = datos['Attack']
        defensa = datos['Defense']
        pokemon = Pokemon(name, tipo, hp, ataque, defensa)
        # Usando los datos crea el objeto pokemon
        pokemones[name] = pokemon
        # Añadimos el pokemon creado al diccinario de pokemones
        print('Haz logrado capturar a {}'.format(name))
    else: # Si existe le notifica al usuario que ya lo tiene
        print('Ya tienes al pokemon {}'.format(name))
except:
    print('No existe el pokémon')

# Visualizar pokemones creados 

for pokemon in pokemones:
    print('Tienes a {} atrapado'.format(pokemon))


