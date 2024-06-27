# Ejercicio 28: Calcular el depósito mensual en una cuenta de ahorro para el retiro (SAR)
salario_mensual = float(input("Ingrese su salario mensual: "))
porcentaje_deposito = float(input("Ingrese el porcentaje de su salario a depositar en el SAR: "))

# Calcular el depósito mensual en la cuenta del SAR
deposito_mensual = salario_mensual * (porcentaje_deposito / 100)

# Calcular el salario mensual después de realizar el depósito en el SAR
salario_despues_deposito = salario_mensual - deposito_mensual

print(f"Depósito mensual en el SAR: ${deposito_mensual:.2f}")
print(f"Salario mensual después del depósito en el SAR: ${salario_despues_deposito:.2f}")
