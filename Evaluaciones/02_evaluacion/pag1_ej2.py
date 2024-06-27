def longitud_palabras():
    cadena = input("Ingrese una lista de palabras: ")
    palabra = ""
    longitud_palabras = {}
    for caracter in cadena:
        if caracter != " ":
            palabra += caracter
        else:
            longitud_palabras[palabra] = len(palabra)
            palabra = ""
    # Agregar la última palabra si no se ha agregado
    if palabra:
        longitud_palabras[palabra] = len(palabra)
    return longitud_palabras

# Ejemplo de uso
resultado = longitud_palabras()
print(resultado)
