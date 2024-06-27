import Nivel
acertijos= {
    "¿Qué tiene patas pero no puede caminar?": "Una mesa",
    "¿Qué tiene hojas pero no es un árbol?": "Un libro",
    "¿Qué es algo que se puede abrir pero no se puede cerrar?": "Un huevo",
    "Entre el clavel blanco y la roa roja, su majestas escoja. ¿Cual es el problema de su majestad?": "Es coja",
    "¿Qué es algo que va hacia arriba pero nunca regresa?": "La edad"
}
pistas = ["Un mueble comun en las casas", "Lo usas para obtener informacion", "Se come en el desayuno", "Lee lento el acertijo", "Que numero te identifica."]

nivel1 = Nivel.Nivel(acertijos,pistas, 50)

acertijos= {
    "¿Qué tiene ciudades pero no casas, ríos pero no agua, y bosques pero no árboles?": "Un mapa",
    "¿Qué tiene agujas pero no cose, y números pero no calcula?": "Un reloj",
    "¿Cuál es el animal que tiene la cola más larga del mundo?": "El elefante",
    "¿Cuál es el país más grande del mundo por área terrestre?": "Rusia",
    "¿Cuál es el océano más grande del mundo?": "El océano Pacífico"
}
pistas = ["Lo usas para guiarte", "Se pone en la muñeca", "Mamifero terrestre mas grande", "Se toma mucho vodka", "El oceano mas tranquilo"]
nivel2 = Nivel.Nivel(acertijos,pistas, 50)
acertijos = {
    "¿Cuál es el fontanero famoso de Nintendo?": "Mario",
    "¿Juego mas conocido de peleas?": "Mortal Kombat",
    "¿Qué juego popular tiene bloques que caen y debes alinearlos?": "Tetris",
    "¿En qué juego debes recolectar monedas y esquivar caparazones?": "Mario Kart",
    "¿Cuál es el juego donde debes construir y explorar un mundo infinito?": "Minecraft"
}
pistas = ["Tiene un lindo bigote", "Combate mortal", "Tiene muchos bloques", "El fontanero pero en carro", "Un mundo cubico"]
nivel3 = Nivel.Nivel(acertijos,pistas, 55)

acertijos = {
    "¿Qué emperador romano supuestamente tocaba la lira mientras Roma ardía?": "Neron",
    "¿Quién fue el primer presidente de los Estados Unidos?": "George Washington",
    "¿Qué líder militar francés conquistó gran parte de Europa en el siglo XIX?": "Napoleon Bonaparte",
    "¿Quién fue el líder político y activista que luchó por los derechos civiles en Estados Unidos en el siglo XX?": "Martin Luther King",
    "¿Qué famoso explorador italiano llegó a América en 1492?": "Cristobal Colon"
}

pistas = ["Empieza por N", "En latinoamerica le diriamos jorge", "Muy bajito", "Era color carton", "Su apellido es el mismo nombre de un cancer"]

nivel4 = Nivel.Nivel(acertijos,pistas, 55)

acertijos = {
    "Si tengo 3 manzanas y me das otras 2, ¿cuántas manzanas tengo en total?": "5",
    "Si multiplicas mis años por 2 y le sumas 10, obtienes 30. ¿Cuántos años tengo?": "10",
    "Si tengo un rectángulo con un perímetro de 20 unidades y uno de sus lados mide 4 unidades, ¿cuánto mide el otro lado?": "6",
    "Si tienes 10 caramelos y los distribuyes en 2 amigos por igual, ¿cuántos caramelos recibe cada amigo?": "5",
    "Si tienes un cubo con aristas de 3 unidades de longitud, ¿cuál es el volumen del cubo?": "27"
}

pistas = ["No esta tan dificil", "ten un regalo", "3 veces es el numero del diablo", "Lo mismo de la primera", "3 x 10 - 3"]
nivel5 = Nivel.Nivel(acertijos,pistas, 60)
lista_niveles = [nivel1, nivel2, nivel3, nivel4, nivel5]

