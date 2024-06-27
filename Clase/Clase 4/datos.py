from funciones.operaciones import salario_horas_extras, descuento_dias_no_trabajados, seguridad_social

salario = int(input("Ingrese su salario basico: "))
nhed = int(input("Horas extras diurnas: "))
nhen = int(input("Horas extras nocturnas: "))
nhef = int(input("Horas extras festivas: "))
nhedo = int(input("Horas extras dominicales: "))

ndnt = int(input("Numero de dias no trabajados: "))


she = salario_horas_extras(salario, nhed, nhen, nhef, nhedo)
ddnt = descuento_dias_no_trabajados(salario, ndnt)

ti = she - ddnt
ss = seguridad_social(ti)

print(f"Salario total: ${ti - ss}")