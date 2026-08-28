# Inhoud van een Cylinder
# Texas Instruments Ti84

import math

def volume_cilinder(r, h):
    return math.pi * r**2 * h

print("\n** Inhoud van een Cylinder **\n")
# Vraag de gebruiker om de straal en hoogte in te voeren
straal = float(input("Straal: "))
hoogte = float(input("Hoogte: "))

# Bereken het volume van de cilinder
volume = volume_cilinder(straal, hoogte)

# Print het resultaat
print(f"Het volume van de cilinder is: {volume:.2f}")