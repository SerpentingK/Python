from acertijos import Acertijos

class Juego:
    def __init__(self):
        self.acertijos = Acertijos()
        self.puntuacion = 0
        self.pistas_utilizadas = 0
        self.acertijos_resueltos = []

    def mostrar_instrucciones(self):
        print("Bienvenido al juego de acertijos. Debes resolver 5 acertijos por nivel para avanzar al siguiente nivel.")
        print("Si te atascas, puedes pedir una pista, pero cada pista utilizada restará puntos.")
        print("Buena suerte!\n")

    def mostrar_puntuacion(self):
        print(f"Tu puntuación actual es: {self.puntuacion}\n")

    def mostrar_acertijo(self, nivel, numero):
        print(f"Acertijo {numero}: {self.acertijos.obtener_acertijo(nivel, numero)}\n")

    def pedir_respuesta(self, nivel, numero):
        respuesta = input("Ingresa tu respuesta: ")
        if self.acertijos.verificar_respuesta(nivel, numero, respuesta):
            self.puntuacion += 1
            self.acertijos_resueltos.append(numero)
            print("¡Respuesta correcta!\n")
        else:
            print("Respuesta incorrecta. Inténtalo de nuevo.\n")

    def jugar_nivel(self, nivel):
        print(f"Nivel {nivel}")
        for i in range(1, 6):
            self.mostrar_acertijo(nivel, i)
            self.pedir_respuesta(nivel, i)
        self.mostrar_puntuacion()

    def jugar(self):
        self.mostrar_instrucciones()
        for nivel in range(1, 6):
            self.jugar_nivel(nivel)
            if self.pistas_utilizadas < 3:
                respuesta = input("¿Deseas usar una pista? (si/no): ")
                if respuesta.lower() == "si":
                    self.usar_pista(nivel)
                    self.pistas_utilizadas += 1
        print("¡Felicidades! Has completado todos los niveles.")

    def usar_pista(self, nivel):
        pista = self.acertijos.obtener_pista(nivel, self.pistas_utilizadas + 1)
        print(f"Pista: {pista}\n")
        self.puntuacion -= 1
