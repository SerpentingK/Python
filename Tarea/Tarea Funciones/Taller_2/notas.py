def calcular_promedio(calificaciones):
    total = 0
    for i in calificaciones:
        total += i
    return total / len(calificaciones)

def obtener_maxima(calificaciones):
    califi = calificaciones.copy()
    califi.sort()
    return califi[-1]

def obtener_minima(calificaciones):
    califi = calificaciones.copy()
    califi.sort()
    return califi[0]

# Solicitar las calificaciones al usuario
calificaciones = []
for i in range(4):
    calificacion = float(input(f"Introduce la calificación {i+1}: "))
    calificaciones.append(calificacion)

# Calcular el promedio, la calificación máxima y mínima
promedio = calcular_promedio(calificaciones)
maxima = obtener_maxima(calificaciones)
minima = obtener_minima(calificaciones)

# Mostrar los resultados
print(f"El promedio de las calificaciones es: {promedio}")
print(f"La calificación máxima es: {maxima}")
print(f"La calificación mínima es: {minima}")
