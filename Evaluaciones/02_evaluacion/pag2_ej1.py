def calcular_promedio_estudiantes():
    cantidad = int(input("Ingrese la cantidad de estudiantes: "))
    estudiantes = {}
    
    for i in range(cantidad):
        estudiante = input(f"Ingrese el nombre del estudiante {i + 1}: ")
        calificaciones = []
        while True:
            calificacion = input(f"Ingrese la calificación para {estudiante} (o 'fin' para terminar): ")
            if calificacion.lower() == 'fin':
                break
            calificaciones.append(float(calificacion))
        
        promedio = sum(calificaciones) / len(calificaciones)
        estudiantes[estudiante] = promedio
    
    return estudiantes

# Ejemplo de uso
estudiantes = calcular_promedio_estudiantes()
print(estudiantes)
