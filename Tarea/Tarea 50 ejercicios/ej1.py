# Ejercicio 1: Comisiones de un vendedor
sueldo_base = 1000  # Sueldo base del vendedor
venta1 = float(input("Ingrese venta 1: "))
venta2 = float(input("Ingrese venta 2: "))
venta3 = float(input("Ingrese venta 3: "))

# Calculamos la comisión como el 10% de las ventas totales
comisiones = (venta1 + venta2 + venta3) * 0.10

# Calculamos el total a recibir sumando el sueldo base y las comisiones
total = sueldo_base + comisiones

# Imprimimos los resultados
print(f"El vendedor recibirá ${comisiones:.2f} por concepto de comisiones en el mes.")
print(f"El total que recibirá en el mes será de ${total:.2f}.")
