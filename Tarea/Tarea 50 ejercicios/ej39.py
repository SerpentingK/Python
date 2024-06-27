# Ejercicio 39: Calcular el descuento en la compra de computadoras en una tienda
num_computadoras = int(input("Ingrese el número de computadoras compradas: "))
precio_unitario = 11000  # Precio unitario de cada computadora
subtotal = num_computadoras * precio_unitario

if num_computadoras < 5:
    descuento = 0
elif num_computadoras < 10:
    descuento = 0.1
else:
    descuento = 0.4

descuento_total = subtotal * descuento
total_pagar = subtotal - descuento_total

print(f"El descuento total es: ${descuento_total}")
print(f"El total a pagar es: ${total_pagar}")
