# Ejercicio 30: Calcular la cantidad de árboles a sembrar en un bosque

# Solicitamos la superficie del terreno en metros cuadrados
superficie_terreno = float(input("Ingrese la superficie del terreno en metros cuadrados: "))

# Definimos los metros cuadrados necesarios por árbol
metros_cuadrados_pino = 10
metros_cuadrados_oyamel = 15
metros_cuadrados_cedro = 18

# Calculamos la cantidad de árboles por hectárea
arboles_por_hectarea = 10000 / (metros_cuadrados_pino + metros_cuadrados_oyamel + metros_cuadrados_cedro)

# Calculamos la cantidad de árboles a sembrar
if superficie_terreno > 1000000:
    arboles_pino = 0.7 * (superficie_terreno / 10000) * arboles_por_hectarea
    arboles_oyamel = 0.2 * (superficie_terreno / 10000) * arboles_por_hectarea
    arboles_cedro = 0.1 * (superficie_terreno / 10000) * arboles_por_hectarea
else:
    arboles_pino = 0.5 * (superficie_terreno / 10000) * arboles_por_hectarea
    arboles_oyamel = 0.3 * (superficie_terreno / 10000) * arboles_por_hectarea
    arboles_cedro = 0.2 * (superficie_terreno / 10000) * arboles_por_hectarea

# Imprimimos los resultados
print(f"Número de pinos a sembrar: {arboles_pino:.0f}")
print(f"Número de oyameles a sembrar: {arboles_oyamel:.0f}")
print(f"Número de cedros a sembrar: {arboles_cedro:.0f}")
