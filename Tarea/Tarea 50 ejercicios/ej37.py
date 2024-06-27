# Ejercicio 37: Calcular el precio final de una compra con descuento según el color de una bolita
precio_total = float(input("Ingrese el precio total de la compra: "))
color_bolita = input("Ingrese el color de la bolita (blanco, verde, amarilla, azul, roja): ")

descuento = 0

if color_bolita == "verde":
    descuento = precio_total * 0.1
elif color_bolita == "amarilla":
    descuento = precio_total * 0.25
elif color_bolita == "azul":
    descuento = precio_total * 0.5
elif color_bolita == "roja":
    descuento = precio_total

precio_final = precio_total - descuento

print(f"El precio final de la compra es: {precio_final}")
