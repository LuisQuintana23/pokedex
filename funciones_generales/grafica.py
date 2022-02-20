
import matplotlib.pyplot as plt # Libreria para poder graficar

# Recibe la lista de las estadisticas que se desea grafica
# el nombre de la estadistica a graficar (grafica)
# y el nombre del pokemon
def imprimir_grafica(lista, grafica, pokemon):
    fig, ax = plt.subplots()
    combates = range(len(lista)) # Obtiene el numero de combates mediante la longitud de la lista
    ax.plot(combates, lista) # Crea la grafica
    # Formato para los ejes y el titulo
    ax.set_xlabel('{}'.format(grafica).capitalize(), fontdict={'fontsize':16,'family':'fantasy','color':'tab:red'})
    ax.set_ylabel('Combates', fontdict={'fontsize':16,'family':'fantasy','color':'tab:red'})
    ax.set_title('Grafica de {} de {}'.format(grafica, pokemon), fontdict={'fontsize':20,'fontweight':'bold','color':'y'})
    plt.show() # Se muestra la grafica

if "__main__" == __name__:
    lista = [4,3,2,1]
    #print(len(lista))
    imprimir_grafica(lista,'defensa','Bulbasaur')