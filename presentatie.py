# Les 10 – Opdracht 7 + 8
def presenteer(dictionary, totaal):
    for key, value in dictionary.items():
        print(f"{key} : {value} euro")
    print("=" * 30)
    print(f"Totaal : {totaal} euro")

# Alleen uitvoeren als dit bestand direct wordt gestart
if __name__ == "__main__":
    mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}
    totaal = sum(mijn_dict.values())
    presenteer(mijn_dict, totaal)