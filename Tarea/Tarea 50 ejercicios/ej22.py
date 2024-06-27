# Ejercicio 22: Calcular el total a pagar por la compra de llantas
cantidad_llantas = int(input("Ingrese la cantidad de llantas a comprar: "))
precio_llanta = 80000  # Precio unitario de cada llanta
total_pagar = 0

# Calculamos el precio total según la cantidad de llantas
if cantidad_llantas < 5:
    total_pagar = cantidad_llantas * precio_llanta
else:
    total_pagar = cantidad_llantas * 70000  # Precio unitario con descuento de 5 o más llantas

print(f"Total a pagar por la compra de llantas: ${total_pagar}")
