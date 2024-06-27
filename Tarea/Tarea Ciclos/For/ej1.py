import time

for _ in range(5):  # Repetir 5 veces, puedes cambiar el número según lo necesites
    total = 0

    for n in range(2, 160, 2):
        total += n

    print("El total es: ", total)
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        time.sleep(1)
        break
