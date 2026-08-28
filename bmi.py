# BMI Berekening
# Van een input-string naar een float en terug naar een string-output.
# Update 27 maart 2023 -> Github
# input en output en een kleine berekening met floats

print("\n*** BMI Berekening ***")
print("Gebruik een . als scheidingsteken voor decimalen!")
print("Geef uw massa in kilogram: "),
massa_kg = float(input())
print("Geef uw lengte in meter: "),
lengte_m = float(input())
bmi = massa_kg / (lengte_m * lengte_m)
print("Uw BMI bedraagt: " + str(round(bmi,2)) + ".")
print("\nEinde van het programma.")

# Einde BMI