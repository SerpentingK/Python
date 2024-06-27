# Ejercicio 42: Calcular el precio de un aparato de sonido con descuento
precio_sin_iva = float(input("Ingrese el precio del aparato sin IVA: "))
marca = input("Ingrese la marca del aparato (NOSY para descuento adicional): ")

# Aplicar descuento del 10% si el precio sin IVA es mayor o igual a $2000
descuento = 0.1 if precio_sin_iva >= 2000 else 0

# Aplicar descuento adicional del 5% si la marca es "NOSY"
if marca.upper() == "NOSY":
    descuento += 0.05

# Calcular precio final con IVA incluido
precio_con_descuento = precio_sin_iva * (1 - descuento)
precio_con_iva = precio_con_descuento * 1.16

print(f"El precio final del aparato de sonido con IVA incluido es: ${precio_con_iva:.2f}")
