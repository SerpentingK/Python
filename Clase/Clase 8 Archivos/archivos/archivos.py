
with open('nombres.csv', 'r') as txt:
    contenido = txt.readlines()
    
    nombrelista = []
    nombre_f = []
    nombre_m = []
    c_f = 0
    c_m = 1
    c = 0
    l = input("Ingrese año de filtro: ")
    
    for i in contenido:
        x = i.split(",")
        nombre = x[3]
        if(x[2] == l):
            nombrelista.append(i)
            c += 1
            if c >= 50:
                break
            
    with open('datos.csv', 'w') as datos_txt:
        for i in nombrelista:
            datos_txt.write(i)
    