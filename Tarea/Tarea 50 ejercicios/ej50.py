# Ejercicio 50: Determinar si un año es bisiesto

# Solicitar al usuario el año
año = int(input("Ingrese un año: "))

# Determinar si el año es bisiesto
if año % 4 != 0:
    es_bisiesto = False
elif año % 100 != 0:
    es_bisiesto = True
elif año % 400 == 0:
    es_bisiesto = True
else:
    es_bisiesto = False

# Mostrar el resultado
if es_bisiesto:
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")
