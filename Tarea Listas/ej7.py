alumnos = []
mayores_de_edad = []
alumno_mayor = None
edad_mayor = 0

while True:
    nombre = input("Introduce el nombre del alumno (o * para terminar): ")
    if nombre == "*":
        break
    edad = int(input("Introduce la edad de " + nombre + ": "))
    alumnos.append((nombre, edad))
    if edad >= 18:
        mayores_de_edad.append((nombre, edad))
    if edad > edad_mayor:
        alumno_mayor = nombre
        edad_mayor = edad

print("\nAlumnos mayores de edad:")
for nombre, edad in mayores_de_edad:
    print(nombre, "-", edad, "años")

print("\nAlumno mayor:")
print(alumno_mayor, "-", edad_mayor, "años")


 

