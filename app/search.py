from data.destinations_data import filter_destinations
from data.accomodations_data import filter_accomodations


# primero filtramos los destinos por environment y visa
# despues, por cada destino que sirve, buscamos sus alojamientos que cumplan el resto
# cada combinacion valida se guarda como un diccionario con destination y accomodation
# si un destino no tiene alojamientos validos (Zanzibar) simplemente no aporta combinaciones
def custom_trip(environment, wo_visa, accomodation_type, max_price, breakfast):
    combinations = []
    for destination in filter_destinations(environment, wo_visa):
        valid_accomodations = filter_accomodations(
            max_price, accomodation_type, breakfast, False, destination["id"]
        )
        for accomodation in valid_accomodations:
            combinations.append({"destination": destination, "accomodation": accomodation})
    return combinations
