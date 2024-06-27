class Acertijos:
    def __init__(self):
        self.acertijos_respuestas = {
            1: [
                {"acertijo": "Tiene ojos y no puede ver, tiene un corazón y no puede amar, ¿qué es?", "respuesta": "un espantapájaros"},
                {"acertijo": "Aunque se baña todos los días, no se puede secar, ¿qué es?", "respuesta": "el pez"},
                {"acertijo": "Siempre sube y nunca baja, ¿qué es?", "respuesta": "la edad"},
                {"acertijo": "Cuanto más se seca, más mojada está, ¿qué es?", "respuesta": "una toalla"},
                {"acertijo": "Vuela sin alas, llora sin ojos. ¿Qué es?", "respuesta": "la nube"}
            ],
            2: [
                {"acertijo": "Tiene hojas pero no es un árbol, tiene una cara pero no es una persona, ¿qué es?", "respuesta": "el libro"},
                {"acertijo": "Cuanto más le quitas, más grande se vuelve, ¿qué es?", "respuesta": "un agujero"},
                {"acertijo": "Se rompe al nombrarlo, ¿qué es?", "respuesta": "el silencio"},
                {"acertijo": "Tiene agujas pero no puede coser, ¿qué es?", "respuesta": "un reloj"},
                {"acertijo": "Es pequeño como un ratón, pero guarda la casa como un león, ¿qué es?", "respuesta": "la cerradura"}
            ],
            3: [
                {"acertijo": "Nunca se moja aunque llueva a mares, ¿qué es?", "respuesta": "la sombra"},
                {"acertijo": "Tiene corazón pero no late, ¿qué es?", "respuesta": "el artista"},
                {"acertijo": "Siempre se tira pero nunca se moja, ¿qué es?", "respuesta": "el anzuelo"},
                {"acertijo": "Tiene pies pero no puede caminar, ¿qué es?", "respuesta": "la regla"},
                {"acertijo": "Cuanto más vacía, más pesa, ¿qué es?", "respuesta": "el agujero"}
            ],
            4: [
                {"acertijo": "Vuela sin alas, llora sin ojos, ¿qué es?", "respuesta": "la nube"},
                {"acertijo": "Siempre está delante pero nunca se ve, ¿qué es?", "respuesta": "el futuro"},
                {"acertijo": "Tiene dientes y no puede comer, ¿qué es?", "respuesta": "el peine"},
                {"acertijo": "Tiene cama pero no duerme, ¿qué es?", "respuesta": "el río"},
                {"acertijo": "Tiene agujas y no puede coser, ¿qué es?", "respuesta": "un reloj"}
            ],
            5: [
                {"acertijo": "Siempre sube y nunca baja, ¿qué es?", "respuesta": "la edad"},
                {"acertijo": "Es pequeño como un ratón pero guarda la casa como un león, ¿qué es?", "respuesta": "la cerradura"},
                {"acertijo": "Tiene ojos y no puede ver, ¿qué es?", "respuesta": "un espantapájaros"},
                {"acertijo": "Cuanto más se seca, más mojada está, ¿qué es?", "respuesta": "una toalla"},
                {"acertijo": "Tiene cabeza redonda, sombrero blanco y capa roja, ¿qué es?", "respuesta": "el champiñón"}
            ]
        }

        self.pistas = {
            1: [
                "Su función es asustar a los pájaros en los campos.",
                "Vive en el agua y necesita estar siempre mojado para sobrevivir.",
                "Es un elemento vital para todas las formas de vida.",
                "Es transparente pero puede ahogar a un hombre.",
                "Es un elemento que no se puede romper con las manos."
            ],
            2: [
                "Se encuentra en las bibliotecas y contiene historias y conocimientos.",
                "Se encuentra en lugares donde algo está faltando.",
                "Se usa para escribir y dibujar.",
                "Es un objeto que se usa para medir el tiempo.",
                "Es un objeto que se usa para abrir y cerrar puertas."
            ],
            3: [
                "Es creada por la luz.",
                "Se usa para medir o trazar líneas.",
                "Es algo que se usa en la pesca.",
                "Es algo que se usa para medir la longitud.",
                "Es un objeto que se usa para transportarse sobre el agua."
            ],
            4: [
                "Es una masa de vapor de agua suspendida en la atmósfera.",
                "Se encuentra en los relojes y marca las horas.",
                "Es algo que se usa para desenredar el cabello.",
                "Es un objeto que se usa para sujetar el cabello.",
                "Es un objeto que se usa para limpiar los dientes."
            ],
            5: [
                "Es algo que siempre aumenta a medida que pasa el tiempo.",
                "Se usa para proteger una puerta o entrada.",
                "Es algo que se encuentra en los campos y se puede cosechar.",
                "Es un objeto que se usa para proteger los ojos del sol.",
                "Es un objeto que se usa para proteger la cabeza del frío."
            ]
        }

    def obtener_acertijo(self, nivel, numero):
        return self.acertijos_respuestas[nivel][numero - 1]["acertijo"]

    def verificar_respuesta(self, nivel, numero, respuesta):
        return respuesta.lower() == self.acertijos_respuestas[nivel][numero - 1]["respuesta"]

    def obtener_pista(self, nivel, numero):
        return self.pistas[nivel][numero - 1] if numero <= len(self.pistas[nivel]) else "No hay más pistas disponibles."
