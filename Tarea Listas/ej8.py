tempMed = []
tempMax = []
tempMin = []

for i in range(5):
    minTemp = float(input(f"Ingrese la temperatura mínima del día {i + 1}: "))
    
    if minTemp in tempMin:
        for j in range(len(tempMin)):
            if tempMin[j] == minTemp:
                print(f"El día: {j + 1}, tuvo la misma temperatura mínima")
    else:
        print("Ningún día tuvo la misma temperatura mínima")
    
    maxTemp = float(input(f"Ingrese la temperatura máxima del día {i + 1}: "))
    
    if maxTemp in tempMax:
        for j in range(len(tempMax)):
            if tempMax[j] == maxTemp:
                print(f"El día: {j + 1}, tuvo la misma temperatura máxima")
    else:
        print("Ningún día tuvo la misma temperatura máxima")
        
    medTemp = (minTemp + maxTemp) / 2
    print(f"Temperatura media del día {i + 1}: {medTemp}")
    if medTemp in tempMed:
        for j in range(len(tempMed)):
            if tempMed[j] == medTemp:
                print(f"El día: {j + 1}, tuvo la misma temperatura media")
    else:
        print("Ningún día tuvo la misma temperatura media")
    
    tempMin.append(minTemp)
    tempMax.append(maxTemp)
    tempMed.append(medTemp)

tempMin_copy = []
for temp in tempMin:
    if temp not in tempMin_copy:
        tempMin_copy.append(temp)

menor_temp_1 = tempMin_copy[0]
menor_temp_2 = tempMin_copy[1]

for temp in tempMin_copy[2:]:
    if temp < menor_temp_1:
        menor_temp_2 = menor_temp_1
        menor_temp_1 = temp
    elif temp < menor_temp_2:
        menor_temp_2 = temp

indice_temp_1 = tempMin.index(menor_temp_1) + 1
indice_temp_2 = tempMin.index(menor_temp_2) + 1
print(f"Los dos días con la menor temperatura mínima fueron el día {indice_temp_1} y el día {indice_temp_2} con {menor_temp_1}°C y {menor_temp_2}°C respectivamente.")

tempBuscada = float(input("Ingrese la temperatura que desea buscar: "))
dias_con_temp_maxima = []

for i in range(len(tempMax)):
    if tempMax[i] == tempBuscada:
        dias_con_temp_maxima.append(i + 1)

if len(dias_con_temp_maxima) > 0:
    print(f"Los días con la misma temperatura máxima de {tempBuscada}°C fueron:")
    for dia in dias_con_temp_maxima:
        print(f"Día {dia}")
else:
    print(f"Ningún día tuvo una temperatura máxima de {tempBuscada}°C")
