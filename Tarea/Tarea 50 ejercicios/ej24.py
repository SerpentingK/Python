# Ejercicio 24: Calcular las pulsaciones por cada 10 segundos de ejercicio
sexo = input("Ingrese su sexo (Femenino/Masculino): ").lower()
edad = int(input("Ingrese su edad: "))
pulsaciones = 0

if sexo == "femenino":
    pulsaciones = (220 - edad) / 10
elif sexo == "masculino":
    pulsaciones = (210 - edad) / 10

print(f"Número de pulsaciones por cada 10 segundos de ejercicio: {pulsaciones}")
