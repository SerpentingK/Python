# Ejercicio 48: Calcular el total de una factura

# Variables de control
total_factura = 0
total_iva = 0

while True:
    importe = float(input("Ingrese el importe (0 para salir): "))
    if importe == 0:
        break
    iva = int(input("Ingrese el IVA (4, 7, 16): "))
    if iva not in [4, 7, 16]:
        print("IVA inválido. Por favor, introduzca 4, 7, o 16.")
        continue
    total_factura += importe
    total_iva += importe * (iva / 100)

# Calcular descuento
if total_factura < 1000:
    descuento = 0
elif total_factura < 10000:
    descuento = 0.05 * total_factura
else:
    descuento = 0.1 * total_factura

# Imprimir resultados
print(f"Total factura: {total_factura:.2f}")
print(f"Total IVA: {total_iva:.2f}")
print(f"Descuento: {descuento:.2f}")
print(f"Total a pagar: {(total_factura + total_iva - descuento):.2f}")
