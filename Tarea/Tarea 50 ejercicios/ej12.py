# Ejercicio 12: Calcular el porcentaje de inversión de cada persona en una empresa
inversion_persona1 = 5000  # Inversión de la persona 1
inversion_persona2 = 7000  # Inversión de la persona 2
inversion_persona3 = 10000  # Inversión de la persona 3
inversion_total = inversion_persona1 + inversion_persona2 + inversion_persona3

# Calculamos el porcentaje de inversión de cada persona
porcentaje_persona1 = (inversion_persona1 / inversion_total) * 100
porcentaje_persona2 = (inversion_persona2 / inversion_total) * 100
porcentaje_persona3 = (inversion_persona3 / inversion_total) * 100

# Imprimimos los porcentajes de inversión
print(f"Porcentaje de inversión de la persona 1: {porcentaje_persona1:.2f}%")
print(f"Porcentaje de inversión de la persona 2: {porcentaje_persona2:.2f}%")
print(f"Porcentaje de inversión de la persona 3: {porcentaje_persona3:.2f}%")
