while True:
    x = True
    cliente = 0
    d = 0
    nombre = input("Ingrese nombre del cliente: ")
    while x:
        cliente = int(input("Ingrese el tipo del cliente: "))
        if cliente <= 0 or cliente > 4:
            print("Invalido, ingrese nuevo")
        else:
            x = False
    if cliente == 1:
        d = 0.05
    elif cliente == 2:
        d = 0.08
    elif cliente == 3:
        d = 0.12
    elif cliente == 4:
        d = 0.15

    hojas = int(input(f"Ingrese la cantidad de hojas que compra el usuario {nombre}: "))
    precioHoja = 200
    totalHojas = precioHoja * hojas
    hielo = int(input(f"Ingrese la cantidad de hielo seco que compra el usuario {nombre}: "))
    precioHielo = 100
    totalHielo = precioHielo * hielo
    descuento = (totalHielo + totalHojas) * d
    total = (totalHielo + totalHojas)
    totalFinal = total - descuento

    print(f"Usuario: {nombre}\nTipo: {cliente}\nTotal por hojas: ${totalHojas}\nTotal por hielo seco: ${totalHielo}")
    print(f"Cantidad de hojas: {hojas}")
    print(f"Cantidad de hielo seco: {hielo}")
    print(f"Total compra: ${totalHielo + totalHojas}")
    print(f"Total con descuento: ${totalFinal}")
    print(f"Descuento: ${descuento}")
    r = input("Desea ingresar otro cliente?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        break