# Pregunta 1
print("¿Colón descubrió América?")
respuesta = input("(Si/No): ")
if respuesta.lower() == "si":
    # Pregunta 2
    print("¿La independencia de México fue en el año 1810?")
    respuesta = input("(Si/No): ")
    if respuesta.lower() == "si":
        # Pregunta 3
        print("¿The Doors fue un grupo de rock Americano?")
        respuesta = input("(Si/No): ")
        if respuesta.lower() == "si":
            print("¡Felicidades! Has ganado el juego.")
        else:
            print("Respuesta incorrecta. Juego terminado.")
    else:
        print("Respuesta incorrecta. Juego terminado.")
else:
    print("Respuesta incorrecta. Juego terminado.")
