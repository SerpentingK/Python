precio_menos_cinco = 300
precio_cinco_diez = 250
precio_mas_diez = 200

#Cantidad de llantas que compra el cliente
cantidad_llantas = int(input("Ingrese la cantidad de llantas que va a comprar: "))

#Calculamos el precio por llanta y el total de la compra
if cantidad_llantas < 5:
    precio_por_llanta = precio_menos_cinco
elif cantidad_llantas <= 10:
    precio_por_llanta = precio_cinco_diez
else:
    precio_por_llanta = precio_mas_diez

total_compra = cantidad_llantas * precio_por_llanta

#Mostramos el precio por llanta y el total de la compra
print(f"Precio por llanta: ${precio_por_llanta}")
print(f"Total de la compra: ${total_compra}")