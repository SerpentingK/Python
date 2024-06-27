from clases import Estudiante

nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
estudiante = Estudiante(nombre, edad, list())

while True:
    nuevaCalif = float(input("Ingrese calificacion: "))
    estudiante.add_calificaciones(nuevaCalif)
    r = input("Desea añadir calificacion? ")
    if r.lower() == "si":
        continue
    else:
        break

print(f"Calificaciones: {estudiante.get_calificaciones()}")
print(f"Promedio: {estudiante.cal_promedio()}")