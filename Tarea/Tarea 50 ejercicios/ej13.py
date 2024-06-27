# Ejercicio 13: Calcular el promedio general y por materia de un alumno

# Solicitamos las calificaciones del alumno
examen_matematicas = float(input("Ingrese la calificación del examen de Matemáticas: "))
tarea1_matematicas = float(input("Ingrese la calificación de la tarea 1 de Matemáticas: "))
tarea2_matematicas = float(input("Ingrese la calificación de la tarea 2 de Matemáticas: "))
tarea3_matematicas = float(input("Ingrese la calificación de la tarea 3 de Matemáticas: "))
promedio_tareas_matematicas = (tarea1_matematicas + tarea2_matematicas + tarea3_matematicas) / 3

examen_fisica = float(input("Ingrese la calificación del examen de Física: "))
tarea1_fisica = float(input("Ingrese la calificación de la tarea 1 de Física: "))
tarea2_fisica = float(input("Ingrese la calificación de la tarea 2 de Física: "))
promedio_tareas_fisica = (tarea1_fisica + tarea2_fisica) / 2

examen_quimica = float(input("Ingrese la calificación del examen de Química: "))
tarea1_quimica = float(input("Ingrese la calificación de la tarea 1 de Química: "))
tarea2_quimica = float(input("Ingrese la calificación de la tarea 2 de Química: "))
tarea3_quimica = float(input("Ingrese la calificación de la tarea 3 de Química: "))
promedio_tareas_quimica = (tarea1_quimica + tarea2_quimica + tarea3_quimica) / 3

# Calculamos el promedio general y por materia
promedio_general = (examen_matematicas * 0.9 + promedio_tareas_matematicas * 0.1 +
                    examen_fisica * 0.8 + promedio_tareas_fisica * 0.2 +
                    examen_quimica * 0.85 + promedio_tareas_quimica * 0.15) / 3

promedio_matematicas = (examen_matematicas * 0.9 + promedio_tareas_matematicas * 0.1)
promedio_fisica = (examen_fisica * 0.8 + promedio_tareas_fisica * 0.2)
promedio_quimica = (examen_quimica * 0.85 + promedio_tareas_quimica * 0.15)

# Imprimimos los resultados
print(f"Promedio general: {promedio_general:.2f}")
print(f"Promedio en Matemáticas: {promedio_matematicas:.2f}")
print(f"Promedio en Física: {promedio_fisica:.2f}")
print(f"Promedio en Química: {promedio_quimica:.2f}")
