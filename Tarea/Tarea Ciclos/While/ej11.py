vendedores = ["Juan", "María", "Pedro", "Luis", "Ana", "Carlos", "Sofía", "Javier", "Laura", "Diego"]
autos_vendidos = [5, 8, 10, 12, 15, 7, 9, 11, 6, 13]
salario_minimo = 1000000
valor_por_auto = 100000

sueldos = []
i = 0
while i < len(vendedores):
    sueldo = salario_minimo + valor_por_auto * autos_vendidos[i] + 0.02 * autos_vendidos[i]
    sueldos.append(sueldo)
    i += 1

indice_max = sueldos.index(max(sueldos))
print(f"El vendedor con el sueldo más alto es: {vendedores[indice_max]}")
