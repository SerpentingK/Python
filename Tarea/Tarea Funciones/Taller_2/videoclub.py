def calcular_total(precio1, precio2, precio3):
    # Ordenar los precios de menor a mayor
    precios_ordenados = sorted([precio1, precio2, precio3])
    
    # Calcular el total a pagar
    total = precios_ordenados[0] + precios_ordenados[1]
    
    return total

# Solicitar los precios de las películas al usuario
precio1 = float(input("Precio de la primera pelicula: "))
precio2 = float(input("Precio de la segunda pelicula: "))
precio3 = float(input("Precio de la tercera pelicula: "))

# Calcular el total a pagar y mostrarlo al usuario
total = calcular_total(precio1, precio2, precio3)
print(f"Total a pagar: ${total:.2f}")
