# Ejercicio 14: Calcular el descuento en una compra en un almacén
precio_compra = 600000  # Precio total de la compra

# Aplicamos el descuento si la compra supera los $500.000
if precio_compra > 500000:
    descuento = precio_compra * 0.20  # 20% de descuento
else:
    descuento = 0

# Calculamos el total a pagar restando el descuento
total_pagar = precio_compra - descuento

# Imprimimos el total a pagar
print(f"El total a pagar con el descuento aplicado es: ${total_pagar:.2f}")
