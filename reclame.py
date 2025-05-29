from algemene_functies import mijn_functie_2
#Les 8 opdracht 5
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    nieuwe_prijs = round(nieuwe_prijs, 2)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro.")
aanbieding_1("aardbei", 4, 0.1)   


#Les 8 opdracht 6
def inkomsten_totaal(inkomsten_lijst):
    totaal = sum(inkomsten_lijst)
    return totaal

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]

totaal_bedrag = inkomsten_totaal(week_inkomsten)
print(totaal_bedrag)


#Les 8 opdracht 7
def inkomsten_totaal(inkomsten_lijst, btw):
    totaal = sum(inkomsten_lijst)
    btw_bedrag = round(totaal * btw, 2)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(week_inkomsten, 0.09))


#Les 8 opdracht 8
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(inkomsten))


#Les 8 opdracht 9
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    return totaal / aantal

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(week_inkomsten))


#Les 8 opdracht 10
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_inkomsten = round(totaal / aantal, 2)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(week_inkomsten))


#Les 8 opdracht 11
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

getallen = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(getallen))


#Les 8 opdracht 12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

voorbeeld_lijst = [10, 2, 8, 5, 3]
print(combinatie(voorbeeld_lijst))

