# Preguntar al usuario el tipo de vehículo y el número de días de alquiler
vehiculo = input("Ingrese el tipo de vehículo (BMW, MEGANE, MERCEDES, TWINGO, CHEVROLET AVEO): ")
dias_alquiler = int(input("Ingrese el número de días de alquiler: "))
seguro = input("¿Desea tomar un seguro a todo riesgo? (Si/No): ")

# Calcular el valor total del alquiler sin descuento
if vehiculo == "BMW":
    precio_base = 650000
elif vehiculo == "MEGANE":
    precio_base = 120000
elif vehiculo == "MERCEDES":
    precio_base = 700000
elif vehiculo == "TWINGO":
    precio_base = 100000
elif vehiculo == "CHEVROLET AVEO":
    precio_base = 150000
else:
    print("Vehículo no válido.")
    exit()

total_sin_descuento = precio_base * dias_alquiler

# Calcular el descuento según el número de días de alquiler
if 3 <= dias_alquiler <= 5:
    descuento = total_sin_descuento * 0.10
elif 6 <= dias_alquiler <= 10:
    descuento = total_sin_descuento * 0.15
elif dias_alquiler > 10:
    descuento = total_sin_descuento * 0.20
else:
    descuento = 0

# Aplicar el descuento
total_con_descuento = total_sin_descuento - descuento

# Calcular el costo del seguro
if seguro.lower() == "si":
    costo_seguro = total_con_descuento * 0.05
    total_con_seguro = total_con_descuento + costo_seguro
else:
    costo_seguro = 0
    total_con_seguro = total_con_descuento

# Mostrar resultados
print(f"Total de alquiler: ${total_con_seguro:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Seguro a todo riesgo: ${costo_seguro:.2f}")
print(f"Total a pagar: ${total_con_seguro:.2f}")
