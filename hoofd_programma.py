from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")

uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

for regel in uitvoer:
    print(regel)