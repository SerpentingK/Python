import time

for _ in range(5):  # Repetir 5 veces, puedes cambiar el número según lo necesites
    totalEstudiantes = 750

    for i in range(2024, 2036):
        totalEstudiantes += totalEstudiantes * 0.12
    print(f"El total de estudiantes en el 2035 será de: {int(totalEstudiantes)}")

    r = input("¿Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        time.sleep(1)
        break
