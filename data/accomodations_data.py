accomodations = [
    {"id": 1, "name": "Ryokan Tradicional Gion", "type": "hotel", "destination_id": 1,
     "price": 140, "breakfast": True, "pets": False,
     "stars": 4, "extra": "Baño termal privado en la habitación"},
    {"id": 2, "name": "Capsule Hostel Urban", "type": "hostal", "destination_id": 1,
     "price": 35, "breakfast": False, "pets": False,
     "stars": 2, "extra": None},
    {"id": 3, "name": "Apartamento Bambú Arashiyama", "type": "apartamento", "destination_id": 1,
     "price": 95, "breakfast": False, "pets": True,
     "stars": None, "extra": "Terraza con vistas al río"},
    {"id": 4, "name": "Rorbu Fjord Cabins", "type": "cabaña", "destination_id": 2,
     "price": 160, "breakfast": True, "pets": True,
     "stars": 4, "extra": "Acceso directo al muelle del fiordo"},
    {"id": 5, "name": "Arctic Light Hotel", "type": "hotel", "destination_id": 2,
     "price": 210, "breakfast": True, "pets": False,
     "stars": 5, "extra": "Mirador acristalado en la azotea"},
    {"id": 6, "name": "Refugio de Pescadores Svolvær", "type": "hostal", "destination_id": 2,
     "price": 55, "breakfast": False, "pets": True,
     "stars": None, "extra": None},
    {"id": 7, "name": "Hostal Caribe Maya", "type": "hostal", "destination_id": 4,
     "price": 25, "breakfast": True, "pets": True,
     "stars": 2, "extra": None},
    {"id": 8, "name": "Eco-Villas Tulum Road", "type": "cabaña", "destination_id": 4,
     "price": 110, "breakfast": False, "pets": True,
     "stars": 3, "extra": "Funciona al 100% con energía solar"},
    {"id": 9, "name": "Grand Resort Riviera", "type": "hotel", "destination_id": 4,
     "price": 190, "breakfast": True, "pets": False,
     "stars": 5, "extra": "Club de playa privado"},
    {"id": 10, "name": "Loft Quinta Avenida", "type": "apartamento", "destination_id": 4,
     "price": 80, "breakfast": False, "pets": False,
     "stars": None, "extra": None},
         {"id": 11, "name": "Hotel Caldera Blue", "type": "hotel", "destination_id": 5,
     "price": 220, "breakfast": True, "pets": False,
     "stars": 5, "extra": "Piscina infinita con vistas a la caldera"},
    {"id": 12, "name": "Casa Blanca Oia", "type": "apartamento", "destination_id": 5,
     "price": 120, "breakfast": False, "pets": True,
     "stars": None, "extra": "Terraza privada con vistas al atardecer"},
    {"id": 13, "name": "Hotel Plaza Inca", "type": "hotel", "destination_id": 6,
     "price": 95, "breakfast": True, "pets": False,
     "stars": 4, "extra": "Calefacción en todas las habitaciones"},
    {"id": 14, "name": "Hostal Valle Sagrado", "type": "hostal", "destination_id": 6,
     "price": 30, "breakfast": True, "pets": True,
     "stars": 2, "extra": None},
    {"id": 15, "name": "Riad Jardín Secreto", "type": "hotel", "destination_id": 7,
     "price": 85, "breakfast": True, "pets": False,
     "stars": 4, "extra": "Patio interior con piscina"},
    {"id": 16, "name": "Hostal Medina Azul", "type": "hostal", "destination_id": 7,
     "price": 28, "breakfast": False, "pets": True,
     "stars": None, "extra": None},
    {"id": 17, "name": "Villa Arrozales Ubud", "type": "cabaña", "destination_id": 8,
     "price": 75, "breakfast": True, "pets": True,
     "stars": 3, "extra": "Vistas a los campos de arroz"},
    {"id": 18, "name": "Bali Surf Hostel", "type": "hostal", "destination_id": 8,
     "price": 22, "breakfast": False, "pets": False,
     "stars": 2, "extra": "Tablas de surf de alquiler en recepción"},
         {"id": 19, "name": "Hotel Teide Vista", "type": "hotel", "destination_id": 9,
     "price": 105, "breakfast": True, "pets": False,
     "stars": 4, "extra": "Piscina climatizada con vistas al Teide"},
    {"id": 20, "name": "Finca Los Gigantes", "type": "cabaña", "destination_id": 9,
     "price": 70, "breakfast": False, "pets": True,
     "stars": 3, "extra": "Jardín privado con árboles frutales"},
]


def obtain_accomodations():
    return accomodations


def search_accomodation_by_id(accomodation_id):
    for accomodation in accomodations:
        if accomodation["id"] == accomodation_id:
            return accomodation
    return None


# todos los alojamientos cuyo destination_id coincide con el id que nos pasan
# si el destino no tiene ninguno (Zanzibar) devuelve una lista vacia, no da error
def accomodations_of_destination(destination_id):
    result = []
    for accomodation in accomodations:
        if accomodation["destination_id"] == destination_id:
            result.append(accomodation)
    return result


# funcion con todos los criterios posibles para poder reutilizarla
# el comparador no pasa destination_id (busca en todo el mundo)
# el asistente si lo pasa, para buscar dentro de cada destino
# breakfast y pets en True significa que es imprescindible, en False no importa
def filter_accomodations(max_price, accomodation_type="", breakfast=False, pets=False, destination_id=None):
    result = []
    for accomodation in accomodations:
        if accomodation["price"] > max_price:
            continue
        if accomodation_type != "" and accomodation["type"] != accomodation_type:
            continue
        if breakfast and not accomodation["breakfast"]:
            continue
        if pets and not accomodation["pets"]:
            continue
        if destination_id is not None and accomodation["destination_id"] != destination_id:
            continue
        result.append(accomodation)
    return result
