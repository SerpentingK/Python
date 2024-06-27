def encriptar_caracter(caracter, b):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    if caracter == " ":
        return " "
    else:
        a = alfabeto.index(caracter)
        phi = (a + b) % 27
        return alfabeto[phi]

def encriptar(mensaje, b):
    mensaje_encriptado = ""
    for caracter in mensaje:
        mensaje_encriptado += encriptar_caracter(caracter, b)
    return mensaje_encriptado

def desencriptar_caracter(caracter_encriptado, b):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    if caracter_encriptado == " ":
        return " "
    else:
        phi = alfabeto.index(caracter_encriptado)
        a = (phi - b) % 27
        return alfabeto[a]

def desencriptar(mensaje_encriptado, b):
    mensaje_desencriptado = ""
    for caracter_encriptado in mensaje_encriptado:
        mensaje_desencriptado += desencriptar_caracter(caracter_encriptado, b)
    return mensaje_desencriptado

while True:
    mensaje = input("Ingrese el mensaje a encriptar: ")
    clave = int(input("Ingrese la clave de encriptación (número entero positivo): "))
    
    mensaje_encriptado = encriptar(mensaje.upper(), clave)
    print("Mensaje encriptado:", mensaje_encriptado)

    mensaje_desencriptado = desencriptar(mensaje_encriptado, clave)
    print("Mensaje desencriptado:", mensaje_desencriptado)

    continuar = input("¿Desea encriptar/desencriptar otro mensaje? (s/n): ")
    if continuar.lower() != "s":
        break
