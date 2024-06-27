import time


lista = [3,3,4,3,4,3]

while True:
    print("Elija su opcion")
    print("1. Añadir numero a la lista")
    print("2. Añadir numero a la lista en posicion")
    print("3. Longitud de la lista")
    print("4. Eliminar ultimo numero")
    print("5. Eliminar un numero en posicion")
    print("6. Contar numeros")
    print("7. Posiciones de un numero")
    print("8. Mostrar lista")
    
    r = int(input(""))
    if r == 1:
        nuevo = int(input("Ingrese el numeor a agregar: "))
        lista.append(nuevo)
    elif r == 2:
        if len(lista) > 0:
            print(lista)
            modif = int(input("Ingrese el indice del valor que quiere modificar: "))
            if modif > len(lista):
                print("Excede el largo de la lista")
            else:
                nuevo = int(input("Ingrese el numero que desea añadir: "))
                lista[modif] = nuevo
        else:
            print("Lista vacia, añada un numero primero")
    elif r == 3:
        print(f"Longitud actual de la lista: {len(lista)}")
    elif r == 4:
        print(f"Ultimo numero de la lista: {lista[len(lista) - 1]}") 
        print("Eliminado")
        lista.remove(lista[len(lista) - 1])
        print(lista)
    elif r == 5:
        if len(lista) > 0:
            print(lista)
            elim = int(input("Ingrese el indice del valor que quiere eliminar: "))
            if elim > len(lista):
                print("Excede el largo de la lista")
            else:
                lista.remove(lista[elim - 1])
                
            print(lista)
        else:
            print("Lista vacia, añada un numero primero")
    elif r == 6:
        repetido = 0
        if len(lista) > 0:
            contar = int(input("Ingrese el numero que desea buscar: "))
            if contar in lista:
                for i in lista:
                    if i == contar:
                        repetido += 1
            else:
                print("Numero no se encuentra en lista")
        else:
            print("Lista vacia, añada un numero primero")
    elif r == 7:
        pos = 1
        posiciones = []
        if len(lista) > 0:
            buscar = int(input("Ingrese el numero que desea saber en cuantas posiciones esta: "))
            if buscar in lista:
                for i in lista:
                    
                    if i == buscar:
                        posiciones.append(pos)
                    pos += 1
                print(posiciones)
                print(f"Su numero se encuentra en las siguientes posiciones: ", end=" ")
                for i in posiciones:
                    print(i, end=" ")
                print(".")
            else:
                print("Numero no se encuentra en lista")
        else:
            print("Lista vacia, añada un numero primero")
    elif r == 8:
        print(f"Lista actual: {lista}")
    elif r == 9:
        print("Cerrando")
        time.sleep(1)
        
        
