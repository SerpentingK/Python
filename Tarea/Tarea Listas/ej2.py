promedio = 0
notaAlta = -1
notaBaja = 11
total = 0

while True:
    
    x = True
    
    for i in range(10):
        nota = 0
        while x:
            nota = int(input(f"Ingrese la nota {i + 1}: \n"))
            if nota < 0 or nota > 10:
                print("Nota invalida, ingrese de nuevo")
            else:
                x = False
        x = True
        if nota > notaAlta:
            notaAlta = nota
        elif nota < notaBaja:
            notaBaja = nota
        total += nota
    
    print(f"El promedio es: {total/10}")
    print(f"La nota mas alta: {notaAlta}")
    print(f"La nota mas baja: {notaBaja}")
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        break