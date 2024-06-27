# Ejercicio 29: Calcular el préstamo bancario para iniciar un negocio
monto_hipoteca = float(input("Ingrese el monto de la hipoteca: "))
saldo_cuenta = float(input("Ingrese el saldo de su cuenta bancaria: "))

if monto_hipoteca < 100000000:
    inversion_propia = monto_hipoteca * 0.5
    inversion_socio = monto_hipoteca * 0.5
else:
    inversion_propia = monto_hipoteca
    inversion_socio = (saldo_cuenta + inversion_propia) / 2

print(f"Inversión propia: ${inversion_propia:.2f}")
print(f"Inversión del socio: ${inversion_socio:.2f}")
