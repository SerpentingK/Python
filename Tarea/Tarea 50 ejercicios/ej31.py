# Ejercicio 31: Cálculo de sanción por contaminación en fábrica

# Solicitamos los puntos IMECA de cada día
puntos_imeca_1 = float(input("Ingrese los puntos IMECA del día 1: "))
puntos_imeca_2 = float(input("Ingrese los puntos IMECA del día 2: "))
puntos_imeca_3 = float(input("Ingrese los puntos IMECA del día 3: "))
puntos_imeca_4 = float(input("Ingrese los puntos IMECA del día 4: "))
puntos_imeca_5 = float(input("Ingrese los puntos IMECA del día 5: "))

# Calculamos el promedio de puntos IMECA
promedio_puntos_imeca = (puntos_imeca_1 + puntos_imeca_2 + puntos_imeca_3 + puntos_imeca_4 + puntos_imeca_5) / 5

# Definimos las ganancias diarias
ganancias_diarias = float(input("Ingrese las ganancias diarias de la fábrica: "))

# Verificamos si se aplica sanción y calculamos la multa
if promedio_puntos_imeca > 170:
    sancion = True
    multa = 0.5 * ganancias_diarias
else:
    sancion = False
    multa = 0

# Imprimimos los resultados
print(f"Promedio de puntos IMECA: {promedio_puntos_imeca}")
if sancion:
    print("Se detiene la producción por una semana y se aplica una multa del 50% de las ganancias diarias.")
    print(f"Multa a pagar: {multa}")
else:
    print("No se aplica sanción ni multa.")
