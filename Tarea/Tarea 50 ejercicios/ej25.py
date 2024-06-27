# Ejercicio 25: Calcular la cuota que debe pagar un cliente por una fianza
monto = float(input("Ingrese el monto por el que se efectúa la fianza: "))
cuota = 0

if monto < 50000:
    cuota = monto * 0.03  # Cuota del 3% si el monto es menor a $50,000
else:
    cuota = monto * 0.02  # Cuota del 2% si el monto es mayor o igual a $50,000

print(f"Cuota a pagar por la fianza: ${cuota:.2f}")
