def divisores(n1, n2):
    if n1 % n2 != 0:
        print(f"{n2} no es divisor de {n1}")
    else:
        print(f"{n2} es divisor de {n1}")

num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))

divisores(num1, num2)
