import random

def obtener_jugada():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def jugar_ronda(jugador1, jugador2):
    jugada1 = obtener_jugada()
    jugada2 = obtener_jugada()
    
    print(f"{jugador1} ha jugado: {jugada1}")
    input("Presiona Enter para que juegue el otro jugador...")
    print(f"{jugador2} ha jugado: {jugada2}")
    
    if jugada1 == jugada2:
        print("Empate!")
        return None
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
         (jugada1 == "papel" and jugada2 == "piedra") or \
         (jugada1 == "tijera" and jugada2 == "papel"):
        print(f"{jugador1} gana la ronda!")
        return jugador1
    else:
        print(f"{jugador2} gana la ronda!")
        return jugador2

def jugar_juego():
    puntaje_jugador1 = 0
    puntaje_jugador2 = 0
    
    jugador1 = input("Ingrese el nombre del jugador 1: ")
    jugador2 = input("Ingrese el nombre del jugador 2: ")
    
    while puntaje_jugador1 < 20 and puntaje_jugador2 < 20:
        ganador_ronda = jugar_ronda(jugador1, jugador2)
        if ganador_ronda == jugador1:
            puntaje_jugador1 += 10
        elif ganador_ronda == jugador2:
            puntaje_jugador2 += 10
        input("Presiona Enter para continuar al siguiente juego...")
    
    if puntaje_jugador1 >= 20:
        print(f"\n{jugador1} gana el juego con un puntaje de {puntaje_jugador1}!")
    elif puntaje_jugador2 >= 20:
        print(f"\n{jugador2} gana el juego con un puntaje de {puntaje_jugador2}!")

# Iniciar el juego
jugar_juego()
