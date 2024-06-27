# Ejercicio 16: Calcular los intereses y saldo final de una inversión en el banco
inversion_inicial = float(input("Ingrese la cantidad inicial de la inversión en el banco: "))
intereses_generados = 0

# Calculamos los intereses generados
if inversion_inicial > 0:
    intereses_generados = inversion_inicial * 0.04  # Suponiendo una tasa de interés del 4%

# Calculamos el saldo final
saldo_final = inversion_inicial + intereses_generados

# Verificamos si se reinvierten los intereses
if intereses_generados > 70000:  # Se reinvierten si superan $70,000
    saldo_final += intereses_generados

print(f"Los intereses generados son: ${intereses_generados:.2f}")
print(f"El saldo final de la inversión es: ${saldo_final:.2f}")
