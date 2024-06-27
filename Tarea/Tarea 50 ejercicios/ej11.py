# Ejercicio 11: Calcular el tiempo promedio de una persona en recorrer una ruta en una semana

# Solicitamos los tiempos en minutos de la persona para cada día de la semana
tiempo_lunes = float(input("Ingrese el tiempo en minutos del lunes: "))
tiempo_martes = float(input("Ingrese el tiempo en minutos del martes: "))
tiempo_miercoles = float(input("Ingrese el tiempo en minutos del miércoles: "))
tiempo_jueves = float(input("Ingrese el tiempo en minutos del jueves: "))
tiempo_viernes = float(input("Ingrese el tiempo en minutos del viernes: "))
tiempo_sabado = float(input("Ingrese el tiempo en minutos del sábado: "))
tiempo_domingo = float(input("Ingrese el tiempo en minutos del domingo: "))

# Calculamos el tiempo promedio en minutos
tiempo_promedio = (tiempo_lunes + tiempo_martes + tiempo_miercoles + tiempo_jueves + tiempo_viernes + tiempo_sabado + tiempo_domingo) / 7

# Convertimos el tiempo promedio a horas y minutos
horas = int(tiempo_promedio / 60)
minutos = int(tiempo_promedio % 60)

# Imprimimos el tiempo promedio
print(f"El tiempo promedio de la persona en recorrer la ruta en una semana es de: {horas} horas y {minutos} minutos.")
