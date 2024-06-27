class Nivel:
    preguntas = dict()
    puntaje = int()
    tiempo = float()
    tiempoMinimo = float()
    pistas = list()
    
    
    def __init__(self, preguntas, pistas, tiempoMinimo):
        self.preguntas = preguntas
        self.puntaje = 0
        self.pistas = pistas
        self.tiempoMinimo = tiempoMinimo
        
    def sumarPuntos(self, int):
        self.puntaje += int

