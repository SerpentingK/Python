# Ejercicio 45: Determinar si una persona tiene anemia basándose en su nivel de hemoglobina

edad = int(input("Ingrese la edad de la persona: "))
sexo = input("Ingrese el sexo de la persona (M para masculino, F para femenino): ").upper()
nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

tiene_anemia = False

if sexo == "M":
    if edad <= 1:
        if nivel_hemoglobina < 13:
            tiene_anemia = True
    elif edad <= 6:
        if nivel_hemoglobina < 10:
            tiene_anemia = True
    elif edad <= 12:
        if nivel_hemoglobina < 11:
            tiene_anemia = True
    elif edad <= 5:
        if nivel_hemoglobina < 11.5:
            tiene_anemia = True
    elif edad <= 10:
        if nivel_hemoglobina < 12.6:
            tiene_anemia = True
    elif edad <= 15:
        if nivel_hemoglobina < 13:
            tiene_anemia = True
    else:
        if nivel_hemoglobina < 14:
            tiene_anemia = True
else:
    if edad <= 1:
        if nivel_hemoglobina < 13:
            tiene_anemia = True
    elif edad <= 6:
        if nivel_hemoglobina < 10:
            tiene_anemia = True
    elif edad <= 12:
        if nivel_hemoglobina < 11:
            tiene_anemia = True
    elif edad <= 5:
        if nivel_hemoglobina < 11.5:
            tiene_anemia = True
    elif edad <= 10:
        if nivel_hemoglobina < 12.6:
            tiene_anemia = True
    elif edad <= 15:
        if nivel_hemoglobina < 13:
            tiene_anemia = True
    else:
        if nivel_hemoglobina < 12:
            tiene_anemia = True

if tiene_anemia:
    print("La persona tiene anemia.")
else:
    print("La persona no tiene anemia.")
