from funciones_nomina import calcular_valor_dia, calcular_valor_hora_basica, calcular_valor_hora_extra_diurna, calcular_valor_hora_extra_dominical, calcular_valor_hora_extra_nocturna, calcular_valor_hora_extra_festiva, calcular_total_horas_extras, calcular_descuento_dias_no_laborados, calcular_salario_total

salario_basico = float(input("Ingrese su salario basico mensual: \n"))
valor_dia = calcular_valor_dia(salario_basico)
valor_hora_basica = calcular_valor_hora_basica(valor_dia)
valorHorasExD = calcular_valor_hora_extra_diurna(valor_hora_basica)
valorHorasExN = calcular_valor_hora_extra_nocturna(valor_hora_basica)
valorHorasExDom = calcular_valor_hora_extra_dominical(valor_hora_basica)
valorHorasExF = calcular_valor_hora_extra_festiva(valor_hora_basica)

HorasExD = int(input("Ingrese horas extra diurnas: "))
HorasExN = int(input("Ingrese horas extra nocturnas: "))
HorasExDom = int(input("Ingrese horas extra dominicales: "))
HorasExF = int(input("Ingrese horas extra festivas: "))

totalHorasExtras = calcular_total_horas_extras(HorasExD, HorasExN, HorasExDom, HorasExF, valorHorasExD, valorHorasExN, valorHorasExDom, valorHorasExF)

dias_no_lab = int(input("Cuantos dias no trabajo? "))
descuento_dias_no_laborados = calcular_descuento_dias_no_laborados(dias_no_lab, valor_dia)

salario_total = calcular_salario_total(salario_basico, descuento_dias_no_laborados, totalHorasExtras)
desc = salario_total * 0.04
salario_sin_desc = salario_total - (desc * 2)

print(f"El valor de su dia de trabajo es: {valor_dia}")
print(f"El valor de su hora de trabajo es: {valor_hora_basica}")
print(f"El valor de su hora extra diruna es: {valorHorasExD}")
print(f"El valor de su hora extra nocturna es: {valorHorasExN}")
print(f"Tu salario de este mes es: {salario_total}")
print(f"Tu salario menos salud y pension es: {salario_sin_desc}")
