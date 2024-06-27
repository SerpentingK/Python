# Solicitar al usuario que ingrese el costo del artículo
costo = float(input("Ingrese el costo del artículo: "))

# Calcular la utilidad y el precio de venta
utilidad = costo * 1.5
impuesto = (costo + utilidad) * 0.15
precio_venta = costo + utilidad + impuesto

# Mostrar la utilidad, impuesto y precio de venta
print("Utilidad:", utilidad)
print("Impuesto:", impuesto)
print("Precio de venta:", precio_venta)
