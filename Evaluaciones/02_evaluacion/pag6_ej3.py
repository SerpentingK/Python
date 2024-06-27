def contar_letras(cadena):
    diccionario_letras = {}

    for letra in cadena:
        if letra != ' ':
            if letra in diccionario_letras:
                diccionario_letras[letra] += 1
            else:
                diccionario_letras[letra] = 1

    return diccionario_letras

# Ingreso de datos
cadena = input("Ingrese una cadena de texto: ")

# Llamada a la función e impresión del resultado
resultado = contar_letras(cadena)
print(resultado)
