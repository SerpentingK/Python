# Ejercicio 36: Calcular la utilidad en el reparto anual de utilidades
salario_mensual = float(input("Ingrese el salario mensual del trabajador: "))
antiguedad = int(input("Ingrese la antigüedad en años del trabajador: "))

if antiguedad < 1:
    utilidad = salario_mensual * 0.05
elif antiguedad < 2:
    utilidad = salario_mensual * 0.07
elif antiguedad < 5:
    utilidad = salario_mensual * 0.1
elif antiguedad < 10:
    utilidad = salario_mensual * 0.15
else:
    utilidad = salario_mensual * 0.2

print(f"La utilidad en el reparto anual de utilidades es: {utilidad}")
