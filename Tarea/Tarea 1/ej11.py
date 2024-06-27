"""
Calcular el salario que debe recibir una persona teniendo en cuenta lo siguiente, el
salario básico mensual se ingresa por teclado, el número de horas extras se ingresa por
teclado, el tipo de horas extras que puede trabajar la persona son; horas extras diurna,
el valor de una hora extra diurna corresponde a 25% más del valor de la hora normal
de trabajo, horas extras nocturnas el valor de una hora extra nocturna corresponde a
35% más del valor de la hora normal de trabajo, horas extras festivas 
"""


salarioBasico = float(input("Ingrese su salario basico mensual: \n"))
valorDia = round(salarioBasico/30 , 2)
valorHoraB = round((salarioBasico/30)/8, 2)
valorHorasExD = round(valorHoraB + (valorHoraB * 0.25), 2)
valorHorasExN = round(valorHoraB + (valorHoraB * 0.35), 2)
valorHorasExF = round(valorHoraB + (valorHoraB * 0.75), 2)
valorHorasExDom = round(valorHoraB * 2, 2)
print(f"El valor de su dia de trabajo es: {valorDia}")
print(f"El valor de su hora de trabajo es: {valorHoraB}")
print(f"El valor de su hora extra diruna es: {valorHorasExD}")
print(f"El valor de su hora extra nocturna es: {valorHorasExN}")

HorasExD = int(input("Ingrese horas extra nocturnas: "))
HorasExN = int(input("Ingrese horas extra diurnas: "))
HorasExDom = int(input("Ingrese horas extra documentales: "))
HorasExF = int(input("Ingrese horas extra festivas: "))

totalHorasExD = HorasExD * valorHorasExD
totalHorasExN = HorasExN * valorHorasExN
totalHorasExDom = HorasExDom * valorHorasExDom
totalHorasExF = HorasExF * valorHorasExF

diasNoLab = int(input("Cuantos dias no trabajo?"))
print(f"Descuento por dias no laborados: {diasNoLab * valorDia}")

salarioTotal = round((salarioBasico - (diasNoLab * valorDia)) + totalHorasExF + totalHorasExD + totalHorasExDom + totalHorasExN)

print(f"Tu salario de este mes es: {salarioTotal}")
desc = salarioTotal * 0.04
print(f"Tu salario menos salud y pension es: {salarioTotal - (desc * 2)}")