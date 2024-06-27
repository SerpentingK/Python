# Ejercicio 35: Calcular el pago por horas extras trabajadas
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
salario_por_hora = 16
pago_horas_extra = 0

if horas_trabajadas > 40:
    horas_extra = horas_trabajadas - 40
    if horas_extra <= 8:
        pago_horas_extra = horas_extra * (salario_por_hora * 2)
    else:
        pago_horas_extra = 8 * (salario_por_hora * 2) + (horas_extra - 8) * (salario_por_hora * 3)

print(f"El pago por horas extras trabajadas es: {pago_horas_extra}")
