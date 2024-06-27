# Ejercicio 3: Calificación final de un alumno en Algoritmos
parcial1 = 80  # Calificación del primer parcial
parcial2 = 75  # Calificación del segundo parcial
parcial3 = 85  # Calificación del tercer parcial
examen_final = 90  # Calificación del examen final
trabajo_final = 95  # Calificación del trabajo final

# Calculamos el promedio de los tres parciales
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

# Calculamos la calificación final según la ponderación especificada
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# Imprimimos la calificación final
print(f"La calificación final en Algoritmos es: {calificacion_final:.2f}")

