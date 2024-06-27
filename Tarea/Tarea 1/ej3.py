# Solicitar al usuario que ingrese los datos del terreno
ancho = float(input("Ingrese el ancho del terreno en metros: "))
largo = float(input("Ingrese el largo del terreno en metros: "))
costo_por_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado en la moneda deseada: "))

# Calcular el área del terreno
area = ancho * largo

# Calcular el costo total del terreno
costo_total = area * costo_por_metro_cuadrado

# Mostrar el costo total del terreno
print("El costo total del terreno es:", costo_total, "en la moneda deseada")

