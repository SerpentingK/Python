# Solicitar al usuario que ingrese la descripción del artículo y el costo de producción
descripcion = input("Ingrese la descripción del artículo: ")
costo_produccion = float(input("Ingrese el costo de producción del artículo: "))

# Calcular la utilidad y el precio de venta
utilidad = costo_produccion * 1.2
precio_venta = costo_produccion + utilidad
impuesto = precio_venta * 0.15
precio_venta_total = precio_venta + impuesto

# Mostrar la descripción del artículo y el precio de venta total
print("Descripción del artículo:", descripcion)
print("Precio de venta total:", precio_venta_total)

