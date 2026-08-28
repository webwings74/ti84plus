# Libraries
import json
import math

# Functie om de grootcirkelafstand te berekenen
def gcdist(lat1, lon1, lat2, lon2):
    # Straal van de aarde in kilometers
    R = 6371.0
    
    # Converteer graden naar radialen
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Haversine formule
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Bereken de afstand
    distance = R * c
    return distance

# Grootcircel Dictionary
payload = {
    "lata": "56.1",
    "lona": "6.1",
    "latb": "57.1",
    "lonb": "7.1"
    }

# Converteer dictionary naar JSON
json_payload = json.dumps(payload, indent=4)

# Uitvoer
print(json_payload)
lat1 = float(payload['lata'])
lon1 = float(payload['lona'])
lat2 = float(payload['latb'])
lon2 = float(payload['lonb'])

# Bereken de afstand en geef het resultaat weer
afstand = gcdist(lat1, lon1, lat2, lon2)
print("De grootcirkelafstand tussen de punten is: {:.2f} km".format(afstand))