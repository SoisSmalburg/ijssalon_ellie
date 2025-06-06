# Les 10 – Opdracht 11
import csv

# Les 10 – Opdracht 4
from helper import *

# Les 10 – Opdracht 2
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750
}

# Les 10 – Opdracht 5
totaal_inkomsten = som(inkomsten)
print(f"Totaal: {totaal_inkomsten} euro")

# Les 10 – Opdracht 12
with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key, value])