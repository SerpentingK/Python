# Ejercicio 51: Calcular el día siguiente

# Solicitar al usuario el día, mes y año
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

# Incrementar el día
dia += 1

# Determinar si el año es bisiesto y ajustar el número de días en febrero
es_bisiesto = (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))
dias_febrero = 29 if es_bisiesto else 28

# Ajustar el día y el mes si es necesario
if dia > 31 or (mes == 2 and dia > dias_febrero) or (mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30):
    dia = 1
    mes += 1
    if mes > 12:
        mes = 1
        año += 1

# Mostrar el día siguiente
print("El día siguiente es:", dia, "/", mes, "/", año)
