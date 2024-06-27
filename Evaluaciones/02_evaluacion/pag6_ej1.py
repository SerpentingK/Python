def estudiante_calificacion_mas_alta(diccionario_estudiantes):
    estudiante_max_calificacion = ""
    calificacion_max = 0

    for estudiante, calificacion in diccionario_estudiantes.items():
        if calificacion > calificacion_max:
            estudiante_max_calificacion = estudiante
            calificacion_max = calificacion

    return estudiante_max_calificacion, calificacion_max

# Ingreso de datos
num_estudiantes = int(input("Ingrese el número de estudiantes: "))
diccionario_estudiantes = {}
for _ in range(num_estudiantes):
    estudiante = input("Ingrese el nombre del estudiante: ")
    calificacion = int(input("Ingrese la calificación del estudiante: "))
    diccionario_estudiantes[estudiante] = calificacion

# Llamada a la función e impresión del resultado
estudiante_max_calificacion, calificacion_max = estudiante_calificacion_mas_alta(diccionario_estudiantes)
print(f"El estudiante con la calificación más alta es {estudiante_max_calificacion} con una calificación de {calificacion_max}")
