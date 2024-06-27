from clases import Vuelo

vuelo = Vuelo("Ciudad A", "Ciudad B", 100)

vuelo.consultar_disponibilidad()

vuelo.reservar_asientos(2)
vuelo.consultar_disponibilidad()

vuelo.reservar_asientos(100)
vuelo.consultar_disponibilidad()