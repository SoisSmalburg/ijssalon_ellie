def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag/personen
    except:
        bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro"

def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

if __name__ == "__main__":
    b = int(input("Welk bedrag zit er in de fooienpot? "))
    p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))
    resultaat = fooi_pp(b, p)
    decoreer(resultaat)