def agrupar_nombres_por_letra():
    nombres = input("Ingrese una lista de nombres separados por espacios: ").split()
    nombres_agrupados = {}
    for nombre in nombres:
        inicial = nombre[0]
        if inicial in nombres_agrupados:
            nombres_agrupados[inicial].append(nombre)
        else:
            nombres_agrupados[inicial] = [nombre]
    return nombres_agrupados

# Ejemplo de uso
resultado = agrupar_nombres_por_letra()
print(resultado)
