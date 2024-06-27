def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def obtener_dia_siguiente(dia, mes, año):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if es_bisiesto(año):
        dias_por_mes[2] = 29
    
    dia += 1
    if dia > dias_por_mes[mes]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            año += 1
    
    return dia, mes, año

# Solicitar la fecha al usuario
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

# Obtener la fecha del día siguiente
dia_siguiente, mes_siguiente, año_siguiente = obtener_dia_siguiente(dia, mes, año)

# Mostrar la fecha del día siguiente
print(f"La fecha del día siguiente es: {dia_siguiente}/{mes_siguiente}/{año_siguiente}")
