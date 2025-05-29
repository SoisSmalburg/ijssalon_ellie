# Les 8 opdracht 2
def mijn_functie_1(getal):
    return getal ** 2

tabel_functie_1 = [2, 4, 10, 12]

for argument in tabel_functie_1:
    print(mijn_functie_1(argument))


    
# Les 8 opdracht 3
def mijn_functie_2(a, b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a + b)
    uitvoer_lijst.append(a - b)
    uitvoer_lijst.append(a * b)
    uitvoer_lijst.append(a / b)
    return uitvoer_lijst

tabel_functie_2 = [
    (12, 3),
    (12, 2),
    (10, 5),
    (100, 20)
]

for a, b in tabel_functie_2:
    print(mijn_functie_2(a, b))