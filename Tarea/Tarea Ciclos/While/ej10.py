import time

while True:
    x = int(input("Ingrese el numero minimo del rango: \n"))
    y = int(input("Ingrese el numero maximo dle rango: \n"))
    numeros_primos = []
    for num in range(x, y + 1):
        if num > 1:
            es_primo = True
            for i in range(2, num):
                if (num % i) == 0:
                    es_primo = False
                    break
            if es_primo:
                numeros_primos.append(num)


    cantidad_primos = len(numeros_primos)
    print(f"En el rango de {x} a {y} hay {cantidad_primos} números primos:")
    print(numeros_primos)
    r = input("Desea ejecutar otra vez?\n")
    if r.lower() == "si":
        print("Ejecutando")
    else:
        print("Finzalizando condigo")
        time.sleep(1)
        break