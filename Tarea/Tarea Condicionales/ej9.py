import time

def obtener_calificacion(nota):
    if 0 <= nota <= 1:
        return "D"
    elif 1.1 <= nota <= 2.9:
        return "I"
    elif 3 <= nota <= 3.8:
        return "A"
    elif 3.9 <= nota <= 4.6:
        return "S"
    elif 4.7 <= nota <= 5:
        return "E"
    else:
        return "Nota inválida"


# Solicitar las notas de los cuatro períodos
promedio = 0
for i in range(1, 5):
    print(f"Período {i}:")
    nota1 = float(input("Ingrese la nota de la primera materia: "))
    nota2 = float(input("Ingrese la nota de la segunda materia: "))
    nota3 = float(input("Ingrese la nota de la tercera materia: "))
    nota4 = float(input("Ingrese la nota de la cuarta materia: "))

    # Calcular el promedio de las notas
    promedio_periodo = (nota1 + nota2 + nota3 + nota4) / 4
    promedio += promedio_periodo

    # Mostrar calificaciones por período
    print(f"Calificación del período {i}:")
    print(f"Materia 1: {obtener_calificacion(nota1)}")
    print(f"Materia 2: {obtener_calificacion(nota2)}")
    print(f"Materia 3: {obtener_calificacion(nota3)}")
    print(f"Materia 4: {obtener_calificacion(nota4)}")
    print(f"Promedio del período {i}: {promedio_periodo:.2f}")
    time.sleep(1)
    print()

# Calcular el promedio general
promedio_general = promedio / 4

# Determinar si el estudiante es promovido al siguiente grado
if promedio_general >= 3.5:
    if 3.5 <= promedio_general < 3.9:
        promocion = "Siguiente grado: 11"
    elif 3.9 <= promedio_general <= 5:
        promocion = "Siguiente grado: 12"
    print(f"El estudiante es promovido al siguiente grado. {promocion}")
else:
    print("El estudiante NO ES PROMOVIDO.")
