import random #importamos la libreria random para usarlo como dado

def snake(player): #hacemos las serpientes del tablero
    if player == 14:
        return 4
    elif player == 19:
        return 8
    elif player == 22:
        return 20
    elif player == 24:
        return 16
    

def stair(player): #hacemos las escalera del tablero
    if player == 3:
        return 11
    elif player == 6:
        return 17
    elif player == 9:
        return 18
    elif player == 10:
        return 12

def dado(): #Dado que proporciona un numero random del 1 - 6
    return random.randint(1, 6)

def Jugar():
    player = 0
    Dado = int
    Nturnos = 0
    print("----Bienvenido al juego de la escalera Veevart----")
    print("----------------Reglas del juego------------------")
    print("1. El tablero tiene 25 cuadros, y el objetivo es llegar o superar el cuadro 25")
    print("2. El cuadro inicial es el 0, el cual se encuentra por fuera del tablero a la izquierda del cuadro 1")
    print("3. En cada turno usted tira un dado de 6 lados y mueve el número de cuadrados siguiendo la línea punteada de la imagen")
    print("4. Si su turno termina en la parte inferior de una escalera, sube por la escalera")
    print("5. Si su turno termina en la cabeza de una serpiente, baja por la serpiente")
    print("6. Recuerde que un dado solo puede caer entre los números 1 a 6")

    while player <25:
        Nturnos += 1
        print("Turno numero: "+str(Nturnos))
        print("Lanzamos dado")
        Dado = dado()
        print("Resultado: "+ str(Dado))
        print("Desplazando jugador...")
        player += Dado
        print("Jugador 1: Estas en la casilla numero "+str(player))

        if player == 14 or player == 19 or player == 22 or player == 24:
            player = snake(player)
            print("Caiste en la serpiente ahora estas en la casilla: "+str(player))
        elif player == 3 or player == 6 or player == 9 or player == 10:
            player = stair(player)
            print("Caiste en la escalera ahora estas en la casilla: "+str(player))
    print("Has ganado despues de "+str(Nturnos)+" Turnos")

Jugar()