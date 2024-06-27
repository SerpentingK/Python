# Precio del aparato de sonido
precio_aparato = float(input("Ingrese el precio del aparato: "))

# Marca del aparato
marca = input("Ingrese la marca del aparato: ")

# Inicializamos el descuento
descuento = 0

# Calculamos el descuento del 10% si el precio es $2000 o más
if precio_aparato >= 2000:
    descuento += precio_aparato * 0.10
# Si la marca es NOSY, aplicamos un descuento adicional del 5%
if marca.upper() == "NOSY":
    descuento += precio_aparato * 0.05

# Calculamos el precio total con descuento e IVA
precio_con_descuento = precio_aparato - descuento
precio_con_iva = precio_con_descuento * 1.16  # IVA del 16%

# Mostramos el precio a pagar con IVA incluido
print(f"El precio a pagar con IVA incluido es: ${precio_con_iva:.2f}")
