poderes = []
castigos = []
monedasPlata = 0
monedasOro = 0
respuestasCorrectas = 0

preguntasNivel1 = ["Si el mono tiene 3 manzanas y se come 2 cuantas le quedan?",
                   "Si el rinoceronte destruye pisa 1 flor mientras camina, cuantas flores piso?",
                   "Si el tucan ve dos turistas en la selva, y ve que solo se va uno, cuantos turistas hay en la selva?",
                   "Si la leona tiene 3 cachorros, y dos se escapan, cuantos cachorros estan con la leona?",
                   "Cuantas reinas abejas hay en un panal?"]
preguntasNivel2 = ["Si la siguiente isla se encuentra a 25° - 20° a la derecha, a cuantos grados se encuentra?",
                   "Cuanto es 15 menos 10?",
                   "Cuanto es 35 menos 30",
                   "Cuanto es 45 dividido 9",
                   "Cuanto es 50 dividido 10"]
preguntasNivel3 = ["Cuanto 3 x 2?", "Cuanto es 12/2?", "Cuanto es 36/6?", "Cuanto es 30 - 24?", "Cuanto es 60/10?"]

def mostrarDatos():
    print("Poderes actuales: ")
    for i in poderes:
        print(i)
    print(f"Monedas de plata actuales: ${monedasPlata}")
    print(f"Monedas de oro actuales: {monedasOro}")
    
def sumarMonedas(v, i):
    global monedasPlata
    global monedasOro
    if i == 1:
        monedasPlata += v
    elif i == 2:
        monedasOro += v
def nivel1():
    global respuestasCorrectas
    print("----Nivel 1----")
    print("----Selva oscura----")
    for i in preguntasNivel1:
        print(f"----Pregunta {preguntasNivel1.index(i) + 1}:")
        print(i)
        r = int(input("Ingrese su respuesta: "))
        if r == 1:
            sumarMonedas(5000, 1)
            respuestasCorrectas += 1
            print("Perfecto, has ganado 5000 monedas.")
        else:
            print("Respuesta incorrecta")
    if respuestasCorrectas >= 2:
        sumarMonedas(20000, 1)
        poderes.append("Daga de la Tribu")
        print("Has pasado el nivel 1. Ganaste 20000")
        print(f"Respuestas correctas: {respuestasCorrectas}")
        print(f"Respuestas incorrectas: {5 - respuestasCorrectas}")
        nivel2()
    else:
        print("Has quedado perdido en la selva")

def nivel2():
    respuestasCorrectas = 0
    mostrarDatos()
    print("----Nivel 2----")
    print("----Rio de las mentiras----")
    for i in preguntasNivel2:
        print(f"----Pregunta {preguntasNivel2.index(i) + 1}:")
        print(i)
        r = int(input("Ingrese su respuesta: "))
        if r == 5:
            sumarMonedas(10000, 1)
            respuestasCorrectas += 1
            print("Perfecto, has ganado 10000 monedas.")
        else:
            print("Respuesta incorrecta")
    if respuestasCorrectas >= 3:
        sumarMonedas(30000, 1)
        poderes.append("Mapa de los templos")
        print("Has pasado el nivel 2.")
        print(f"Respuestas correctas: {respuestasCorrectas}")
        print(f"Respuestas incorrectas: {5 - respuestasCorrectas}")
        nivel3()
    else:
        mostrarDatos()
        if monedasPlata >= 40000:
            print("No has logrado pasar el segundo nivel")
            print("Deseas pagar 40000 monedas para poder seguir con tu aventura?")
            r = input()
            if r.lower() == "si":
                sumarMonedas(-40000)
                print(f"Respuestas correctas: {respuestasCorrectas}")
                print(f"Respuestas incorrectas: {5 - respuestasCorrectas}")
                nivel3()
