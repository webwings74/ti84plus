# Ti84 Grootcircel Koersen
# (c)2024, Richard

import math

def deg_to_rad(deg):
    """Zet graden om naar radialen"""
    return deg * (math.pi / 180)

def rad_to_deg(rad):
    """Zet radialen om naar graden"""
    return rad * (180 / math.pi)

def grootcirkel_koers(lat1, lon1, lat2, lon2):
    # Zet breedte- en lengtegraad om naar radialen
    lat1 = deg_to_rad(lat1)
    lon1 = deg_to_rad(lon1)
    lat2 = deg_to_rad(lat2)
    lon2 = deg_to_rad(lon2)
    
    delta_lon = lon2 - lon1
    
    # Beginkoers berekenen
    x = math.sin(delta_lon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    beginkoers = math.atan2(x, y)
    beginkoers = (rad_to_deg(beginkoers) + 360) % 360  # Om het resultaat tussen 0 en 360 graden te houden
    
    # Eindkoers berekenen
    x = math.sin(delta_lon) * math.cos(lat1)
    y = math.cos(lat2) * math.sin(lat1) - math.sin(lat2) * math.cos(lat1) * math.cos(delta_lon)
    eindkoers = math.atan2(x, y)
    eindkoers = (rad_to_deg(eindkoers)) % 360  # Eindkoers om 180 graden corrigeren en normaliseren
    
    return beginkoers, eindkoers

# Invoer coordinaten
print("\n** Ti84 Grootcircelkoersen **\n")
lat1 = float(input("Breedtegraad vertrekpunt: "))
lon1 = float(input("Lengtegraad vertrekpunt: "))
lat2 = float(input("Breedtegraad eindpunt: "))
lon2 = float(input("Lengtegraad eindpunt: "))

# Berekening
beginkoers, eindkoers = grootcirkel_koers(lat1, lon1, lat2, lon2)

# Uitvoer
print(f"De beginkoers is: {beginkoers:.2f} graden")
print(f"De eindkoers is: {eindkoers:.2f} graden\n")