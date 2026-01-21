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