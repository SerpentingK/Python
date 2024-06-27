def palabras_con_vocales(lista_palabras):
    vocales = ['a', 'e', 'i', 'o', 'u']
    palabras_con_vocales = {}

    for palabra in lista_palabras:
        solo_vocales = True
        for letra in palabra:
            if letra.lower() not in vocales:
                solo_vocales = False
                break
        if solo_vocales:
            for letra in palabra:
                if letra.lower() in palabras_con_vocales:
                    palabras_con_vocales[letra.lower()].append(palabra)
                else:
                    palabras_con_vocales[letra.lower()] = [palabra]

    return palabras_con_vocales

# Ingreso de datos
num_palabras = int(input("Ingrese el número de palabras: "))
lista_palabras = []
for _ in range(num_palabras):
    palabra = input("Ingrese una palabra: ")
    lista_palabras.append(palabra)

# Llamada a la función e impresión del resultado
resultado = palabras_con_vocales(lista_palabras)
print(resultado)
