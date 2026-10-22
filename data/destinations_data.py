destinations = [
    {
        "id": 1,
        "name": "Kioto",
        "country": "Japón",
        "environment": "ciudad",
        "high_season": "primavera",
        "visa": False,
        "advise": "La moneda local es el yen y recomendamos llevar siempre efectivo para el acceso a los templos tradicionales.",
        "imag": None,
    },
    {
        "id": 2,
        "name": "Islas Lofoten",
        "country": "Noruega",
        "environment": "montaña",
        "high_season": "invierno",
        "visa": False,
        "advise": "Es imprescindible viajar con ropa térmica extrema y calzado impermeable.",
        "imag": None,
    },
    {
        "id": 3,
        "name": "Zanzíbar",
        "country": "Tanzania",
        "environment": "playa",
        "high_season": "verano",
        "visa": True,
        "advise": None,
        "imag": None,
    },
    {
        "id": 4,
        "name": "Playa del Carmen",
        "country": "México",
        "environment": "playa",
        "high_season": "verano",
        "visa": False,
        "advise": "La moneda es el peso mexicano, aunque aceptan dólares en casi todas las zonas turísticas.",
        "imag": None,
    },
        {
        "id": 5,
        "name": "Santorini",
        "country": "Grecia",
        "environment": "playa",
        "high_season": "verano",
        "visa": False,
        "advise": None,
        "imag": None,
    },
    {
        "id": 6,
        "name": "Cusco",
        "country": "Perú",
        "environment": "montaña",
        "high_season": "invierno",
        "visa": False,
        "advise": "La ciudad está a más de 3.000 metros de altitud, conviene pasar un par de días aclimatándose antes de hacer excursiones.",
        "imag": None,
    },
    {
        "id": 7,
        "name": "Marrakech",
        "country": "Marruecos",
        "environment": "ciudad",
        "high_season": "primavera",
        "visa": False,
        "advise": "La moneda es el dírham marroquí y en los zocos es habitual regatear el precio.",
        "imag": None,
    },
    {
        "id": 8,
        "name": "Bali",
        "country": "Indonesia",
        "environment": "playa",
        "high_season": "verano",
        "visa": True,
        "advise": "La moneda es la rupia indonesia y conviene llevar repelente de mosquitos.",
        "imag": None,
    },
        {
        "id": 9,
        "name": "Tenerife",
        "country": "España",
        "environment": "playa",
        "high_season": "verano",
        "visa": False,
        "advise": "El tiempo cambia mucho entre la costa y el Teide, conviene llevar una chaqueta si se sube a la montaña.",
        "imag": None,
    },
]


# devuelve la lista completa
def obtain_destinations():
    return destinations


# recorre la lista y devuelve el destino cuyo id coincide
# si no lo encuentra devuelve None, y el controlador decide si lanza el 404
def search_destination_by_id(destination_id):
    for destination in destinations:
        if destination["id"] == destination_id:
            return destination
    return None


# environment vacio significa cualquiera, wo_visa en False significa que no se filtra por visado
# usamos continue para saltar al siguiente destino cuando no cumple una condicion
# solo los que pasan todas las condiciones llegan al append que los añade a result
def filter_destinations(environment="", wo_visa=False):
    result = []
    for destination in destinations:
        if environment != "" and destination["environment"] != environment:
            continue
        if wo_visa and destination["visa"]:
            continue
        result.append(destination)
    return result
