# Solicitar al usuario que ingrese la cantidad de dólares y el tipo de cambio
cantidad_dolares = float(input("Ingrese la cantidad de dólares a comprar: "))
tipo_cambio = float(input("Ingrese el tipo de cambio (costo de un dólar en pesos): "))

# Calcular la cantidad a pagar en pesos
cantidad_pesos = cantidad_dolares * tipo_cambio

# Mostrar la cantidad a pagar en pesos
print("La cantidad a pagar en pesos es:", cantidad_pesos)
