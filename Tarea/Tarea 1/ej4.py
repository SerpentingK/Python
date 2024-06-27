# Solicitar al usuario que ingrese el número de horas
horas = float(input("Ingrese el número de horas: "))

# Convertir horas a minutos, segundos y días
minutos = horas * 60
segundos = horas * 3600
dias = horas / 24

# Mostrar el resultado de la conversión
print("Equivalente en minutos:", minutos)
print("Equivalente en segundos:", segundos)
print("Equivalente en días:", dias)
