import random
import sys

# la siugiente funcion imprime la tabla en la pantalla
def imprimir (lista):
    cont = 0
    print("----tabla----")
    for i in range(3):
        print("+-----------+","\n|",end="")
        for j in range(3):
            print(" %s |" %lista[cont],end="")
            cont += 1
        print()
    print("+-----------+")


# la siguiente funcion verifica si la casilla que ha elegido esta disponible
def disponibilidad (lista, indice, player):
    if (type(lista[indice]) == int):
        if (player == 1): lista_o[indice] = "X"
        if (player == 2): lista_o[indice] = "O"
        imprimir(lista_o)
        return True
    
# la siguiente funcion le pide a el jugador una casilla
def jugador (player):
    while (True):
        if (player==1): entrada = random.randrange(1,10)
        if (player==2): entrada = int(input("ingrese casilla: "))
                
        if (disponibilidad(lista_o, entrada-1,player)): break
        else: 
            if (player == 2): print("¡CASILLA NO DISPONIBLE!")
            continue

# la siguiente funcion verifica si ha ganado
def estado (lista,player):
    if (player==1): player = "X"
    if (player==2): player = "O"

    # recorrido diagonal de izquierda a derecha
    cont = 0
    for i in lista[::+4]:
        if (i == player):
            cont += 1
    if(cont==3): return True

    # recorrido horizontal
    temp = 0
    for i in range(3):
        cont = 0
        for j in range(3):
            if (lista[temp]==player):
                cont += 1
            temp += 1
        if(cont==3): return True

    # recorrido vertical
    for i in range(3):
        temp = i
        cont = 0
        for j in range(3):
            if (lista[temp] == player):
                cont += 1
            temp += 3
        if (cont == 3): return True

    # recorrido diagonal de derecha a izquierda
    cont = 0
    for i in lista[:7:-2]:
        if (i == player):
            cont += 1
    if (cont == 3): return True

# esta funcion verifica si todas las casillas estan llenas
def full (lista):
    for i in lista:
        if (type(i) == int):
            return False
    return True

# ////////////////////////// INICIO ///////////////////////////////
lista_o = []
cont = 1

for i in range(9):
    lista_o.append(cont)
    cont += 1

imprimir(lista_o)
jugadores = 0

while (True):
    jugadores = 1
    jugador(jugadores)
    if (estado(lista_o,jugadores)): break
    if (full(lista_o)): 
        jugadores = 0
        break


    jugadores = 2
    jugador(jugadores)
    if (estado(lista_o,jugadores)): break
    if (full(lista_o)): 
        jugadores = 0
        break

if (jugadores > 0): print("jugador %s ha ganado" %jugadores)
else: print("juego empatado")