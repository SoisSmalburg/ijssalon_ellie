def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append("=" * len(tekst))
    return uit

def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

uitvoer = onderstreep("AANBIEDING")
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

print()

for el in uitvoer:
    print(el)

# Les 10 – Opdracht 3

def som(dictionary):
    return sum(dictionary.values())

