import json

with open('ej_1/csv/GLOBANT.csv', 'r') as datos:
    contenido = datos.readlines()

with open('ej_1/csv/analisis_archivo.csv', 'w') as analisis:
    analisis.write("Fecha\tComportamiento de la accion\tPunto medio HIGH-LOW\n")
    fecha_menor = ""
    fecha_mayor = ""
    menor = 999999
    mayor = -1
    c_sube = 0
    c_baja = 0
    c_estable = 0
    for i in contenido[1:]:
        x = i.split(",")
        fecha = x[0]
        comportamiento = ""
        if float(x[4]) - float(x[1]) > 0:
            comportamiento = "SUBE"
            c_sube +=1
        elif float(x[4]) - float(x[1]) < 0:
            comportamiento = "BAJA"
            c_baja += 1
        elif float(x[4]) - float(x[1]) == 0:
            comportamiento = "ESTABLE"
            c_estable += 1
            
        punto_medio = float(x[2]) - float(x[3])/2
        
        analisis.write(f"{fecha}\t{comportamiento}\t{round(punto_medio, 2)}\n")
        
        if float(x[3]) < menor:
            menor = float(x[3])
            fecha_menor = x[0]
        if float(x[2]) > mayor:
            mayor = float(x[2])
            fecha_mayor = x[0]
    md = {
        "date_lowest_price": fecha_menor,
        "lowest_price": menor,
        "date_highest_price": fecha_mayor,
        "highest_price": mayor,
        "cantidad_sube": c_sube,
        "cantidad_baja": c_baja,
        "cantidad_estable": c_estable
    }
    
    with open('ej_1/json/detalles.json', 'w') as archivo:
        json.dump(md, archivo)
        
    print("Se han ejecutado creectamente el programa")
        
