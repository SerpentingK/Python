
precio_computadora = 11000

cantidad_computadoras = int(input("Ingrese la cantidad de computadoras que va a comprar: "))

total_sin_descuento = cantidad_computadoras * precio_computadora

descuento = 0

if cantidad_computadoras < 5:
    descuento = total_sin_descuento * 0.10  # 10% de descuento
elif cantidad_computadoras < 10:
    descuento = total_sin_descuento * 0.20  # 20% de descuento
else:
    descuento = total_sin_descuento * 0.40  # 40% de descuento

# Calculamos el total con descuento
total_con_descuento = total_sin_descuento - descuento

# Mostramos el total a pagar con descuento
print(f"Total a pagar con descuento: ${total_con_descuento}")
