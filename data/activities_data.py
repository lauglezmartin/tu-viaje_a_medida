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
