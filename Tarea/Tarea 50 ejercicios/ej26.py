# Ejercicio 26: Calcular el costo de la colegiatura para un alumno
promedio = float(input("Ingrese el promedio del alumno: "))
colegiatura = 0

if promedio >= 9.5:
    colegiatura = 55 * 300 * 0.75  # Descuento del 25% para alumnos con promedio mayor o igual a 9.5
elif promedio >= 9:
    colegiatura = 50 * 300 * 0.90  # Descuento del 10% para alumnos con promedio mayor o igual a 9
elif 7 <= promedio < 9:
    colegiatura = 50 * 300  # Sin descuento para alumnos con promedio entre 7 y 9
else:
    reprobadas = int(input("Ingrese el número de materias reprobadas: "))
    if reprobadas >= 4:
        colegiatura = 40 * 300  # Sin descuento para alumnos con promedio menor a 7 y 4 o más materias reprobadas
    else:
        colegiatura = 45 * 300  # Sin descuento para alumnos con promedio menor a 7 y menos de 4 materias reprobadas

print(f"Total a pagar por la colegiatura: ${colegiatura:.2f}")
