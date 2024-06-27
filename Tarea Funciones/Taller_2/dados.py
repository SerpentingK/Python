import random

def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def craps():
    primera_tirada = tirar_dados()
    if primera_tirada in (7, 11):
        print(f"¡Ganaste en la primera tirada con un {primera_tirada}!")
        return True
    elif primera_tirada in (2, 3, 12):
        print(f"Perdiste en la primera tirada con un {primera_tirada} (craps).")
        return False
    else:
        print(f"Tu punto es {primera_tirada}. Debes seguir tirando para hacer tu tirada.")
        while True:
            siguiente_tirada = tirar_dados()
            print(f"Has tirado un {siguiente_tirada}.")
            if siguiente_tirada == 7:
                print("Perdiste al sacar un 7 antes de hacer tu tirada.")
                return False
            elif siguiente_tirada == primera_tirada:
                print(f"¡Ganaste haciendo tu tirada de {primera_tirada}!")
                return True

jugar = True
while jugar:
    if craps():
        print("¡Felicidades! ¿Quieres jugar otra vez?")
    else:
        print("¿Quieres intentarlo de nuevo?")
    respuesta = input("Escribe 's' para seguir jugando, o cualquier otra tecla para salir.\n")
    if respuesta.lower() != "s":
        jugar = False
