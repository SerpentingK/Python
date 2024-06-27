meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

while True:
    numero_mes = int(input("Introduce un número de mes (1-12): "))
    if 1 <= numero_mes <= 12:
        nombre_mes = meses[numero_mes - 1]
        if numero_mes == 2:
            dias = 28
        elif numero_mes in [4, 6, 9, 11]:
            dias = 30
        else:
            dias = 31
        print(f"El mes de {nombre_mes} tiene {dias} días.")
    else:
        print("Número de mes inválido. Debe estar entre 1 y 12.")

    r = input("Desea ejecutar otra vez?\n")
    if r.lower() != "si":
        print("Finalizando código")
        break
