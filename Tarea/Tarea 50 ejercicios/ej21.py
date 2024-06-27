# Ejercicio 21: Calcular la forma de pago de una empresa por una compra de refacciones
monto_compra = float(input("Ingrese el monto total de la compra de refacciones: "))
forma_pago = ""

# Determinamos la forma de pago según el monto de la compra
if monto_compra > 500000:
    inversion_propia = monto_compra * 0.55
    prestamo_banco = monto_compra * 0.30
    credito_fabricante = monto_compra * 0.15
    forma_pago = f"Inversión propia: ${inversion_propia:.2f}, Préstamo del banco: ${prestamo_banco:.2f}, Crédito del fabricante: ${credito_fabricante:.2f}"
else:
    inversion_propia = monto_compra * 0.70
    credito_fabricante = monto_compra * 0.30
    forma_pago = f"Inversión propia: ${inversion_propia:.2f}, Crédito del fabricante: ${credito_fabricante:.2f}"

print(f"Forma de pago: {forma_pago}")
