import math

# Functie Grootcirkelafstand
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Straal van de aarde in kilometers

    # Omzetten naar radialen
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    afstand = R * c
    return afstand

# Invoer van breedte- en lengtegraden van twee lokaties:
latlons = "52.370216,4.895168 40.712776,-74.005974"

# Extract coördinaten uit het commando
try:
    coord1, coord2 = latlons.split()  # Commandosyntaxis splitsen
    lat1, lon1 = map(float, coord1.split(','))
    lat2, lon2 = map(float, coord2.split(','))

    # Grootcirkelafstand berekenen
    afstand = haversine(lat1, lon1, lat2, lon2)
    
    # Bericht voorbereiden
    print(f"\nDe grootcirkelafstand tussen de coördinaten is {afstand:.2f} kilometer.\n")

except ValueError:
    print("Ongeldig commando of coördinaten.")