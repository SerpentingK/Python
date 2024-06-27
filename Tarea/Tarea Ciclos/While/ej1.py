import time

while True:
    total = 0

    for n in range(2, 160, 2):
        total += n

    print("El total es: ", total)
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break
