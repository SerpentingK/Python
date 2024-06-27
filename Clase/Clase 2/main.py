options = ["1. Insertar usuario en lista", "2. Actualizar usuario de la lista", "3. Buscar usuario en lista", "4. Eliminar un usuario de la lista", "5. Consultar la lista", "6. Salir"]
print("¡BIENVENIDO!\nMENU:")
users = ["Juan", "Pedro", "Mateo", "Kevin"]
while True:
    for i in options:
        print(i)
    election = int(input("Ingrese que accion desea ejecutar: "))
    if election == 1:
        newUser = input("Ingrese el usuario que desea ingresar: ")
        users.append(newUser)
        input("Presione enter para continuar")
    elif election == 2:
        print("Lista Actual: ")
        for i in range(users.__len__()):
            print(i + 1, f". {users[i]}")
        while True:
            ind = int(input("Ingrese el numero del usuario que desea Actualizar: "))
            if ind < 0 or ind > users.__len__():
                print("Valor invalido, ingrese de nuevo")
            else:
                newAct = input("Ingrese el nuevo usuario: ")
                users[ind - 1] = newAct
                break
        input("Presione enter para continuar")
    elif election == 3:
        userSearch = input("Ingrese usuario que desea buscar: ")
        if userSearch in users:
            print("Se encuentra en la lista")
            print("Posicion: ", users.index(userSearch) + 1)
        else:
            print("No se encuentra en la lista")

        input("Presione enter para continuar")
    elif election == 4:
        print("Lista Actual: ")
        for i in range(users.__len__()):
            print(i + 1, f". {users[i]}")
        while True:
            userDel = input("Ingrese el usuario que desea eliminar: ")
            if userDel in users:
                users.remove(userDel)
                break
            else:
                print("Usuario inexistente, ingrese de nuevo")
        print("Usuario eliminado")
        input("Presione enter para continuar")
    elif election == 5:
        print("Lista Actual: ")
        for i in range(users.__len__()):
            print(i + 1, f". {users[i]}")
    elif election == 6:
        break
    else:
        print("Opcion invalida ingrese de nuevo")