# Saldo actual del capital
saldo_actual = float(input("Ingrese el saldo actual del capital: "))

# Pedir préstamo y calcular nuevo saldo
if saldo_actual < 0:
    prestamo = 10000
    nuevo_saldo = 10000
elif saldo_actual > 0:
    if saldo_actual <= 20000:
        prestamo = 20000 - saldo_actual
        nuevo_saldo = 20000
    else:
        prestamo = 0
        nuevo_saldo = saldo_actual
else:
    print("El saldo actual no puede ser negativo.")
    exit()

# Distribución del presupuesto
equipo_computo = 5000
mobiliario = 2000
restante = nuevo_saldo - equipo_computo - mobiliario
insumos = restante / 2
incentivos_personal = restante / 2

# Mostrar resultados
print(f"Se pidió un préstamo de ${prestamo:.2f}")
print(f"El nuevo saldo es: ${nuevo_saldo:.2f}")
print(f"Se destinarán:")
print(f"Equipo de computo: ${equipo_computo}")
print(f"Mobiliario: ${mobiliario}")
print(f"Insumos: ${insumos:.2f}")
print(f"Incentivos al personal: ${incentivos_personal:.2f}")