def nivel3():
    respuestasCorrectas = 0
    mostrarDatos()
    print("----Nivel 3----")
    print("----En busca del amuleto ancestral----")
    for i in preguntasNivel3:
        print(f"----Pregunta {preguntasNivel3.index(i) + 1}:")
        print(i)
        r = int(input("Ingrese su respuesta: "))
        if r == 6:
            sumarMonedas(20000, 2)
            respuestasCorrectas += 1
            print("Perfecto, has ganado 20000 monedas.")
        else:
            print("Respuesta incorrecta")
    if 3 <= respuestasCorrectas < 5:
        mostrarDatos()
        if monedasPlata >= 60000:
            r = input("Deseas pagar 60k y regresar al nivel 1?")
            if r.lower() == "si":
                nivel1()
            else:
                if monedasPlata >= 120000:
                    r = input("Deseas pagar 120000 y regresar al nivel 2?")
                    if r.lower() == "si":
                        nivel2()
                    else:
                        print("Has perdido")
    else:
        mostrarDatos()
        sumarMonedas(100000, 2)
        poderes.append("Amuleto ancestral")
        print("Has pasado el nivel 3.")
        print(f"Respuestas correctas: {respuestasCorrectas}")
        print(f"Respuestas incorrectas: {5 - respuestasCorrectas}")
        nivel4()         
def nivel4():
    respuestasCorrectas = 0
    mostrarDatos()
    print("----Nivel 4----")
    print("----En busca de la lanza sagrada----")
    print("De que color eran las mangas blancas del chaleco de simon bolivar?")
    print("1. Blancas")
    print("2. Negras")
    print("3. Ninguna")
    r = int(input("Ingrese su respuesta: "))
    
    if r == 3:
        respuestasCorrectas += 1
    
    print("Cual fue el ultimo animal en subir al arca de moises?")
    print("1. Delfin")
    print("2. Vaca")
    print("3. Ninguna")
    r = int(input("Ingrese su respuesta: "))
    
    if r == 3:
        respuestasCorrectas += 1
        
    if respuestasCorrectas == 1:
        if monedasOro >= 160000 and monedasPlata >= 40000:
            r = input("Deseas pagar 160k de oro y 40k de plata y regresar al nivel 1?")
            if r.lower() == "si":
                nivel1()
    if respuestasCorrectas == 2:
        sumarMonedas(1000000, 2)
        print("Has pasado el nivel 4")
        poderes.append("Lanza sagrada")
        nivel5()
        print(f"Respuestas correctas: {respuestasCorrectas}")
        print(f"Respuestas incorrectas: {2 - respuestasCorrectas}")

def nivel5():
    respuestasCorrectas = 0
    mostrarDatos()
    print("----Nivel 5----")
    print("----La batalla final----")
    print("De que color eran las mangas blancas del chaleco de simon bolivar?")
    print("1. Blancas")
    print("2. Negras")
    print("3. Ninguna")
    r = int(input("Ingrese su respuesta: "))
    
    if r == 3:
        respuestasCorrectas += 1
    
    print("Cual fue el ultimo animal en subir al arca de moises?")
    print("1. Delfin")
    print("2. Vaca")
    print("3. Ninguna")
    r = int(input("Ingrese su respuesta: "))
    
    if r == 3:
        respuestasCorrectas += 1
        
    print("Cual fue el ultimo animal en subir al arca de moises?")
    print("1. Delfin")
    print("2. Vaca")
    print("3. Ninguna")
    r = int(input("Ingrese su respuesta: "))
    
    if r == 3:
        respuestasCorrectas += 1
        
    if respuestasCorrectas == 3:
        print("Eres el maestro explorador!")
        poderes.append("Poderes del señor oscuro")
        if(len(poderes) == 5):
            print("Eres un super sagrado")
            mostrarDatos()
    else:
        if(monedasPlata >= 200000 and monedasOro >= 1000000):
            r = input("Has sido derrotado por la oscuridad, deseas pagar 1000k de oro y 200k de plata y volver al nivel 1?")
            if r.lower() == "si":
                nivel1()
nivel1()