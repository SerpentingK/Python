import time
str = "*"
while True:
    n = int(input("Ingrese la altura de la piramide: \n"))
    for i in range(n):
        print(str)
        str += "*"
        r = input("Desea ejecutar otra vez?\n")
        if r.lower() == "si":
            print("Ejecutando")
        else:
            print("Finzalizando condigo")
            time.sleep(1)
            break