from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic

# Función para obtener coordenadas usando la API de OpenCage
def get_coordinates(city, api_key):
    geocoder = OpenCageGeocode(api_key)
    results = geocoder.geocode(city)
    if results and len(results):
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        return (lat, lng)
    else:
        return None

# Función para calcular la distancia entre dos coordenadas
def calculate_distance(coord1, coord2):
    distance_km = geodesic(coord1, coord2).kilometers
    distance_mi = geodesic(coord1, coord2).miles
    return distance_km, distance_mi

# Función para estimar la duración del viaje
def estimate_travel_duration(distance_km, transport_mode):
    if transport_mode == 'coche':
        speed_kmh = 80  # Velocidad promedio en km/h para coche
    elif transport_mode == 'avión':
        speed_kmh = 800  # Velocidad promedio en km/h para avión
    else:
        speed_kmh = 50  # Velocidad promedio en km/h para otros medios de transporte
    duration_hours = distance_km / speed_kmh
    return duration_hours

# Función para imprimir la narrativa del viaje
def print_travel_narrative(city1, city2, distance_km, distance_mi, transport_mode, duration_hours):
    print(f"La distancia entre {city1} y {city2} es:")
    print(f"{distance_km:.2f} kilómetros")
    print(f"{distance_mi:.2f} millas")
    print(f"Duración estimada del viaje en {transport_mode}: {duration_hours:.2f} horas")

def main():
    api_key = '49ca5ace15de497c8709e6416fc848b9'

    while True:
        # Obtener entrada del usuario
        city1 = input("Ingrese la ciudad de origen (Chile) o 's' para salir: ")
        if city1.lower() == 's':
            break
        city2 = input("Ingrese la ciudad de destino (Argentina): ")
        transport_mode = input("Ingrese el medio de transporte (e.g., coche, avión, etc.): ")

        # Obtener coordenadas para ambas ciudades
        coord1 = get_coordinates(city1, api_key)
        coord2 = get_coordinates(city2, api_key)

        if coord1 and coord2:
            # Calcular distancias
            distance_km, distance_mi = calculate_distance(coord1, coord2)

            # Estimar duración del viaje
            duration_hours = estimate_travel_duration(distance_km, transport_mode)

            # Imprimir narrativa del viaje
            print_travel_narrative(city1, city2, distance_km, distance_mi, transport_mode, duration_hours)
        else:
            print("No se pudieron obtener las coordenadas para una o ambas ciudades.")

if __name__ == "__main__":
    main()
