# Ejercicio 41: Juego de preguntas

print("Bienvenido al juego de preguntas. Responde correctamente las siguientes preguntas para ganar.")

# Pregunta 1
respuesta_1 = input("1. ¿Colón descubrió América? (Responde 'Si' o 'No'): ").capitalize()

# Pregunta 2
respuesta_2 = input("2. ¿La independencia de México fue en el año 1810? (Responde 'Si' o 'No'): ").capitalize()

# Pregunta 3
respuesta_3 = input("3. ¿The Doors fue un grupo de rock americano? (Responde 'Si' o 'No'): ").capitalize()

# Verificamos si el jugador ganó o perdió
if respuesta_1 == "Si" and respuesta_2 == "Si" and respuesta_3 == "Si":
    print("¡Felicidades, has ganado!")
else:
    print("Lo siento, has perdido. Inténtalo de nuevo.")
