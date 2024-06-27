def construir_diccionario():
    cantidad = int(input("Ingrese la cantidad de elementos a ingresar: "))
    keys = []
    values = []
    
    for i in range(cantidad):
        key = input(f"Ingrese la clave {i + 1}: ")
        value = input(f"Ingrese el valor para {key}: ")
        keys.append(key)
        values.append(value)
    
    diccionario = {}
    for i in range(cantidad):
        diccionario[keys[i]] = values[i]
    
    return diccionario

# Ejemplo de uso
diccionario = construir_diccionario()
print(diccionario)
