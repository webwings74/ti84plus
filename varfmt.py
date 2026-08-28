# Uitproberen van een manier om een variable mee te geven aan
# de format functie. Standaard Python op Ti-84 rekenmachine.

print("\n** Kolombreedte Format **")
breedte = str(input("\nGeef de kolombreedte op: "))
tekst = str(input("Geef de tekst op: "))

uitvoer = "De tekst in een vak van {0} letters:\n\n[{1:" + breedte + "}]"
print(uitvoer.format(breedte,tekst))
print("\nEinde programma.")