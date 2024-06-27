# Ejercicio 38: Determinar el tipo de jubilación de una persona
edad = int(input("Ingrese la edad de la persona: "))
antiguedad = int(input("Ingrese la antigüedad en años en su empleo: "))

if edad >= 60 and antiguedad < 25:
    tipo_jubilacion = "por edad"
elif edad < 60 and antiguedad >= 25:
    tipo_jubilacion = "por antigüedad joven"
elif edad >= 60 and antiguedad >= 25:
    tipo_jubilacion = "por antigüedad adulta"
else:
    tipo_jubilacion = "no aplica"

print(f"La persona quedará adscrita a la jubilación {tipo_jubilacion}.")
