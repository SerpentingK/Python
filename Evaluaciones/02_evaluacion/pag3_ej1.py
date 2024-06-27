def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def obtener_primos(lista_numeros):
    primos = {}
    for numero in lista_numeros:
        primos[numero] = es_primo(numero)
    return primos

# Ejemplo de uso
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = obtener_primos(numeros)
print(resultado)
