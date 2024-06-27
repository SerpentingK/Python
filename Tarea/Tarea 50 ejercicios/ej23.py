# Ejercicio 23: Calcular el descuento en una compra en un supermercado
total_compra = float(input("Ingrese el total de la compra en el supermercado: "))
descuento = 0

# Calculamos el descuento según el número escogido al azar
numero_escogido = int(input("Ingrese el número escogido al azar: "))
if numero_escogido < 74:
    descuento = total_compra * 0.15  # Descuento del 15% si el número es menor a 74
else:
    descuento = total_compra * 0.20  # Descuento del 20% si el número es mayor o igual a 74

print(f"Descuento: ${descuento:.2f}")
