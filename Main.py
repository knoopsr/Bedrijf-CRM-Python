import crud_functies as db

def bedrijf_aanmaken():
    name = input("Bedrijf naam: ").strip()
    vat_number = input("Bedrijf vat number: ").strip()

    if not name or not vat_number:
        print("Naam en VAT-nummer zijn verplicht.")
        return

    db.create_company(name, vat_number)
    print("Bedrijf aangemaakt.")

import crud_functies as db


def bedrijf_tonen():
    rows = db.list_companies()

    if not rows:
        print("Geen bedrijven gevonden.")
        return

    # Header
    print("\nBEDRIJVEN")
    print("-" * 80)
    print(f"{'ID':>4}  {'Naam':<30}  {'BTW':<15}  {'Aangemaakt':<19}")
    print("-" * 80)

    # Rows
    for r in rows:
        vat = r["vat_number"] if r["vat_number"] else "-"
        created = str(r["created_at"])  # meestal al 'YYYY-MM-DD HH:MM:SS'
        print(f"{r['id']:>4}  {r['name']:<30}  {vat:<15}  {created:<19}")

    print("-" * 80)





def menu():
    while True:
        print("1 bedrijf aanmaken")
        print("2 bedrijven tonen")
        print("3 bedrijf aanpassen")
        print("4 bedrijf verwijderen")
        print("5 contact aanmaken")
        print("6 contacten tonen")
        print("7 contact aanpassen")
        print("8 contact verwijderen")
        print("9 toon bedrijven met contacten (genest)")
        print("0 stop")

        keuze = input("Geef de keuze: ")

        if keuze == "1":
            bedrijf_aanmaken()
        elif keuze == "2":
            bedrijf_tonen()
        elif keuze == "3":
            bedrijf_aanpassen()
        elif keuze == "4":
            bedrijf_verwijderen()
        elif keuze == "5":
            contact_aanmaken()
        elif keuze == "6":
            contact_tonen()
        elif keuze == "7":
            contact_aanpassen()
        elif keuze == "8":
            contact_verwijderen()
        elif keuze == "9":
            toon_bedrijven_met_contacten()
        elif keuze == "0":
            print("programma gestopt")
            break

        else:
            print("Ongeldige keuze.")
menu()