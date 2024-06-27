import time

while True:
    totalEstudiantes = 750

    for i in range(2024, 2036):
        totalEstudiantes += totalEstudiantes * 0.12
    print(f"El total de estudiantes en el 2035 sera de: {int(totalEstudiantes)}")

    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break
