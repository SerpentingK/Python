import time
from Niveles import lista_niveles

puntajeTotal = 0

print("-------------------------------------------------------------------------------------")
print("Instrucciones:")
print("Respinde correctamente al menos 3 preguntas para pasar al siguiente nivel.")
print("Si respondes al menos 4 preguntas correctamente en menos del tiempo minimo recibira una recompensa.")
print("Si no logras pasar algun nivel, el tiempo no dejara de correr.")
print("Si no logras pasar un nivel, se te ofrecera una pista a una pregunta en especifico.")
print("-------------------------------------------------------------------------------------")
for i in lista_niveles:
    print(f"NIVEL: {lista_niveles.index(i) + 1}")
    print(f"TIEMPO MINIMO: {i.tiempoMinimo} segundos")
    print("-------------------------------------------------------------------------------------")
    input("Presione enter para empezar. \n")
    tiempoInicio = time.time()
    x = False
    while not(x):
        for j in i.preguntas:
            print(j)
            r = input()
            if r.lower() == i.preguntas[j].lower():
                print("Correcto, mas un punto.")
                i.sumarPuntos(1)
                print(f"Puntaje: {i.puntaje}")
            else:
                print("Respuesta incorrecta.")
                print(f"Puntaje: {i.puntaje}")
                
        if i.puntaje < 3:
            print("No has alcanzado el puntaje necesario")
            print(f"Puntaje: {i.puntaje}")
            r = input("¿Deseas una pista?\n")
            if r.lower() == "si":
                r = int(input("¿Que numero de pregunta deseas la pista?"))
                if r > 5 or r < 1:
                    print("Valor invalido, perdiste tu pista")
                else:
                    print(i.pistas[r - 1])
            i.puntaje
        else:
            print("Has pasado al siguiente nivel.")
            print(f"Puntaje: {i.puntaje}")
            tiempoFinal = time.time()
            i.tiempo = (tiempoFinal - tiempoInicio)
            
            if i.tiempo < i.tiempoMinimo and i.puntaje >= 4:
                print("Has demorado menos que el tiempo minimo y tuviste al menos 4 respuestas correctas. Ganas dos puntos")
                i.sumarPuntos(2)
                print(f"Puntaje: {i.puntaje}")
            x = True

for i in lista_niveles:
    print(f"Puntaje nivel {lista_niveles.index(i) + 1}: {i.puntaje}")
    puntajeTotal += i.puntaje
    
print(f"Puntaje total: {puntajeTotal}")

