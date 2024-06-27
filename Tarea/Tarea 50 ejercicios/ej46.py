# Ejercicio 46: Calcular el total a pagar por la colegiatura de un alumno

promedio = float(input("Ingrese el promedio del alumno: "))
tipo_alumno = input("Ingrese el tipo de alumno (P para preparatoria, C para profesional): ").upper()
unidades_cursadas = int(input("Ingrese la cantidad de unidades a cursar: "))
precio_unidad = 0
descuento = 0
iva = 0.1

if promedio >= 9.5 and tipo_alumno == "P":
    unidades_cursadas = 55
    descuento = 0.25
elif 9 <= promedio < 9.5 and tipo_alumno == "P":
    unidades_cursadas = 50
    descuento = 0.1
elif 7 < promedio < 9 and tipo_alumno == "P":
    unidades_cursadas = 50
elif promedio <= 7 and 0 <= unidades_reprobadas <= 3 and tipo_alumno == "P":
    unidades_cursadas = 45
elif promedio <= 7 and unidades_reprobadas >= 4 and tipo_alumno == "P":
    unidades_cursadas = 40
elif promedio >= 9.5 and tipo_alumno == "C":
    unidades_cursadas = 55
    descuento = 0.2
else:
    unidades_cursadas = 55

if tipo_alumno == "P":
    precio_unidad = 180
else:
    precio_unidad = 300

subtotal = unidades_cursadas * precio_unidad
descuento_total = subtotal * descuento
subtotal_descuento = subtotal - descuento_total
total = subtotal_descuento + (subtotal_descuento * iva)

print(f"El total a pagar por la colegiatura es: {total}")
