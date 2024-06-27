# Solicitar al usuario que ingrese las calificaciones de los cuatro exámenes
calificacion1 = float(input("Ingrese la calificación del primer examen: "))
calificacion2 = float(input("Ingrese la calificación del segundo examen: "))
calificacion3 = float(input("Ingrese la calificación del tercer examen: "))
calificacion4 = float(input("Ingrese la calificación del cuarto examen: "))

# Calcular el promedio de las calificaciones
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4

# Mostrar el promedio de las calificaciones
print("El promedio de las calificaciones es:", promedio)
