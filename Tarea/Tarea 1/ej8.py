# Definir la velocidad de la luz en kilómetros por segundo
velocidad_luz_km_por_segundo = 300000

# Solicitar al usuario que ingrese el tiempo en segundos
tiempo_segundos = float(input("Ingrese el tiempo en segundos: "))

# Calcular la distancia que recorre la luz en el tiempo dado
distancia_recorrida_km = velocidad_luz_km_por_segundo * tiempo_segundos

# Mostrar la distancia que recorre la luz en el tiempo dado
print("La luz recorre una distancia de", distancia_recorrida_km, "kilómetros en", tiempo_segundos, "segundos")
