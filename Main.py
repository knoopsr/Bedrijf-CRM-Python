import crud_functies as db

def bedrijf_aanmaken():
    name = input("Bedrijf naam: ").strip()
    vat_number = input("Bedrijf vat number: ").strip()

    if not name or not vat_number:
        print("Naam en VAT-nummer zijn verplicht.")
        return

    db.create_company(name, vat_number)
    print("Bedrijf aangemaakt.")




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





def bedrijf_aanpassen():
    try:
        bedrijf_id = int(input("Geef het ID van het bedrijf dat je wil aanpassen: "))
    except ValueError:
        print("Ongeldig ID.")
        return

    bedrijf = db.get_company(bedrijf_id)

    if not bedrijf:
        print("Bedrijf niet gevonden.")
        return

    print("\nHuidige gegevens:")
    print(f"Naam: {bedrijf['name']}")
    print(f"BTW-nummer: {bedrijf['vat_number']}")
    print(f"Aangemaakt: {bedrijf['created_at']}")

    print("\nLaat een veld leeg om de huidige waarde te behouden.\n")

    # Nieuwe waarden vragen
    new_name = input("Nieuwe naam: ").strip()
    new_vat = input("Nieuw BTW-nummer: ").strip()

    # Lege velden behouden de oude waarde
    name = new_name if new_name else bedrijf["name"]
    vat = new_vat if new_vat else bedrijf["vat_number"]

    # Update uitvoeren
    db.update_company(bedrijf_id, name, vat)

    print("Bedrijf succesvol aangepast.")




def bedrijf_verwijderen():
    try:
        bedrijf_id = int(input("Geef het ID van het bedrijf dat je wil verwijderen: "))
    except ValueError:
        print("Ongeldig ID.")
        return

    bedrijf = db.get_company(bedrijf_id)

    if not bedrijf:
        print("Bedrijf niet gevonden.")
        return

    print("\nJe staat op het punt om dit bedrijf te verwijderen:")
    print(f"ID: {bedrijf['id']}")
    print(f"Naam: {bedrijf['name']}")
    print(f"BTW: {bedrijf['vat_number']}")
    print(f"Aangemaakt: {bedrijf['created_at']}")

    bevestiging = input("Weet je zeker dat je dit bedrijf wil verwijderen? (j/n): ").lower()

    if bevestiging != "j":
        print("Verwijderen geannuleerd.")
        return

    if db.delete_company(bedrijf_id) != 0:
        print("Bedrijf succesvol verwijderd.")
        return

    print("Bedrijf is niet verwijderd!")





def contact_aanmaken():
    print("\nNIEUW CONTACT AANMAKEN")
    print("-" * 40)

    first = input("Naam: ").strip()

    email = input("Email: ").strip()
    phone = input("Telefoon (optioneel): ").strip()
    company_id = input("Bedrijf ID: ").strip()

    # Validatie verplichte velden
    if not first  or not email or not company_id:
        print("Voornaam, email en bedrijf ID zijn verplicht.")
        return

    # Bedrijf ID moet een getal zijn
    try:
        company_id = int(company_id)
    except ValueError:
        print("Ongeldig bedrijf ID.")
        return

    # Contact opslaan
    db.create_contact(company_id, first, email, phone)

    print("Contact succesvol aangemaakt.")







def contact_tonen():
    rows = db.list_contacts()

    if not rows:
        print("Geen contacten gevonden.")
        return

    print("\nCONTACTEN")
    print("-" * 100)
    print(f"{'ID':>4}  {'Naam':<25}  {'Email':<30}  {'Telefoon':<15}  {'Bedrijf ID':<10}")
    print("-" * 100)

    for c in rows:
        naam = f"{c['name']}"
        email = c['email'] or "-"
        phone = c['phone'] or "-"
        company = c['company_id'] or "-"

        print(f"{c['id']:>4}  {naam:<25}  {email:<30}  {phone:<15}  {company:<10}")

    print("-" * 100)





def contact_aanpassen():
    try:
        contact_id = int(input("Geef het ID van het contact dat je wil aanpassen: "))
    except ValueError:
        print("Ongeldig ID.")
        return

    contact = db.get_contact(contact_id)

    if not contact:
        print("Contact niet gevonden.")
        return

    print("\nHuidige gegevens:")
    print(f"Naam: {contact['name']}")
    print(f"Email: {contact['email']}")
    print(f"Telefoon: {contact['phone']}")

    print("\nLaat leeg om de huidige waarde te behouden.\n")

    # Nieuwe waarden vragen
    new_first = input("Nieuwe naam: ").strip()
    new_email = input("Nieuwe email: ").strip()
    new_phone = input("Nieuwe telefoon: ").strip()

    # Lege velden behouden de oude waarde
    first = new_first if new_first else contact["name"]
    email = new_email if new_email else contact["email"]
    phone = new_phone if new_phone else contact["phone"]


    # Update uitvoeren
    db.update_contact(contact_id, first, email, phone)

    print("Contact succesvol aangepast.")




def contact_verwijderen():
    try:
        contact_id = int(input("Geef het ID van het contact dat je wil verwijderen: "))
    except ValueError:
        print("Ongeldig ID.")
        return

    # Ophalen van het contact om te tonen wat je gaat verwijderen
    contact = db.get_contact(contact_id)

    if not contact:
        print("Contact niet gevonden.")
        return

    # Contact tonen ter bevestiging
    naam = f"{contact['name']}"
    email = contact['email']
    print(f"\nJe staat op het punt om dit contact te verwijderen:")
    print(f"ID: {contact_id}")
    print(f"Naam: {naam}")
    print(f"Email: {email}")

    bevestiging = input("Weet je zeker dat je dit contact wil verwijderen? (j/n): ").lower()

    if bevestiging != "j":
        print("Verwijderen geannuleerd.")
        return

    # Verwijderen uitvoeren
    db.delete_contact(contact_id)
    print("Contact verwijderd.")




def toon_bedrijven_met_contacten():
    rows = db.list_companies_with_contacts_list()

    if not rows:
        print("Geen bedrijven gevonden.")
        return

    print("\nBEDRIJVEN MET CONTACTEN")
    print("=" * 80)

    for bedrijf in rows:
        print(f"\nBedrijf: {bedrijf[1]} (ID {bedrijf[0]})")
        print(f"BTW: {bedrijf[2] or '-'}")
        print(f"Aangemaakt: {bedrijf[3]}")
        print("-" * 80)

        contacten = bedrijf[4]

        if not contacten:
            print("  Geen contacten voor dit bedrijf.")
            continue

        # Header
        print(f"  {'ID':>4}  {'Naam':<25}  {'Email':<30}")
        print(f"  {'-' * 70}")

        # Rows
        for c in contacten:
            naam = f"{c[1]}"
            contactid = f"{c[0]}"
            email = f"{c[2]}"
            print(f"  {contactid:>4}  {naam:<25}  {email:<30}")

    print("\n" + "=" * 80)


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