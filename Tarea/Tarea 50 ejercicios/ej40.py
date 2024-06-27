# Ejercicio 40: Calcular el precio de compra de llantas en un almacén
num_llantas = int(input("Ingrese el número de llantas compradas: "))

if num_llantas < 5:
    precio_unitario = 30000
elif num_llantas < 11:
    precio_unitario = 25000
else:
    precio_unitario = 20000

precio_total = num_llantas * precio_unitario

print(f"El precio total a pagar por las llantas es: ${precio_total}")
