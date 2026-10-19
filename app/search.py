from data.destinations_data import filtrar_destinos
from data.accomodations_data import filtrar_alojamientos

def viaje_a_medida(entorno, sin_visado, tipo, precio_max, desayuno):
    combinaciones = []
    for destino in filtrar_destinos(entorno, sin_visado):
        alojamientos_validos = filtrar_alojamientos(
            precio_max, tipo, desayuno, False, destino["slug"]
        )
        for alojamiento in alojamientos_validos:
            combinaciones.append({"destino": destino, "alojamiento": alojamiento})
    return combinaciones

