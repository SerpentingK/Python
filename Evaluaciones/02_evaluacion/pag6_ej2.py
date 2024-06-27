def edad_promedio_por_nombre(lista):
    diccionario_edad_promedio = {}
    diccionario_cantidad_por_nombre = {}

    for nombre, edad in lista:
        if nombre in diccionario_edad_promedio:
            diccionario_edad_promedio[nombre] += edad
            diccionario_cantidad_por_nombre[nombre] += 1
        else:
            diccionario_edad_promedio[nombre] = edad
            diccionario_cantidad_por_nombre[nombre] = 1

    for nombre, edad_total in diccionario_edad_promedio.items():
        cantidad = diccionario_cantidad_por_nombre[nombre]
        diccionario_edad_promedio[nombre] = edad_total / cantidad

    return diccionario_edad_promedio

# Ingreso de datos
num_personas = int(input("Ingrese el número de personas: "))
lista_personas = []
for _ in range(num_personas):
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    lista_personas.append([nombre, edad])

# Llamada a la función e impresión del resultado
resultado = edad_promedio_por_nombre(lista_personas)
print(resultado)
