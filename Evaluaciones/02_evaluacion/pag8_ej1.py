def ordenar_palabras_por_longitud(lista_palabras):
    return sorted(lista_palabras, key=len, reverse=True)

# Ingreso de datos
num_palabras = int(input("Ingrese el número de palabras: "))
lista_palabras = []
for _ in range(num_palabras):
    palabra = input("Ingrese una palabra: ")
    lista_palabras.append(palabra)

# Llamada a la función e impresión del resultado
resultado = ordenar_palabras_por_longitud(lista_palabras)
print(resultado)
