from pokemon import *

def menu_principal():
    print('MENU PRINCIPAL')
    print(""" 
        [1] Pokedex general
            * Visualizar stats de todos los pokémones
        [2] Atrapar pokémon
            * Atrapa tus pokémones favoritos
        [3] Pokémones atrapados
            * Visualiza tus pokemones atrapados
            * Obten estadísticas
        [4] Duelo de pokemones
            * Duelo de pokemones
        [5] Salir
    """)

def atraparPokemon(pokemones, pokedex):
    while True:
        # Instanciar pokemon 
        name = input('¿Qué pokémon quieres atrapar?\n *[0] Regresar\n>> ').capitalize().replace(' ','')
        if name == '0':
            return pokemones
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
                return pokemones
            else: # Si existe le notifica al usuario que ya lo tiene
                print('Ya tienes al pokemon {}'.format(name))
        except:
            print('No existe el pokémon')

def estadisticas(pokebolas):
    print("Estos son tus pokemones\n")
    for pokemon, stats in pokebolas.items():
        print(pokemon.center(50, "-"))
        print("Ataque: {}\nDefensa: {}\nExperiencia: {}\nNivel: {}\nTipo: {}\nVida: {}\n".format(stats['ataque'], 
        stats['defensa'], stats['exp'], stats["nivel"], stats["tipo"], stats["vida"]))




def duelo(pokebolas):
    print("¿Qué pokemon deseas usar?\n")
    for pokemon in pokebolas:
        print(f"{pokemon}")

    poke_selected = input(">>> ").capitalize()#pondra la primera letra en mayuscula para que coincida
    stats = pokebolas[poke_selected]
    batalla_pokemon = Pokemon(
    stats['nombre'],
    stats['tipo'],
    stats['vida'],
    stats['ataque'],
    stats['defensa'],
    stats['nivel'],
    stats['exp'])

    batalla_pokemon.pelear()