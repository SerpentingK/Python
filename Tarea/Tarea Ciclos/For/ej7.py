import time

for _ in range(5):  # Repetir 5 veces, puedes cambiar el número según lo necesites
    str = "*"
    n = int(input("Ingrese la altura de la pirámide: \n"))
    for i in range(n):
        print(str)
        str += "*"
    r = input("¿Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        time.sleep(1)
        break
