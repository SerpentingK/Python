# Ejercicio 43: Calcular el precio a pagar por la compra de manzanas en una frutería
kilos_comprados = float(input("Ingrese la cantidad de kilos de manzanas comprados: "))

if kilos_comprados <= 2:
    descuento = 0
elif 2.01 <= kilos_comprados <= 5:
    descuento = 0.1
elif 5.01 <= kilos_comprados <= 10:
    descuento = 0.15
else:
    descuento = 0.2

precio_kilo = 50  # Precio ficticio para el ejemplo
precio_sin_descuento = kilos_comprados * precio_kilo
descuento_aplicado = precio_sin_descuento * descuento
precio_final = precio_sin_descuento - descuento_aplicado

print(f"El precio final a pagar por {kilos_comprados} kilos de manzanas es: ${precio_final:.2f}")
