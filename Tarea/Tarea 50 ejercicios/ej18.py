# Ejercicio 18: Calcular las calorías consumidas por una persona en reposo
tiempo_actividad = int(input("Ingrese el tiempo de la actividad en minutos: "))
peso_persona = 70  # Peso en kg
calorias_dormir = 1.08
calorias_reposo = 1.66

# Calculamos las calorías consumidas según la actividad
if tiempo_actividad > 0:
    actividad = input("Ingrese la actividad (dormir/reposo): ")
    if actividad.lower() == "dormir":
        calorias_consumidas = tiempo_actividad * calorias_dormir
    elif actividad.lower() == "reposo":
        calorias_consumidas = tiempo_actividad * calorias_reposo
    else:
        calorias_consumidas = 0
else:
    calorias_consumidas = 0

print(f"La cantidad de calorías consumidas es: {calorias_consumidas:.2f}")
