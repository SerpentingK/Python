"""
Calcular la calificación final de un estudiante. Los datos disponibles para lectura son
calificación 1, equivale al 30% de la nota final, calificacion2, equivale al 20% de la nota
final, calificacion3, equivale al 10% de la nota final, calificacion4, equivale al 40% de la
nota final de cada uno de los cuatro exámenes presentados. La información que se debe
imprimir es el promedio de las calificaciones.
"""
#Declaro variables para calificaciones
c1 = c2 = c3 = c4 = 0

ct : float

x: bool = False
print("Las notas son de 1 a 10")
while not x:
    c1 = int(input("Ingrese su primera calificacion: "))
    if c1 < 0 or c1 > 10:
        print("Valor invalido, ingrese de nuevo")
    else:
        break
while not x:
    c2 = int(input("Ingrese su segunda calificacion: "))
    if c2 < 0 or c2 > 10:
        print("Valor invalido, ingrese de nuevo")
    else:
        break
while not x:
    c3 = int(input("Ingrese su tercer calificacion: "))
    if c3 < 0 or c3 > 10:
        print("Valor invalido, ingrese de nuevo")
    else:
        break
while not x:
    c4 = int(input("Ingrese su cuarta calificacion: "))
    if c4 < 0 or c4 > 10:
        print("Valor invalido, ingrese de nuevo")
    else:
        break

c1 = c1 * 0.3
c2 = c2 * 0.2
c3 = c3 * 0.1
c4 = c4 * 0.4

ct = c1 + c2 + c3 + c4

print(f"Su calificacion total es: {round(ct, 2)}")


