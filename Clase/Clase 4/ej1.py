"""
    Hacer un algoritmo de que le pida a un uusario registrarse con un nombre de usuairo y una conraseña. Debe verificar que la contraseña tenga un * un . un ? y que la cantidad de caracteres sean 8, si no cumple no debe permitir el registro. Despues va el logueo
"""

def verificar(contra):
    if "*" in contra and "." in contra and "?" in contra and len(contra) >= 8:
        return True
    else:
        return False

print("REGISTRO")
usuario = input("Ingrese su usario: ")

while True:
    contraseña = input("Ingrese su contraseña ( debe contener *, ., ?, minimo 8 caracteres): ")
    if verificar(contraseña):
        print("Perfecto")
        break
        
    else:
        print("Contraseña invalida, intente de nuevo")
    
y = True
while y:
    print("Inicio de sesion")
    x = True
    while x:
        intentoUsuario = input("Ingrese su usuario: ")
        if(intentoUsuario != usuario):
            print("Usuario no encontrado")
        else:
            x = False
    x = True
    while x:
        intentoContraseña = input("Ingrese su contraseña: ")
        if(intentoContraseña != contraseña):
            print("Contraseña incorrecta")
        else:
            x = False
            y = False

print("Iniciando sesion")
        
    