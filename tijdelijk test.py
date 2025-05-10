#Les 7 opdracht 1.2 
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
print(prijzen)


#Les 7 opdracht 1.3
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
aanbieding = prijzen["aardbei"] * 0.8
print(aanbieding)


#Les 7 opdracht 1.4
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
print(reclame_tekst)


#Les 7 opdracht 1.5
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
print(reclame_tekst2)

#Les 7 opdracht 1.6
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst[:63]
print(reclame_tekst3.upper())

#Les 7 opdracht 1.7
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst[:63]
reclame_tekst4 = reclame_tekst3.upper().split()
print(reclame_tekst4) 


#Les 7 opdracht 1.8
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst[:63]
reclame_tekst4 = reclame_tekst3.upper().split()
for el in reclame_tekst4:
    print(el)

#Les 7 opdracht 1.9
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst[:63]
reclame_tekst4 = reclame_tekst3.split()
for el in reclame_tekst4:
    print(el.lower())


#Les 7 opdracht 1.10
prijzen = {
     "aardbei": 3,
     "vanille": 4,
     "chocolade": 5,
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst[:63]
reclame_tekst4 = reclame_tekst3.split()
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())