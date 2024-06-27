
#variables
lista = list()
aptas = list()

n = int(input("Ingrese numero de bicicletas: "))
for i in range(n):
    info = input(f"Ingrese info bicicleta {i + 1}: ")
    
    datos = [int(dato) for dato in info.split()]
    dic = {
        "eje" : datos[0],
        "bielas" : datos[1],
        "longitud" : datos[2],
        "manilar" : datos[3],
        "precio" : datos[4]
    }
    lista.append(dic)
    
for dic in lista:
    if dic["eje"] <= 300 and dic["eje"] >= 240:
        if dic["bielas"] <= 180 and dic["bielas"] >= 160:
            if dic["longitud"] <= 275 and dic["longitud"] >= 240:
                if dic["manilar"] <= 50:
                    aptas.append(dic)
    
for dic in aptas:
    print(f"Precio: {dic["precio"]}")


#220 170 258 48 12000
#250 170 258 48 12000
#250 200 258 48 12000