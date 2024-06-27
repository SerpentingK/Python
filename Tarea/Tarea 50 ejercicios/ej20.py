# Ejercicio 20: Calcular el total a pagar por la compra de camisas con descuento
cantidad_camisas = int(input("Ingrese la cantidad de camisas a comprar: "))
precio_camisa = float(input("Ingrese el precio unitario de cada camisa: "))
total_compra = cantidad_camisas * precio_camisa

# Calculamos el descuento según la cantidad de camisas
if cantidad_camisas >= 3:
    descuento = total_compra * 0.20  # Descuento del 20%
else:
    descuento = total_compra * 0.10  # Descuento del 10%

total_pagar = total_compra - descuento

print(f"Total a pagar por la compra de camisas: ${total_pagar:.2f}")
