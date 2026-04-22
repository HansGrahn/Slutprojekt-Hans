import csv
import os

FIL = "kontakter.csv"
telefonbok = {}


def ladda_från_csv():
    #Läser in kontakter från CSV-filen vid start.
    if not os.path.exists(FIL):
        return
    with open(FIL, newline="", encoding="utf-8") as f:
        läsare = csv.DictReader(f)
        for rad in läsare:
            telefonbok[rad["namn"]] = rad["nummer"]
    print(f"{len(telefonbok)} kontakt(er) laddades från {FIL}")


def spara_till_csv():
    #Skriver alla kontakter till CSV-filen.
    with open(FIL, "w", newline="", encoding="utf-8") as f:
        skrivare = csv.DictWriter(f, fieldnames=["namn", "nummer"])
        skrivare.writeheader()
        for namn, nummer in sorted(telefonbok.items()):
            skrivare.writerow({"namn": namn, "nummer": nummer})


def lägg_till_kontakt():
    namn = input("Namn: ").strip()
    if not namn:
        print("Namnet får inte vara tomt.")
        return
    if namn in telefonbok:
        print(f"'{namn}' finns redan. Använd 'ändra' för att uppdatera.")
        return
    nummer = input("Telefonnummer: ").strip()
    if not nummer:
        print("Numret får inte vara tomt.")
        return
    telefonbok[namn] = nummer
    spara_till_csv()
    print(f"{namn} har lagts till och sparats.")
    os.system("pause")


def sök_kontakt():
    sökterm = input("Sök namn: ").strip().lower()
    resultat = {namn: nr for namn, nr in telefonbok.items() if sökterm in namn.lower()}
    if resultat:
        print(f"\n{'Namn':<20} {'Nummer'}")
        print("-" * 35)
        for namn, nummer in resultat.items():
            print(f"{namn:<20} {nummer}")
    else:
        print("Ingen kontakt hittades.")
    os.system("pause")


def visa_alla():
    if not telefonbok:
        print("Telefonboken är tom.")
        return
    print(f"\n{'Namn':<20} {'Nummer'}")
    print("-" * 35)
    for namn, nummer in sorted(telefonbok.items()):
        print(f"{namn:<20} {nummer}")
    print(f"\nTotalt: {len(telefonbok)} kontakt(er)  |  Fil: {FIL}")
    os.system("pause")

def ta_bort_kontakt():
    namn = input("Namn på kontakt att ta bort: ").strip()

    # spelar ej roll om stor eller liten bokstav
    hittad = None
    for kontakt in telefonbok:
        if kontakt.lower() == namn.lower():
            hittad = kontakt
            break

    if hittad:
        del telefonbok[hittad]
        spara_till_csv()
        print(f"{hittad} har tagits bort.")
    else:
        print(f"'{namn}' hittades inte.")

    os.system("pause")




def visa_meny():
    print("\n=== TELEFONBOK ===")
    print("1. Lägg till kontakt")
    print("2. Visa alla kontakter")
    print("3. Sök")
    print("4. Ändra kontakt")
    print("5. Ta bort kontakt")
    print("6. Avsluta")
    print("====================")


def main():
    ladda_från_csv()
    while True:
        visa_meny()
        val = input("Välj (1-6): ").strip()
        if val == "1":
            lägg_till_kontakt()
        elif val == "2":
            visa_alla()
        elif val == "3":
            sök_kontakt()
        elif val == "4":
            pass
        elif val == "5":
            ta_bort_kontakt()
        elif val == "6":
            print("Hejdå!")
            break
        else:
            print("Ogiltigt val. Ange en siffra mellan 1 och 6.")


if __name__ == "__main__":
    main()
    