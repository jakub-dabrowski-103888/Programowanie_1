print("Zadanie 3\n")


biblioteka = [

{
        "tytul": "Hobbit",
        "autor": "J.R.R. Tolkien",
        "dostepna": True
    },



    {
        "tytul": "Wiedzmin",
        "autor": "Andrzej Sapkowski",
        "dostepna": False
    }
]




while True:

    print("\n========== Biblioteka ==========")
    print("1. Dodaj ksiazke")
    print("2. Wyswietl wszystkie ksiazki")
    print("3. Wypozycz ksiazke")
    print("4. Zwroc ksiazke")
    print("5. Usun ksiazke")
    print("0. Zakoncz")
    print("================================")

    try:
        menu_opcja = int(input("Wybierz opcje: "))
    except ValueError:
        print("Blad: podaj liczbe calkowita.")
        continue

    if menu_opcja == 1:
        tytul = input("Tytul: ").strip()
        autor = input("Autor: ").strip()

        if tytul == "" or autor == "":
            print("Blad: pole tytul lub autor nie moga byc puste.")
        else:
            ksiazka = {
                "tytul": tytul,
                "autor": autor,
                "dostepna": True
            }

            biblioteka.append(ksiazka)

            print("Ksiazka dodana.")

    elif menu_opcja == 2:

        ilosc_ksiazek=len(biblioteka)

        if ilosc_ksiazek == 0:
            print("Biblioteka jest pusta.")
        else:

            print("\n Lista ksiazek:")

            for i in range(ilosc_ksiazek):
                print(f"{i + 1}. {biblioteka[i]['tytul']} - {biblioteka[i]['autor']}")

                if biblioteka[i]["dostepna"] == True:
                    print(" Status: Dostepna")
                else:
                    print(" Status: Wypozyczona")

    elif menu_opcja == 3:

        ilosc_ksiazek = len(biblioteka)

        if ilosc_ksiazek == 0:
            print("Biblioteka jest pusta.")
            continue

        try:
            numer = int(input("Numer ksiazki do wypozyczenia: "))
        except ValueError:
            print("Blad: podaj prawidlowy numer.")
            continue

        if numer < 1 or numer > ilosc_ksiazek:
            print("Blad: nie ma ksiazki o takim numerze.")


        elif biblioteka[numer - 1]["dostepna"] == False:
            print(" ksiazka jest wypozyczona.")


        else:
            biblioteka[numer - 1]["dostepna"] = False
            print("Wypozyczono:", biblioteka[numer - 1]["tytul"])

    elif menu_opcja == 4:
        ilosc_ksiazek = len(biblioteka)

        if ilosc_ksiazek == 0:
            print("Biblioteka jest pusta.")
            continue

        try:
            numer = int(input("Numer ksiazki do zwrotu: "))

        except ValueError:
            print("Blad: podaj prawidlowy numer.")
            continue

        if numer < 1 or numer >ilosc_ksiazek:
            print("Blad: nie ma ksiazki o takim numerze.")


        elif biblioteka[numer - 1]["dostepna"] == True:

            print("Ta ksiazka nie jest wypozyczona.")


        else:
            biblioteka[numer - 1]["dostepna"] = True
            print("Zwrocono:", biblioteka[numer - 1]["tytul"])

    elif menu_opcja == 5:

        ilosc_ksiazek = len(biblioteka)

        if ilosc_ksiazek == 0:
            print("Biblioteka jest pusta.")
            continue

        try:
            numer = int(input("Numer ksiazki do usuniecia: "))

        except ValueError:
            print("Blad: podaj prawidlowy numer.")
            continue

        if numer < 1 or numer > ilosc_ksiazek:
            print("Blad: nie ma ksiazki o takim numerze.")
        else:
            do_usuniecia = biblioteka.pop(numer - 1)
            print("Usunieto ksiazke:", do_usuniecia["tytul"])

    elif menu_opcja==0:
        print("Koniec programu.")
        break

    else:
        print("Blad: nieprawidlowa opcja menu.")