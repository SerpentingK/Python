# Ejercicio 19: Imprimir información de un artículo con descuento según clave
nombre_articulo = input("Ingrese el nombre del artículo: ")
clave = input("Ingrese la clave del artículo (01 o 02): ")
precio_original = float(input("Ingrese el precio original del artículo: "))
precio_descuento = 0

# Calculamos el precio con descuento según la clave
if clave == "01":
    descuento = precio_original * 0.10
    precio_descuento = precio_original - descuento
elif clave == "02":
    descuento = precio_original * 0.20
    precio_descuento = precio_original - descuento

print(f"Nombre del artículo: {nombre_articulo}")
print(f"Clave: {clave}")
print(f"Precio original: ${precio_original:.2f}")
print(f"Precio con descuento: ${precio_descuento:.2f}")
