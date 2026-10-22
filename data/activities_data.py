activities = [
    {"id": 1, "name": "Ceremonia del Té en Gion", "destination_id": 1,
     "description": "Ceremonia tradicional del té en el barrio de Gion.",
     "duration": 2, "price": 30, "difficulty": None, "min_age": None,
     "includes": "Degustación de dulces tradicionales matcha"},
    {"id": 2, "name": "Tour Nocturno por Fushimi Inari", "destination_id": 1,
     "description": "Caminata nocturna por los miles de torii de Fushimi Inari.",
     "duration": 3, "price": 40, "difficulty": "media", "min_age": 10,
     "includes": None},
    {"id": 3, "name": "Clase de Cocina Ramen y Gyozas", "destination_id": 1,
     "description": "Clase práctica para cocinar ramen y gyozas.",
     "duration": 3, "price": 65, "difficulty": None, "min_age": 12,
     "includes": "Ingredientes, delantal y recetario impreso"},
    {"id": 4, "name": "Ruta en Bicicleta por el Bosque de Bambú", "destination_id": 1,
     "description": "Recorrido en bicicleta eléctrica por el bosque de bambú.",
     "duration": 4, "price": 50, "difficulty": "baja", "min_age": None,
     "includes": "Alquiler de la bicicleta eléctrica y casco"},
    {"id": 5, "name": "Ruta de las Especias y Paseo en Dhow", "destination_id": 3,
     "description": "Visita a plantaciones de especias y paseo en barco tradicional.",
     "duration": 5, "price": 45, "difficulty": "baja", "min_age": None,
     "includes": "Almuerzo tradicional especiado"},
    {"id": 6, "name": "Snorkel en el Atolón Mnemba", "destination_id": 3,
     "description": "Excursión de snorkel en el atolón Mnemba.",
     "duration": 4, "price": 60, "difficulty": "media", "min_age": 8,
     "includes": "Tubo, gafas y aletas"},
    {"id": 7, "name": "Visita Guiada por Stone Town", "destination_id": 3,
     "description": "Paseo urbano tranquilo por el casco histórico de Stone Town.",
     "duration": 2, "price": 20, "difficulty": None, "min_age": None,
     "includes": None},
    {"id": 8, "name": "Buceo en Cenotes Sagrados", "destination_id": 4,
     "description": "Inmersión en los cenotes sagrados de la zona.",
     "duration": 4, "price": 75, "difficulty": "alta", "min_age": 16,
     "includes": "Bombona de oxígeno, linterna subacuática y traje de neopreno"},
    {"id": 9, "name": "Excursión a las Ruinas de Tulum", "destination_id": 4,
     "description": "Visita al recinto arqueológico de Tulum.",
     "duration": 6, "price": 55, "difficulty": "baja", "min_age": None,
     "includes": "Entradas al recinto y transporte en autobús"},
    {"id": 10, "name": "Paseo en Catamarán al Atardecer", "destination_id": 4,
     "description": "Paseo en catamarán para ver el atardecer en el mar.",
     "duration": 3, "price": 65, "difficulty": None, "min_age": 18,
     "includes": "Barra libre de bebidas y aperitivos a bordo"},
         {"id": 11, "name": "Crucero en Velero por la Caldera", "destination_id": 5,
     "description": "Travesía en velero alrededor de la caldera con paradas para bañarse.",
     "duration": 5, "price": 85, "difficulty": None, "min_age": None,
     "includes": "Cena a bordo y bebidas"},
    {"id": 12, "name": "Cata de Vinos Volcánicos", "destination_id": 5,
     "description": "Visita a una bodega local para probar los vinos de la isla.",
     "duration": 3, "price": 45, "difficulty": None, "min_age": 18,
     "includes": "Degustación de cinco vinos y tabla de quesos"},
    {"id": 13, "name": "Excursión a Machu Picchu", "destination_id": 6,
     "description": "Visita guiada a la ciudadela inca de Machu Picchu.",
     "duration": 10, "price": 120, "difficulty": "media", "min_age": None,
     "includes": "Tren, entradas y guía"},
    {"id": 14, "name": "Taller de Tejido Andino", "destination_id": 6,
     "description": "Taller con artesanas locales para aprender el tejido tradicional.",
     "duration": 2, "price": 25, "difficulty": None, "min_age": None,
     "includes": "Materiales y un tejido para llevarse"},
    {"id": 15, "name": "Paseo en Globo al Amanecer", "destination_id": 7,
     "description": "Vuelo en globo sobre el desierto a las afueras de la ciudad.",
     "duration": 3, "price": 140, "difficulty": "baja", "min_age": 7,
     "includes": "Desayuno bereber tras el vuelo"},
    {"id": 16, "name": "Ruta por los Zocos con Guía", "destination_id": 7,
     "description": "Paseo guiado por los zocos y las plazas de la medina.",
     "duration": 3, "price": 20, "difficulty": "baja", "min_age": None,
     "includes": None},
    {"id": 17, "name": "Clase de Surf en Kuta", "destination_id": 8,
     "description": "Clase de surf para principiantes en la playa de Kuta.",
     "duration": 2, "price": 35, "difficulty": "media", "min_age": 10,
     "includes": "Tabla, licra y monitor"},
    {"id": 18, "name": "Ruta por los Templos de Ubud", "destination_id": 8,
     "description": "Recorrido por los templos y arrozales de la zona de Ubud.",
     "duration": 5, "price": 50, "difficulty": "baja", "min_age": None,
     "includes": "Transporte y entradas"},
    {"id": 19, "name": "Ascenso al Monte Batur al Amanecer", "destination_id": 8,
     "description": "Subida nocturna al volcán para ver salir el sol desde la cima.",
     "duration": 6, "price": 55, "difficulty": "alta", "min_age": 12,
     "includes": "Linterna frontal y desayuno en la cima"},
         {"id": 20, "name": "Subida en Teleférico al Teide", "destination_id": 9,
     "description": "Subida en teleférico hasta las cercanías de la cima del Teide.",
     "duration": 4, "price": 45, "difficulty": "baja", "min_age": None,
     "includes": "Billete de ida y vuelta del teleférico"},
    {"id": 21, "name": "Avistamiento de Ballenas en Los Gigantes", "destination_id": 9,
     "description": "Salida en barco para ver delfines y calderones tropicales.",
     "duration": 3, "price": 35, "difficulty": None, "min_age": None,
     "includes": None},
    {"id": 22, "name": "Senderismo por el Parque Rural de Anaga", "destination_id": 9,
     "description": "Ruta guiada por los bosques de laurisilva de Anaga.",
     "duration": 5, "price": 30, "difficulty": "media", "min_age": 10,
     "includes": "Guía y bastones de senderismo"},
]


def obtain_activities():
    return activities


def search_activity_by_id(activity_id):
    for activity in activities:
        if activity["id"] == activity_id:
            return activity
    return None


def activities_of_destination(destination_id):
    result = []
    for activity in activities:
        if activity["destination_id"] == destination_id:
            result.append(activity)
    return result
