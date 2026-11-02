
kontakty = {
    "111111111": ["Jan", "Kowalski"],
    "222222222": ["Anna", "Nowak"],
    "554444433": ["Piotr", "Wisniewski"],
}


print("Zadanie 1 \n")

while True:
    print("\n========== Ksiazka Kontaktow ==========")
    print("1. Dodaj kontakt")
    print("2. Wyswietl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Edytuj kontakt")
    print("5. Usun kontakt")
    print("0. Zakoncz")
    print("=======================================")

    try:
        menu_opcja = int(input("Wybierz opcje: "))
    except ValueError:
        print("Blad: podaj liczbe calkowita.")
        continue

    if menu_opcja == 1:
        imie = input("Imie: ").strip()
        nazwisko = input("Nazwisko: ").strip()
        telefon = input("Telefon: ").strip()

        if imie == "" or nazwisko == "" or telefon == "":

            print("Blad: wszystkie pola musza byc wypelnione.")

        elif telefon in kontakty:
            print("Blad: kontakt o tym numerze juz istnieje.")

        else:
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt dodany.")

    elif menu_opcja == 2:
        if len(kontakty) == 0:
            print("Ksiazka kontaktow jest pusta.")
        else:
            print("\nLista kontaktow: ")


            for telefon in kontakty:
                print(f"{kontakty[telefon][0]} {kontakty[telefon][1]}- {telefon}")


    elif menu_opcja == 3:

        telefon = input("Podaj numer telefonu: ").strip()

        if telefon in kontakty:

            print(f"Imie: {kontakty[telefon][0]}")

            print(f"Nazwisko: {kontakty[telefon][1]}")

            print(f"Telefon: {telefon}")

        else:
            print("Nie znaleziono kontaktu.")


    elif menu_opcja == 4:

        telefon = input("Podaj numer telefonu kontaktu do edycji: ").strip()

        if telefon not in kontakty:
            print("Blad: Nie znaleziono kontaktu.")
        else:
            print(f"Obecne imie: {kontakty[telefon][0]}")


            print(f"Obecne nazwisko: {kontakty[telefon][1]}")

            imie = input("Nowe imie: ").strip()
            nazwisko = input("Nowe nazwisko: ").strip()

            if imie == "" or nazwisko == "":
                print("Blad: imie i nazwisko nie moga miec  pustego pola.")

            else:
                kontakty[telefon] = [imie, nazwisko]
                print("Kontakt zaktualizowany.")

    elif menu_opcja == 5:
        telefon = input("Podaj numer telefonu kontaktu do usuniecia: ").strip()

        if telefon in kontakty:


            kontakty.pop(telefon)

            print("Kontakt usuniety.")
        else:
            print("Nie znaleziono kontaktu.")

    elif menu_opcja == 0:
        print("Koniec programu.")
        break

    else:
        print("Blad: nieprawidlowa opcja.")
