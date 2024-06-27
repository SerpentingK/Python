def numeros_pares_impares():
    pares = []
    impares = []
    for _ in range(10):
        num = int(input("Introduce un número entero: "))
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    print("Números pares:", pares)
    print("Números impares:", impares)

def numeros_perfectos():
    def es_numero_perfecto(num):
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        return suma == num

    num_perfectos = []
    num = 1
    while len(num_perfectos) < 100:
        if es_numero_perfecto(num):
            num_perfectos.append(num)
        num += 1
    return num_perfectos

def invertir_digitos(num):
    if num < 1000 or num > 9999:
        return "El número debe tener cuatro dígitos."
    else:
        return int(str(num)[::-1])

while True:
    print("\nMenú de opciones:")
    print("1. Determinar números pares e impares.")
    print("2. Obtener los primeros 100 números perfectos.")
    print("3. Invertir los dígitos de un número de cuatro dígitos.")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        numeros_pares_impares()
    elif opcion == 2:
        print("Los primeros 100 números perfectos son:", numeros_perfectos())
    elif opcion == 3:
        num = int(input("Introduce un número de cuatro dígitos: "))
        print("Número con los dígitos invertidos:", invertir_digitos(num))
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")
