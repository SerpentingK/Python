# Nivel del alumno (preparatoria o profesional)
nivel_alumno = input("Ingrese el nivel del alumno (preparatoria o profesional): ")

# Promedio del alumno
promedio = float(input("Ingrese el promedio del alumno: "))

# Número de materias reprobadas del alumno
materias_reprobadas = int(input("Ingrese el número de materias reprobadas del alumno: "))

# Calculamos el total a pagar
if nivel_alumno.lower() == "preparatoria":
    if promedio >= 9.5:
        unidades = 55
        total = (180 * unidades) * 0.75  # Descuento del 25%
    elif 9 <= promedio < 9.5:
        unidades = 50
        total = (180 * unidades) * 0.90  # Descuento del 10%
    elif 7 < promedio < 9:
        unidades = 50
        total = 180 * unidades
    elif promedio <= 7 and materias_reprobadas <= 3:
        unidades = 45
        total = 180 * unidades
    elif promedio <= 7 and materias_reprobadas >= 4:
        unidades = 40
        total = 180 * unidades
    else:
        print("Datos incorrectos.")
        exit()
elif nivel_alumno.lower() == "profesional":
    if promedio >= 9.5:
        unidades = 55
        total = (300 * unidades) * 0.80  # Descuento del 20%
    elif promedio < 9.5:
        unidades = 55
        total = 300 * unidades
    else:
        print("Datos incorrectos.")
        exit()
else:
    print("Datos incorrectos.")
    exit()

# Mostramos el total a pagar
print(f"El total a pagar es: ${total:.2f}")
