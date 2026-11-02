print("Zadanie 4")

operacje = [
    {
        "opis": "zakupy",
        "kwota": 21.37,
        "rodzaj": "wydatek"
    },
    {
    "opis": "sprzedaz-vinted",
    "kwota": 120,
    "rodzaj": "przychod"
    }
]

while True:
    print("\n========== moj budzet ==========")
    print("1. Dodaj przychod")
    print("2. Dodaj wydatek")
    print("3. Wyswietl historie operacji")
    print("4. Wyswietl stan konta")
    print("5. Podsumowanie finansowe")
    print("6. Wyszukaj operacje")
    print("7. Usun operacje")
    print("0. Zakoncz")
    print("================================")

    try:
        menu_opcja = int(input("Wybierz opcje: "))
    except ValueError:
        print("Blad: podaj liczbe calkowita.")
        continue

    if menu_opcja == 0:
        print("Koniec programu.")
        break


    elif menu_opcja == 1:
        opis = input("Opis przychodu : ").strip()

        if opis =="":
            print("Blad: opis nie moze byc pusty.")
            continue

        try:
            kwota = float(input("Kwota: "))

        except ValueError:
            print("Blad: podaj prawidlowa kwote.")
            continue

        if kwota <= 0:
            print("Blad: kwota musi byc dodatnia.")
            continue

        rodzaj = "przychod"

        operacja = {
            "opis": opis,
            "kwota": kwota,
            "rodzaj": rodzaj
        }

        operacje.append(operacja)

        print("Dodano przychod.")


    elif menu_opcja == 2:
        opis = input("Opis wydatku : ").strip()

        if opis =="":
            print("Blad: opis nie moze byc pusty.")
            continue

        try:
            kwota = float(input("Kwota: "))

        except ValueError:
            print("Blad: podaj prawidlowa kwote.")
            continue

        if kwota <= 0:
            print("Blad: kwota musi byc dodatnia.")
            continue

        rodzaj = "wydatek"

        operacja = {
            "opis": opis,
            "kwota": kwota,
            "rodzaj": rodzaj
        }

        operacje.append(operacja)

        print("Dodano wydatek.")

    elif menu_opcja == 3:

        if len(operacje) == 0:
            print("Historia operacji jest pusta.")

        else:
            print("\nHistoria operacji:")


            for i in range(len(operacje)):
                print(f"{i + 1}. {operacje[i]['opis']} - "f"{operacje[i]['kwota']} zl - "f"{operacje[i]['rodzaj']}")


    elif menu_opcja == 4:

        suma_przychodow = 0
        suma_wydatkow = 0

        for operacja in operacje:
            if operacja["rodzaj"] == "przychod":
                suma_przychodow += operacja["kwota"]
            else:
                suma_wydatkow += operacja["kwota"]

        stan_konta = suma_przychodow - suma_wydatkow
        print(f"Stan konta: {stan_konta:.2f} zl")

    elif menu_opcja == 5:

        suma_przychodow = 0
        suma_wydatkow = 0
        najwiekszy_wydatek = 0

        for operacja in operacje:
            if operacja["rodzaj"] == "przychod":
                suma_przychodow += operacja["kwota"]
            else:
                suma_wydatkow += operacja["kwota"]

                if operacja["kwota"] > najwiekszy_wydatek:
                    najwiekszy_wydatek = operacja["kwota"]

        bilans = suma_przychodow - suma_wydatkow

        print(f"Suma przychodow: {suma_przychodow:.2f} zl")
        print(f"Suma wydatkow: {suma_wydatkow:.2f} zl")
        print(f"Bilans: {bilans:.2f} zl")

        if najwiekszy_wydatek == 0:
            print("Brak wydatkow.")
        else:
            print(f"Najwiekszy wydatek: {najwiekszy_wydatek:.2f} zl")

    elif menu_opcja == 6:
        print("opcja nieaktywna")

    elif menu_opcja == 7:

        if len(operacje) == 0:
            print("Historia operacji jest pusta.")
            continue

        print("\nHistoria operacji:")

        for i in range(len(operacje)):

            print(f"{i + 1}. {operacje[i]['opis']} - "f"{operacje[i]['kwota']} zl - "f"{operacje[i]['rodzaj']}")

        try:
            numer = int(input("Podaj numer operacji do usuniecia: "))

        except ValueError:
            print("Blad: podaj prawidlowy numer.")
            continue

        if numer < 1 or numer > len(operacje):

            print("Blad: nie ma operacji o takim numerze.")

        else:

            usunieta_operacja = operacje.pop(numer - 1)
            print("Usunieto operacje:", usunieta_operacja["opis"])

    else:
        print("Blad: nieprawidlowa opcja menu.")


