import random
import time


list = []
for i in range(10):
    r = random.randint(1, 10)
    list.append(r)
print(list)

for j in list:
    cuadrado = j ** 2
    cubo = j ** 3
    print(f"Numero: {j} Cuadrado: {cuadrado} Cubo: {cubo}")
        
    

    